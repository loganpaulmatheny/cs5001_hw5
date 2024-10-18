"""
CS5001
HW5 - remix_master
Fall 2024
Logan Matheny
"""

import music
import re


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
            song[i] = re.sub(r"[^\w\s]", "", song[i])
            found = True
        continue

    # If no old words are found, print an error
    if found is False:
        print(f"Error: It seems the word {old_word} is 
              not in " "the song, try again.")
    return found


def main():
    # print(substitute(music.SONGS[0], "new", "fart"))
    # print(music.SONGS[0])


if __name__ == "__main__":
    main()
