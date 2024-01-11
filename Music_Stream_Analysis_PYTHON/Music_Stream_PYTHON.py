from collections import defaultdict


# MUSIC STREAMING DATA ANALYSIS

print("------------------------MUSIC STREAMING DATA ANALYSIS------------------------\n")

# -----------------------------------------------------------------------------------------------------------------------------

# Playlist Duration Calculator:
# This script defines a function to calculate the total duration of a playlist based on a given list of song durations in minutes.

def playlist_duration(song_durations):
    """
    Calculates the total duration of a playlist.

    Parameters:
    - song_durations (list): A list of song durations in minutes.

    Returns:
    - int: Total duration of the playlist in minutes.
    """
    total_duration = sum(song_durations)
    return total_duration

# Playlist song durations
playlist = [3, 4, 5, 3, 2, 4, 6, 3, 5, 4, 3, 2, 5, 4, 3, 6, 4]

# Calculate the total duration of the playlist
total_duration_result = playlist_duration(playlist)

# Display the result
print(f"The total duration of your playlist is {total_duration_result} minutes.\n")

# -----------------------------------------------------------------------------------------------------------------------------

# Most Played Song:
# This script defines a function to find the most played song in a given dictionary of songs and each time that they have been played.

def most_played_song(songs):
    """
    Calculates the most played song in a given dictionary representing the play counts for each song.

    Parameters:
    - songs (dict): Dictionary containing song names as keys and play counts as values.

    Returns:
    - str: The name of the most played song.
    """
    return max(songs, key=songs.get)

# Dictionary of song play counts
song_play_count = {
    "Shape of You": 25,
    "Despacito": 18,
    "Blinding Lights": 30,
    "Uptown Funk": 15,
    "Thinking Out Loud": 22,
    "Sicko Mode": 28,
    "Happy": 20,
    "Someone You Loved": 33,
    "Old Town Road": 16,
    "Sunflower": 27,
    "Bad Guy": 19,
    "Watermelon Sugar": 24,
    "Rockstar": 21,
    "Dance Monkey": 26,
    "Havana": 31,
    "Believer": 23,
    "Stressed Out": 29
}

# Find the most played song
most_played_result = most_played_song(song_play_count)

# Display the result
print(f"Your most played song is {most_played_result}.\n")

# --------------------------------------------------------------------------------------------------------------------------------

# Genre Analysis:
# This script defines a function to count the number of songs in each genre from a given dataset.

def song_genre_count(songs_data):
    """
    Counts the number of songs in each genre from a given dataset of songs.

    Parameters:
    - songs_data (str): File path to the dataset containing song information.

    Returns:
    - dict: Dictionary with genres as keys and counts as values.
    """
    # Initialize a defaultdict to store genre counts
    genre_count = defaultdict(int)

    # Read the dataset file
    with open(songs_data, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        # Iterate through each line (skipping the header)
        for line in lines[1:]:
            values = line.strip().split(',')

            # Extract the genre information
            genre = values[2]

            # Update the genre count
            genre_count[genre] += 1
        
    # Convert the defaultdict to a regular dictionary
    genre_count = dict(genre_count)

    # Display the genre counts
    for genre, count in genre_count.items():
        print(f"Genre: {genre}, Count: {count}")

    return genre_count

# File path to the dataset
file_path = '/Users/Brendan Smith/Desktop/Music_Stream_Analysis_PYTHON/song_data.csv'

# Call the function with the file path
song_genre_count(file_path)

# --------------------------------------------------------------------------------------------------------------------------------

# Average Song Length:
# This script defines a function to calculate the average duration of songs in a given playlist.

def average_duration(playlist):
    """
    Calculates the average duration of songs in a playlist.

    Parameters:
    - playlist (list): List of song durations in minutes.

    Returns:
    - int: Average duration of songs in the playlist.
    """
    # Calculate the sum of song durations and divide by the number of songs
    average_duration = sum(playlist) // len(playlist)
    return average_duration

# Playlist of song durations in minutes
song_durations = [3, 4, 5, 3, 2, 4, 6, 3, 5, 4, 3, 2, 5, 4, 3, 6, 4]

# Calculate the average duration of songs in the playlist
average_result = average_duration(song_durations)

# Display the result
print(f"\nThe average duration of a song in your playlist is {average_result} minutes.\n")

# ------------------------------------------------------------------------------------------------------------------------------

# Top Artists:
# This script defines a function to identify the top N artists with the most songs in a given playlist.

def playlist_top_artists(playlist, n):
    """
    Identifies the top N artists with the most songs in a given playlist.

    Parameters:
    - playlist (list): List of songs with information on artist names.
    - n (int): Number of top artists to identify.

    Returns:
    - str: A string indicating the top N artists in the playlist.
    """
    # Initialize a defaultdict to store the count of songs for each artist
    artist_count = defaultdict(int)
    
    # Count the number of songs for each artist in the playlist
    for song in playlist:
        artist = song['artist']
        artist_count[artist] += 1

    # Identify the top N artists based on song count
    top_artists = sorted(artist_count, key=artist_count.get, reverse=True)[:n]

    return f"The top {n} artists in your playlist are {', '.join(top_artists)}."

# Playlist of classic rock songs with information on title and artist
classic_rock_songs = [
    {"title": "Stairway to Heaven", "artist": "Led Zeppelin"},
    {"title": "Bohemian Rhapsody", "artist": "Queen"},
    {"title": "Hotel California", "artist": "Eagles"},
    {"title": "Comfortably Numb", "artist": "Pink Floyd"},
    {"title": "Sweet Child o' Mine", "artist": "Guns N' Roses"},
    {"title": "Dream On", "artist": "Aerosmith"},
    {"title": "Livin' on a Prayer", "artist": "Bon Jovi"},
    {"title": "Free Bird", "artist": "Lynyrd Skynyrd"},
    {"title": "Light My Fire", "artist": "The Doors"},
    {"title": "Sweet Emotion", "artist": "Aerosmith"},
    {"title": "Paint It Black", "artist": "The Rolling Stones"},
    {"title": "Born to Run", "artist": "Bruce Springsteen"},
    {"title": "More Than a Feeling", "artist": "Boston"},
    {"title": "Whole Lotta Love", "artist": "Led Zeppelin"},
    {"title": "Don't Stop Believin'", "artist": "Journey"},
]

# Find and print the top 3 artists in the classic rock playlist
top_artists_result = playlist_top_artists(classic_rock_songs, 3)
print(top_artists_result)

# ---------------------------------------------------------------------------------------------------------------------

# OUTPUT:

"""
------------------------MUSIC STREAMING DATA ANALYSIS------------------------

The total duration of your playlist is 66 minutes.

Your most played song is Someone You Loved.

Genre: Pop, Count: 12
Genre: Reggaeton, Count: 1
Genre: Funk, Count: 1
Genre: Hip Hop, Count: 2
Genre: Country, Count: 1

The average duration of a song in your playlist is 3 minutes.

The top 3 artists in your playlist are Led Zeppelin, Aerosmith, Queen.
"""