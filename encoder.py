
from the_code import *

#bambarabacciccocco

def userinput():
    action = input('Would you like to Encode or Decode a message? ').lower() 
    if action == 'encode':
        message = input ('Input your message: ').lower()
        encoding(message)
        more()


    elif action == 'decode':
        message = input ('Input your message: ').lower()
        decoding(message)
        more()

    else:
        print ('Wrong input. Try again')
        userinput()
 
def more():
    goagain = input('Encode/Decode more? ').lower()
    if goagain == 'yes':
        userinput()
    elif goagain == 'no':
        print('Ok. Bye')
    else:
        print ('Wrong input. Try again')
        more()

userinput()
