import time 
from playsound import playsound

def encode(text):
    mcode = {'A' : '.-' , 'B' : '-...' , 'C' : '-.-.' , 'D' : '-..' , 'E' : '.' , 'F' : '..-.' , 'G' : '--.' , 'H' : '....' , 'I' : '..' , 'J' : '.---' , 'K' : '-.-' , 'L' : '.-..' , 'M' : '--' , 'N' : '-.' , 'O' : '---' , 'P' : '.--.' , 'Q' : '--.-' , 'R' : '.-.' , 'S' : '...' , 'T' : '-' , 'U' : '..-' , 'V' : '...-' , 'W' : '.--' , 'X' : '-..-' , 'Y' : '-.--' , 'Z' : '--..' , '0' : '-----' , '1' : '.----' , '2' : '..---' , '3' : '...--' , '4' : '....-' , '5' : '.....' , '6' : '-....' , '7' : '--...' , '8' : '---..' , '9' : '----.' }
    result = ""
    for char in text :
        if(char.isalnum()):
            if(char.isalpha()):
                morse_char = mcode[char.upper()]
                result = result + morse_char + " "
            else :
                morse_char = mcode[char]
                result = result + morse_char + " "
        elif (char == " "):
            result = result + "   "
    return result        


def decode(mtext):
    mdecode = {'.-' : 'A' , '-...' : 'B' , '-.-.' : 'C' , '-..' : 'D' , '.' : 'E' , '..-.' : 'F' , '--.' : 'G' , '....' : 'H' , '..' : 'I' , '.---' : 'J' , '-.-' : 'K' , '.-..' : 'L' , '--' : 'M' , '-.' : 'N' , '---' : 'O' , '.--.' : 'P' , '--.-' : 'Q' , '.-.' : 'R' , '...' : 'S' , '-' : 'T' , '..-' : 'U' , '...-' : 'V' , '.--' : 'W' , '-..-' : 'X' , '-.--' : 'Y' , '--..' : 'Z' , '-----' : '0' , '.----' : '1' , '..---' : '2' , '...--' : '3' , '....-' : '4' , '.....' : '5' , '-....' : '6' , '--...' : '7' , '---..' : '8' , '----.' : '9' }
    ma_list = mtext.split("    ") #4 spaces 1 of char and 3 that separate word 
    result  = ""
    for word in ma_list :
        char_list = word.split(" ")
        for char in char_list :
            result = result + mdecode[char]
        result = result + " "
    return result 


def play_morse(text):
    for char in text : 
        if(char == "."):
            playsound("small_beep.mp3")
        elif(char == "-"):
            playsound("big_beep3.mp3")
        elif(char == " ") : 
            time.sleep(0.2)
        else : 
            print("invalid character ")

#we can write our code morse on a file using the code bellow 

#f = open("morse.txt",'wt')
#f.write(encode(text))
#f.close()

print("------------- Hello and Welcome -------------")
print("Choose from the list bellow : ")
print("1 - Encode plaintext to morse code and play sound ")
print("2 - Decode morse code to plaintext")
choice = input("your choice : ")
if(choice == "1"):
    text = input("give the text : ")
    print(encode(text))
    play_morse(encode(text))
elif(choice == "2"):
    text = input("give morse code with one space between characters and 4 spaces between words")
    print(decode(text))
else : 
    print("invalid input")
