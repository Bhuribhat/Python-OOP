class Song:
    def __init__(self, artist, song, count):
        self.artist = artist
        self.song = song
        self.count = count

    def __repr__(self):
        return f"song : {self.song}\nby : {self.artist}\nview : {self.count}\n" + "-" * 40

def main():
    """ Example """
    star    = Song("Adam Levine", "Lost star", 100000)
    thunder = Song("Imagine dragon", "Thunder", 11000)
    yours   = Song("Jason Marz", "I'm yours", 25000)
    print(star, thunder, yours, sep="\n")

    albums = list()
    number = int(input("Enter number of songs you want in album: ").strip())

    for i in range(number):
        print(f"Music # {i + 1}")
        artist = input("Please enter artist name: ").strip()
        song = input("Please enter a song name: ").strip()
        count = int(input("Please enter view number: ").strip())
        music = Song(artist, song, count)
        albums.append(music)

    albums.sort(key = lambda x: (-x.count, x.artist, x.song))
    print("sorting music in your album...")
    for music in albums:
        print(music)

if __name__ == "__main__":
    main()