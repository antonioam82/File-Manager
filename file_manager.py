#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from colorama import init, Fore, Back, Style
import re

def change_dir(d):
    if os.path.isdir(d):
        os.chdir(d)
        print("Current Directory: " +Fore.GREEN+ "{}".format(os.getcwd())+Fore.RESET+"\n")
    else:
        print(Fore.RED+"Directory not found."+Fore.RESET+"\n")

def clear():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")

def show_files():
    counter = 0
    for i in os.listdir():
        counter += 1
        print(Fore.YELLOW + str(counter) + "- " + i)
    print(Back.GREEN+Fore.BLACK+"\n{} FILES FOUNDED".format(str(counter))+Back.RESET+Fore.RESET+"\n")

def start():
    init()
    print(Back.BLUE+"\n---------------------------------FILE MANAGER---------------------------------"+Back.RESET+"\n")
    print("Current dir: {} ".format(os.getcwd())+"\n")
        

commands = ['cd','q','ls','cl','sd']
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
        elif command[0] == 'cl':
            clear()
            start()
        elif command[0] == 'sd':
            print("Current Directory: " +Fore.GREEN+ "{}".format(os.getcwd())+Fore.RESET+"\n")
    else:
        print("INVALID COMMAND")
            
            
