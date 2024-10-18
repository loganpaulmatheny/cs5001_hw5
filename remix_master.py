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
    FILL OUT LATER
    """
    found = False
    for i in range(len(song)):
        if song[i].find(old_word) != -1:
            song[i] = song[i].replace(old_word, new_word)
            song[i] = re.sub(r'[^\w\s]', '', song[i])
            found = True
        continue
    if found is False:
        print(f"Error: It seems the word {old_word} is not in "
              "the song, try again.") 
    return found

def main():
    print(substitute(music.SONGS[0], "old", "fart"))
    print(music.SONGS[0])


if __name__ == "__main__":
    main()
