import discord
import random
import asyncio
from replit import db
# from keep_alive import keep_alive

# variable
TOKEN = "OTI3OTMzODI4MjQzMjgzOTk4.YdRbuA.TQWcdNMFCLrmaCjYEHR-ihOWnow"

HELP = """```
ก็มี
$guess        - เกมทายคำค่ดดดดดดดดดดดหนุก
$send         - ส่งข้อความเข้าไปที่ channel
                &send {text_channel} {your_text}
$play         - เล่นเพลงในยูทูป
                &play {song_name}
$responding   - เปิดปิดการตอบโต้บอท
                $responding {true/false}
$list         - เอาไว้ดูคำว่ามีไรมั่ง
$add          - เอาไว้เพิ่มคำ 
                $add {คำที่อยากเพิ่ม}
$del          - เอาไว้ลบคำ  
                $del {ตำแหน่งคำที่อยากลบ}
$help         - เอาไว้ดูคำสั่งบอท มักขึ้นต้นด้วย $ อะ ```"""""

words = ['ว่าไง', 'มา', 'เหงา', 'หิว', 'ง่วง', 'โหล', 'เอาเลย', 'ตู่', 'ดี']

interact = ['ไอ่อ้วน', 'โอ้ววว', 'ไงเงา', 'ฝันดีน้า', 'พ่อง', 'เยลโล่ว', 'เรื่องมรึ๊ง']

# initial data to replit's database
if "interact" not in db.keys():
    db["interact"] = interact

if "responding" not in db.keys():
    db["responding"] = True

# function to update word in database
def add_words(new_word):
    if "interact" in db.keys():
        interact = db["interact"]
        interact.append(new_word)
        db["interact"] = interact
    else:
        db["interact"] = [new_word]
    
def delete_word(index):
    interact = db["interact"]
    if len(interact) > index:
        del interact[index]
        db["interact"] = interact

# Class Client
class MyClient(discord.Client):

    # introduce yourself
    async def on_ready(self):
        print('We have logged in as {0.user}'.format(client))
        await client.wait_until_ready()

    # react to word and command
    async def on_message(self, message):
        global interact
        msg = message.content

        # not reply to itself
        if message.author == client.user:
            return

        # responding
        if db["responding"]:
            option = interact
            if "interact" in db.keys():
                option = option + list(db["interact"])

        if any(word in msg for word in words):
            await message.channel.send(random.choice(option))
    
        # Sonteen Word
        if msg.lower().startswith('หวัดดี'):
            await message.reply('ดีงับ', mention_author=True)

        if msg.startswith('ไป'):
            await message.reply('ไกปู', mention_author=True)

        if msg.startswith('สีเหลือง'):
            await message.reply('เยลโล่ว!', mention_author=True)
        
        if msg.lower().startswith('ma'):
            await message.reply('ลุยยยยยยย', mention_author=True)

        if msg.lower().startswith('ฝันดี'):
            await message.reply('เรื่องมึงดิ', mention_author=True)

        if msg.lower().startswith('เนอะ'):
            await message.reply('อื้อ', mention_author=True)
        
        if msg.lower().startswith('โหด'):
            await message.reply('เรื่องกู', mention_author=True)

        if msg.lower().startswith('ดุ'):
            await message.reply('จิงเบ๋อ', mention_author=True)   

        if msg.startswith('กาย'):
            await message.channel.send('อ้วนจัง')

        if msg.startswith('จิง'):
            await message.channel.send('ฮ้อยย้าา')

        # guessing game
        if msg.startswith('$guess'):
            await message.channel.send('ทายเลขใน 1 ถึง 10 ซิ')

        def is_correct(m):
            return m.author == message.author and m.content.isdigit()

        answer = random.randint(1, 10)

        try:
            guess = await self.wait_for('message', check=is_correct, timeout=5.0)
        except asyncio.TimeoutError:
            return await message.channel.send('ช้าเกิ้นสู เฉลยแม่ม {}.'.format(answer))

        if int(guess.content) == answer:
            await message.channel.send('แม่นน!')
        else:
            await message.channel.send('โง่เกิ้น ตอบ {} โว้ยย'.format(answer))

        # anonymus texting command
        if msg.startswith('$send'):
            channel = msg.split(" ", 2)[1]
            text = msg.split(" ", 2)[2]
        if (channel == "general"):
            general_channel = client.get_channel(694382265081266280)
            await general_channel.send(text)
        elif (channel == "music"):
            music_channel = client.get_channel(791315320648368142)
            await music_channel.send(text)
        elif (channel == "study-room"):
            study_room_channel = client.get_channel(808174559529926666)
            await study_room_channel.send(text)
        elif (channel == "gaming"):
            gaming_chanel = client.get_channel(809839995287633950)
            await gaming_chanel.send(text)
        else:
            long_bot_channel = client.get_channel(928269670635671653)  # test
            await long_bot_channel.send(text)

        # playing pancake music
        if msg.startswith('$play'):
            song = msg.split(" ", 1)[1]
            music_channel = client.get_channel(791315320648368142)
            await music_channel.send("p!play " + song)

        # add new words
        if msg.startswith('$add'):
            new_word = msg.split("$add", 1)[1]
            add_words(new_word)
            await message.channel.send("เพิ่มละจ้า")

        # delete word in interact
        if msg.startswith("$del"):
            interact = []
        if "interact" in db.keys():
            index = int(msg.split("$del", 1)[1])
            delete_word(index)
            interact = list(db["interact"])
            list_of_word = ", ".join(interact)
            await message.channel.send("`" + list_of_word + "`")
        else:
            await message.channel.send("ว่างแย้วครับพี่")

        # list of word
        if msg.startswith('$list'):
            interact = []
        if "interact" in db.keys():
            interact = list(db["interact"])
            list_of_word = ", ".join(interact)
            await message.channel.send("`" + list_of_word + "`")
        else:
            await message.channel.send("ว่างครับพี่")

        # responding command
        if msg.startswith("$responding"):
            value = msg.split("$responding ", 1)[1]

            if value.lower() == "true":
                db["responding"] = True
                await message.channel.send("ออนไลน์เพื่อเทอ 24 ชม")
            else:
                db["responding"] = False
                await message.channel.send("ไปละ งอน")

        # help function
        if msg.startswith('$help'):
            await message.channel.send(HELP)

client = MyClient()
# keep_alive()
client.run(TOKEN)