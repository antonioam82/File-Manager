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
    counter = 1
    with os.scandir() as entries:
        for entry in entries:
            if os.path.isdir(entry):
                print(Fore.GREEN + str(counter) + "- " + entry.name)
            else:
                print(Fore.YELLOW + str(counter) + "- " + entry.name)
            counter += 1
    print(Back.GREEN+Fore.BLACK+"\n{} ITEMS FOUNDED".format(str(counter-1))+Back.RESET+Fore.RESET+"\n")    
    '''for i in os.listdir():
        counter += 1
        print(Fore.YELLOW + str(counter) + "- " + i)
    print(Back.GREEN+Fore.BLACK+"\n{} FILES FOUNDED".format(str(counter))+Back.RESET+Fore.RESET+"\n")'''

def start():
    init()
    print(Back.BLUE+"\n---------------------------------FILE MANAGER---------------------------------"+Back.RESET+"\n")
    #print("Current Directory: " +Fore.GREEN+ "{}".format(os.getcwd())+Fore.RESET+"\n")
    print("Current Directory: {}\n".format(os.getcwd()))

commands = ['cd','q','ls','cl','sd']
start()

while True:
    command = input("FM:\> ").split(" ")
    if command[0] in commands:
        if command[0] == 'cd':
            if len(command) >= 2:
                command.pop(0)
                direc = (" ").join(command)
                change_dir(direc)
            else:
                print(Fore.RED+"INVALID ARGUMENT"+Fore.RESET+"\n")
        elif command[0] == 'q':
            if len(command) == 1:
                break
            else:
                print(Fore.RED+"INVALID ARGUMENT"+Fore.RESET+"\n")
        elif command[0] == 'ls':
            if len(command) == 1:############################################3
                show_files()
            else:
                print(Fore.RED+"INVALID ARGUMENT"+Fore.RESET+"\n")
        elif command[0] == 'cl':
            if len(command) == 1:
                clear()
                start()
            else:
                print(Fore.RED+"INVALID ARGUMENT"+Fore.RESET+"\n")     
        elif command[0] == 'sd':
            if len(command) == 1:
                print("Current Directory: " +Fore.GREEN+ "{}".format(os.getcwd())+Fore.RESET+"\n")
            else:
                print(Fore.RED+"INVALID ARGUMENT"+Fore.RESET+"\n") 
    else:
        print(Fore.RED+"INVALID COMMAND\n"+Fore.RESET)            
