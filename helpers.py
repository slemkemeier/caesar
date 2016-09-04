def alphabet_position(letter):
    letter = letter.lower()
    return ord(letter) - 'a'

def rotate_character(char, rot):
    rot = int(rot)
    if char.isalpha() == False:
        return char
    else:
        if char.isupper():
            return(chr(((alphabet_position(char)+rot)%26)+'a').upper())
        else:
            return(chr(((alphabet_position(char)+rot)%26)+'a'))
