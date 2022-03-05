import string
import sys
import art
from termcolor import colored
alphabet_string = string.ascii_lowercase
alphabet_list = list(alphabet_string)
alphabet_list.append(' ')
alphabet_list = alphabet_list * 2

def Main():
    should_end = False    
    while not should_end : 
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n") 
        invalid(direction)  
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        shift = shift % 26
        caesar(text,shift,direction)
        
        restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
        if restart == "no":
            should_end = True
            print("Goodbye")
    
    
def caesar(Text,shift,dirextion):
    
    caesar_text = ''
    if dirextion == 'decode':
        shift *= -1
        
    for letter in Text:
        if letter in alphabet_list:
            postion = alphabet_list.index(letter)
            new_postion = postion + shift      
            caesar_text += alphabet_list[new_postion]
        else:
           caesar_text += letter
            
    print(f"The {dirextion}d Text is {colored(caesar_text,'green')}")

    
def invalid(direction):
    if direction != 'encode' and direction!= 'decode':
        print(colored('Please Enter a valid operation','red'))
        sys. exit()         

if __name__ == '__main__':
    print(art.logo)
    Main()