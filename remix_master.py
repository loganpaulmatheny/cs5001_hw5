"""
CS5001
HW5 - remix_master
Fall 2024
Logan Matheny
"""

import music
import re


def remove_punctuation(line: str) -> str:
    """
    Function: Helper function to remove any punctuation from a line within
        a song.
    Return: A copy of the line within the song w/out punctuation.
    """
    # Can be changed depending on what all punctuation you want removed
    # Simple regex and module for substituting
    return re.sub(r"[!.]", "", line)


def substitute(song: list, old_word: str, new_word: str) -> bool:
    # Takes a song, word to look for, replace the word with new word
    # List of strings
    # Should iterate through the list and use .replace
    """
    Function: Takes a song, which has been broken up into a list of phrases,
        along with a word to 'look for' and word to replace it with if it
        is found. It then modifies the song to replace the old word with
        the new AND removes all the punctuation of within the song.
    Return: Boolean based on any of the 'old word' were found within the song
    """
    # Flag
    found = False

    # Loop to check if old word is in song
    # If any old word NOT not found (found)
    # Both replace the new word and remove punctuation
    for i in range(len(song)):
        if song[i].find(old_word) != -1:
            song[i] = song[i].replace(old_word, new_word)
            song[i] = remove_punctuation(song[i])
            found = True
        continue

    # If no old words are found, print an error
    if found is False:
        print(f"Error: It seems the word {old_word} is not in " "the song, try again.")
    return found


def reverse_it(song: list) -> list:
    """
    Function: Takes in a song (list) and reverses the stanzas within it
    Return: Song with stanzas reversed and punctuation removed
    """
    # Loop through the song and remove puctuation
    # Split line of song on space
    # Reverse the list
    # Then rejoin the reversed list to create the new string
    for i in range(len(song)):
        song[i] = remove_punctuation(song[i])
        song[i] = song[i].split(" ")
        song[i].reverse()
        song[i] = " ".join(song[i])
    return song


def load_song(selection: int) -> list:
    """
    Function: Takes an int from a user representing a song they wish to play
    Return: A list with song lyrics index 0 and the title index 1
    """
    # Define the max int value the user may enter
    song_options = len(music.PLAYLIST)

    # Determine if the argument passed is within the valid range
    if selection < 0 or selection > song_options:
        return []
    else:
        # Create the song-title list
        song = []
        # Make shallow copies of the song and its title
        song.append(music.SONGS[selection - 1][:])
        song.append(music.PLAYLIST[selection - 1][:])
        return song


def playback(current_song: list):
    """
    Function: Plays the required song (prints it to console)
    Return: N/A
    """
    lyrics = current_song[0]

    for i in range(len(lyrics)):
        print(lyrics[i])


def reset_song(current_song: list) -> list:
    """
    Function: Takes the current song list as an argument and changes the
        remix back to the original.
    Return: List of original song lyrics and title.
    """
    song_number = music.PLAYLIST.index(current_song[1]) + 1
    return load_song(song_number)


def title(current_song: list):
    """
    Function: Takes in the current song and prints its title
    Return: String the title of the song
    """
    print(f"Your current song title is: {current_song[1]}")


def select_input():
    return input(
        """
            Remix-Master:
            L: Load a different song
            T: Title of current song
            S: Substitute a word
            P: Playback your song
            R: Reverse it!
            X: Reset to original song
            Q: Quit?

            Your choice: """
    ).upper()


def main():
    # print(substitute(music.SONGS[0], "new", "fart"))
    # print(music.SONGS[0])

    # print(reverse_it(music.SONGS[0]))

    # print(load_song(1))
    # print(load_song(56))

    current_song = load_song(1)

    print("Welcome to the ReMix-Master. You can remix the greatest hits")
    print("Turn up the 808's and drop the beat! Here's your remix:")
    print("")
    playback(current_song)
    selection = select_input()

    while selection != "Q":
        match selection:
            case "L":
                song_number = input("")
            case "T":
                title(current_song)
            case "S":
                old_word = input(
                    "What word do you want to replace in the existing song? "
                )
                new_word = input("What new word do you want to use for the song? ")
                substitute(current_song[0], old_word, new_word)
            case "P":
                playback(current_song)
            case "R":
                reverse_it(current_song[0])
            case "X":
                current_song = reset_song(current_song)
        selection = select_input()


if __name__ == "__main__":
    main()
