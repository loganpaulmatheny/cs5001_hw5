import remix_master

def main(): 
    song = ['go on now go walk out the door', 'just turn around now', "cause you're not welcome anymore", "weren't you the one who tried to hurt me with goodbye", "you think i'd crumble", "you think i'd lay down and die", 'oh no not i i will thrive', "oh as long as i know how to love i know i'll stay alive", "i've got all my life to live", "and i've got all my love to give and i'll thrive", 'i will survive hey hey']
    
    print(f"Before: {song}")
    print("=====AFTER=====")
    print(remix_master.substitute(song, "survive", "thrive"))

if __name__ == "__main__":
    main()
