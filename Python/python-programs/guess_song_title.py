def predict_song_title(lyrics):
    lyric_count = {}
    
    # Count the occurrences of each lyric
    for lyric in lyrics:
        lyric_count[lyric] = lyric_count.get(lyric, 0) + 1
    
    max_occurrences = 0
    most_repeated_lyric = ""
    
    # Find the lyric repeated the most times
    for lyric, count in lyric_count.items():
        if count > max_occurrences:
            max_occurrences = count
            most_repeated_lyric = lyric
        elif count == max_occurrences and len(lyric) < len(most_repeated_lyric):
            most_repeated_lyric = lyric
    
    return most_repeated_lyric

# Example usage:
lyrics = [
    "Hello, world",
    "Hello, world",
    "I just got to say it, hello world",
    "Goodbye, world",
    "Goodbye, world",
    "Goodbye"
]

print(predict_song_title(lyrics))  # Output: "Hello, world"
