from helpers import alphabet_position, rotate_character
from sys import argv
import sys

def encrypt(text, rot):
    answer = ""
    for char in text:
        answer += rotate_character(char, rot)
    return answer

def validation(argv):
    if len(argv) < 2:
        return False
    elif not argv[1].isdigit():
        return False
    else:
        return True


#if validation(argv) == False:
#    print("sorry")
#    sys.exit()

#text = input("Type a message:\n")
#print(encrypt(text, argv[1]))
