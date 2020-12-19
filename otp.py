#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 20:32:41 2020

@author: doxsee https://github.com/doxsee/otp
"""

## This is a OTP (One Time Pad) encryption and decryption program. This program
## generates three files. The first two are the key (otp.txt) and the encrypted
## message (ciphertext.txt). Send the key to the recipient securely (e.g. USB)
## and send the message any way you wish, just not togeather. The thrid file
## (message.txt) is the decrypted message created when using the decryption 
## function.

import os
import time


## This main function is the CLI menu, utilizing both the otpe function for 
## message encryption and the otpd function for message decryption.
 
def main() :
    option = input("(E) to Encrypt - (D) to Decrypt - (Q) to Quit): ")
    if option.upper() == "E" :
        message = input("Enter your message: ")
        otpe(message)
        print("Message successfully encrypted.")
        main()
    elif option.upper() == "D" :
        ciphertextInFile = input("Enter the name of the file to decrypt: ")
        if os.path.isfile(ciphertextInFile) :
            otpInFile = input("Enter the otp file: ")
            if os.path.isfile(otpInFile) :
                otpd(ciphertextInFile, otpInFile)
                print("Message successfully decrypted.")
                main()
            else :
                print("File not found")
                main()
        else :
            print("File not found.")
            main()
    elif option.upper() == "Q" :
        return
    else:
        print("Invalid selection.")
        main()
    return

## This encryption function takes the message and creates two unique files. One
## is the encrypted message stored as a list of UTF-8 characters in dec form,
## while the other is the randomly created key. This key is the same lenght as
## the message and is also stored as a list of UTF-8 characters in dec form.

def otpe(message) :
    otp = []
    otpNum = []
    messageNum = []
    cryptNum = []   
    
# This loop takes each character in the message and adds it to the messageNum
# list as an ASCII decimal number.

    for char in message :
        messageNum.append(ord(char))
        
# This loop fills otp with as many random numbers as there are letters in the 
# message. It also fills cryptNum with the two lists added togeather to create
# the encrypted message.

    for num in range(len(message)) :
        otp.append(os.urandom(1))
        cryptNum.append(messageNum[num] + ord(otp[num]))
        otpNum.append(ord(otp[num]))
        
# Verify ciphertext and otp filenames are unique.

    if os.path.exists("ciphertext.txt") :
        outfile = open("ciphertext{}.txt".format(int(time.time())), "w")
        otpfile = open("otp{}.txt".format(int(time.time())), "w")
        outfile.write(str(cryptNum))
        otpfile.write(str(otpNum))
    else :
        outfile = open("ciphertext.txt", "w")
        outfile.write(str(cryptNum))
        otpfile = open("otp.txt", "w")
        otpfile.write(str(otpNum))
        
    outfile.close()
    otpfile.close()
    return cryptNum

## This function takes the two files created by the otpe function and decrypts
## them into a message.txt file. Creates a unique message file name if message
## file already exists.

def otpd(ciphertextInFile, otpInFile) :

# Open the two files and store them in two corresponding variables.

    ciphertextFile = open(ciphertextInFile, "r")
    otpFile = open(otpInFile, "r")

# Reads the entire ciphertextFile and converts it into a list to be stored
# in the ciphertextList variable.
  
    ciphertext = ciphertextFile.read()
    ciphertext = ciphertext.strip("[]")
    ciphertext = ciphertext.replace(" ", "")
    ciphertextList = []
    encryptedList = ciphertext.split(",")
    for element in encryptedList :
        ciphertextList.append(int(element))
        
# Reads the entire otpFile and converts it into a list to be stored
# in the otpList variable.

    otp = otpFile.read()
    otp = otp.strip("[]")
    otp = otp.replace(" ", "")
    otpList = []
    encryptedList = otp.split(",")
    for element in encryptedList :
        otpList.append(int(element))

# Creates a list that stores the decrypted UTF-8 characters as numbers. The
# loop is the programs decryption mechanism - taking the ciphertext and
# subtracting the otp key.
   
    decryptedMessage = []
    for num in range(len(ciphertextList)) :
        decryptedMessage.append(ciphertextList[num] - otpList[num])
        
# Verify message filename is unique.

    if os.path.exists("message.txt") :
        message = open("message{}.txt".format(int(time.time())), "w")
        for element in decryptedMessage :
            message.write(chr(element))
    else:
        message = open("message.txt", "w")
        for element in decryptedMessage :
            message.write(chr(element))
            
# Close all open files

    message.close()
    ciphertextFile.close()
    otpFile.close()
    
    return

main()
