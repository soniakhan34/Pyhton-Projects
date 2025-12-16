#Random password generator , accessing length from user

import random  #inporting random module
import string #importing string module/library

print("Welcome to our Random password generator! ")


def pass_generator():
        
    length=int(input("Enter length for password generating! ")) #asking user for length
        
    #small alphabets
    abc=string.ascii_lowercase
    #upper case letter
    ABC=string.ascii_uppercase
    #digits 0-9
    digit=string.digits
    #punctuation
    symbols=string.punctuation

    #combining
    combine=abc+ABC+digit+symbols


        
    #using sample()  from random module

    list_type_password=random.sample(combine,length)

    #using join() to make it as string/password type
    password="".join(list_type_password)

    print(password)    #printing password



    pass_generator()   #keeps ask lengh for passord


pass_generator() #main function call


