import random
import webbrowser
import urllib.parse

def play_random_song():
    # List of songs
    songs = [
        "bum bum bole",
        "pappu cant dance sala",
        "dhoom machale dhoom machale",
        "kiska hai ye tumko intezar main hoon na",
        "oh oh jane jana dhunde tujhe deewana"
    ]

    # Choose a random song from the list
    random_song = random.choice(songs)

    # Encode the song name for the YouTube search query
    encoded_song = urllib.parse.quote(random_song)

    # Create the YouTube search URL for the song
    youtube_search_url = f"https://www.youtube.com/results?search_query={encoded_song}"

    # Open the YouTube search URL in a web browser
    webbrowser.open(youtube_search_url)

# Call the function to search for a random song and play the first one that appears
play_random_song()
