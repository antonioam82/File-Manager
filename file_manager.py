#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from colorama import init, Fore, Back, Style
import re

def change_dir(d):
    if os.path.isdir(d):
        os.chdir(d)
        print(Fore.GREEN+"Current Directory: {}".format(os.getcwd())+Fore.RESET+"\n")
    else:
        print(Fore.RED+"Directory not found."+Fore.RESET+"\n")

def show_files():
    counter = 1
    for i in os.listdir():
        print(Fore.YELLOW + str(counter) + "- " + i)
        counter += 1
    print(Fore.RESET+"\n")

def start():
    init()
    print(Back.BLUE+"\n---------------------------------FILE MANAGER---------------------------------"+Back.RESET+"\n")
    print("Directorio actual: {} ".format(os.getcwd())+"\n")
        

commands = ['cd','q','ls']
start()

while True:
    command = input("C:\> ").split(" ")
    if command[0] in commands:
        if command[0] == 'cd':
            change_dir(command[1])
        elif command[0] == 'q':
            break
        elif command[0] == 'ls':
            show_files()
    else:
        print("INVALID COMMAND")
            
            
