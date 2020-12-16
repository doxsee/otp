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

def main() :
    option = input("Press E to Encrypt a message or D to Decrypt a message (press Q to quit at any time): ")
    if option.upper() == "Q" :
        return
    if option.upper() == "E" :
        message = input("Enter your message: ")
        if message.upper() == "Q" :
            return
        if message.upper() != "Q" :
            otpe(message)
            print("\nMessage successfully encrypted.")
            main()
    if option.upper() == "D" :
        ciphertextInFile = input("Enter the name of the file to decrypt: ")
        if os.path.isfile(ciphertextInFile) :
            otpInFile = input("Enter the otp file: ")
            if os.path.isfile(otpInFile) :
                otpd(ciphertextInFile, otpInFile)
                print("\nMessage successfully decrypted.")
                main()
            else :
                print("\nFile not found")
                main()
        else :
            print("\nFile not found.")
            main()
        if ciphertextInFile.upper() == "Q" :
            return
    return

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
        
# Checks if there is another message already generated with the same filename.

    if os.path.exists("ciphertext.txt") :
        outfile = open(("ciphertext{}.txt".format(int(time.time()))), "w")
        otpfile = open(("otp{}.txt".format(int(time.time()))), "w")
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

def otpd(ciphertextInFile, otpInFile) :
    ciphertextFile = open(ciphertextInFile, "r")
    otpFile = open(otpInFile, "r")
    
    ciphertext = ciphertextFile.readline()
    ciphertext = ciphertext.strip("[]")
    ciphertext = ciphertext.replace(" ", "")
    ciphertextList = []
    encryptedList = ciphertext.split(",")
    for element in encryptedList :
        ciphertextList.append(int(element))
    
    otp = otpFile.readline()
    otp = otp.strip("[]")
    otp = otp.replace(" ", "")
    otpList = []
    encryptedList = otp.split(",")
    for element in encryptedList :
        otpList.append(int(element))
    
    decryptedMessage = []
    for num in range(len(ciphertextList)) :
        decryptedMessage.append(ciphertextList[num] - otpList[num])
        
    message = open("message.txt", "w")
    for element in decryptedMessage :
        message.write(chr(element))
    
    message.close()
    ciphertextFile.close()
    otpFile.close()
    
    return
        
        
        
main()
