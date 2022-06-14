#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from colorama import init, Fore, Back, Style
import re

def change_dir(d):
    if os.path.isdir(d):
        os.chdir(d)
        print("Current Directory: {}".format(os.getcwd()))
    else:
        print("Directory not found.")

def start():
    init()
    print(Back.BLUE+"\n------------------------------FILE MANAGER------------------------------"+Back.RESET+"\n")
    print("Directorio actual: {} ".format(os.getcwd())+"\n")
        

commands = ['cd','q']
start()

while True:
    command = input("c:\> ").split(" ")
    if command[0] in commands:
        if command[0] == 'cd':
            change_dir(command[1])
        elif command[0] == 'q':
            break
    else:
        print("INVALID COMMAND")
