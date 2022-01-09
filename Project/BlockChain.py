import datetime
import hashlib
import json

from flask import Flask, jsonify

class Blockchain:
    def __init__(self):
        # store groups of block
        self.chain = []             # list that store block
        self.transaction = 0        # amount of money

        # genesis block
        self.create_block(nonce =  1, previous_hash = "0")
    
    # create block in blockchain's system
    def create_block(self, nonce, previous_hash):
        # store component of each block (dictionary)
        block = {
            "index": len(self.chain) + 1,
            "timestamp": str(datetime.datetime.now()),
            "nonce": nonce,
            "data": self.transaction,
            "previous_hash": previous_hash
        }

        self.chain.append(block)
        return block
    
    # current last block before adding new one
    def get_previous_block(self):
        return self.chain[-1]
    
    # encode block
    def hash(self, block):
        # transform python object(dict) -> json object
        encode_block = json.dumps(block, sort_keys = True).encode()

        # sha-256 : encode to base 16
        return hashlib.sha256(encode_block).hexdigest()

    # form of adding new blocks of transactions to a cryptocurrency's blockchain
    def proof_of_work(self, previous_nonce):
        # find nonce that cause target hash's first 4 digits to be 0000xxxxxxxxx
        new_nonce = 1           # nonce that we're trying to find
        check_proof = False     # check value of nonce to cause target match

        # solve math problems
        while check_proof is False:
            # 1 set of base 16 : block that update to blockchain must have equal hash to the examine one
            hashoperation = hashlib.sha256(str(new_nonce**2 - previous_nonce**2).encode()).hexdigest()  # same as 72
            if hashoperation[:4] == "0000":
                check_proof = True
            else:
                new_nonce += 1

        return new_nonce
    
    # examine block
    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        
        while block_index < len(chain):
            # checked block
            block = chain[block_index] 
            if block["previous_hash"] != self.hash(previous_block):
                return False

            previous_nonce = previous_block["nonce"]    # previous block's nonce
            nonce = block["nonce"]                      # checked block's nonce
            hashoperation = hashlib.sha256(str(nonce**2 - previous_nonce**2).encode()).hexdigest()      # same as 51

            if hashoperation[:4] != "0000":
                return False
            previous_block = block
            block_index += 1

        return True

# web server : if we modify server, we have to stop terminal
# Ctrl + C on terminal, then type "cls" and run again
""" Running on http://127.0.0.1:5000/ """
app = Flask(__name__)

# use blockchain
blockchain = Blockchain()

# routing -> path for client sending request to server
@app.route('/')
def hello():
    return "<h1>Hello Blockchain</h1>"

@app.route('/get_chain', methods = ["GET"])
def get_chain():
    response = {
        "chain": blockchain.chain,
        "length": len(blockchain.chain)
    }
    return jsonify(response), 200

@app.route('/mining', methods = ["GET"])
def mining_block():
    # transaction amount : เงินที่ใช้ในธุรกรรม
    amount = 1000000 
    blockchain.transaction = blockchain.transaction + amount

    # proof of work
    previous_block = blockchain.get_previous_block()
    previous_nonce = previous_block["nonce"]

    # nonce = number only used once : hashed and encrypted
    nonce = blockchain.proof_of_work(previous_nonce)

    # previous hash block
    previous_hash = blockchain.hash(previous_block)

    # update new block
    block = blockchain.create_block(nonce, previous_hash)
    response = {
        "message": "Mining block done..",
        "index": block["index"],
        "timestamp": block["timestamp"],
        "data": block["data"],
        "nonce": block["nonce"],
        "previous_hash": block["previous_hash"]
    }

    # status http code 200 = OK
    return jsonify(response), 200

@app.route('/is_valid', methods = ["GET"])
def is_valid():
    is_valid = blockchain.is_chain_valid(blockchain.chain)

    if is_valid:
        response = {"message": "Blockchain Is Valid"}
    else :
        response = {"message": "Problem Occurs, Blockchain Is Not Valid"}

    return jsonify(response), 200

# Run Server
if __name__ =="__main__":
    app.run()