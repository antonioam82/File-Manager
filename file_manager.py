#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from colorama import init, Fore, Back, Style
import re

def change_dir(d):
    try:
        if os.path.isdir(d):
            os.chdir(d)
            print("Current Directory: " +Fore.GREEN+ "{}".format(os.getcwd())+Fore.RESET+"\n")
        else:
            print(Fore.RED+"Directory not found."+Fore.RESET+"\n")
            
    except Exception as e:
        print(Fore.RED + str(e) + Fore.RESET + "\n")

def ny(c):
    while c!=("Y") and c!=("N") and c!=("y") and c!=("n"):
        print(chr(7));c=input("Enter \'N/n\' or \'Y/y\': ")
    return(c)

def remove_folder(f):
    try:
        if os.path.isdir(f):
            file = Fore.RED+f+Fore.RESET
            dire = Fore.GREEN+os.getcwd()+Fore.RESET
            print("You are going to remove {} from {}".format(file, dire))
            c = ny(input("CONTINUE?[Y/n]: "))
            if c.upper() == "Y":
                os.rmdir(f)
                print("REMOVED {} FROM {}\n".format(file, dire))
            else:
                print(Fore.GREEN+"Action Cancelled by user"+Fore.RESET+"\n")
        else:
            print(Fore.RED+"FOLDER NOT FOUND."+Fore.RESET+"\n")

    except Exception as e:
        print(Fore.RED + str(e) + Fore.RESET + "\n")
        
def make_dir(d):
    try:
        os.mkdir(d)
        print("Created new directory: " + Fore.GREEN + os.path.join(os.getcwd(),d) + Fore.RESET + "\n")
    except Exception as e:
        print(Fore.RED+str(e)+Fore.RESET+"\n")

def clear():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")

def BMP(s):
    return "".join((i if ord(i) < 10000 else '\ufffd' for i in s))

def counter_label(n, s):
    if n == 0:
        print(Fore.BLACK+Back.RED+"No match with \'{}\'.".format(s)+Fore.RESET+Back.RESET+"\n")
    else:
        if n == 1:
            print(Fore.BLACK+Back.GREEN+"\n1 ITEMS FOUND."+Fore.RESET+Back.RESET+"\n")
        else:
            print(Fore.BLACK+Back.GREEN+"\n{} ITEMS FOUND.".format(n)+Fore.RESET+Back.RESET+"\n")

def regex_search_di(s):
    count = 0
    try:
        print("")
        for i in os.listdir():
            match_ = re.search(s, i)
            if match_:
                count+=1
                print(Fore.GREEN+'{}-'.format(count)+os.path.join(os.getcwd(),BMP(Fore.YELLOW+Style.DIM+i+Fore.RESET+Style.NORMAL)))
        counter_label(count, s)
        
    except Exception as e:
        print(Fore.RED+str(e)+Fore.RESET+"\n")

def regex_search(s):
    global showed_dir
    count = 0
    try:
        print("")
        for root, folders, files in os.walk(os.getcwd()):
            for file in files:
                match_ = re.search(s, file)
                if match_:
                    show_dir(root)
                    count+=1
                    print(Fore.GREEN+'{}-'.format(count)+os.path.join(root,BMP(Fore.YELLOW+Style.DIM+file+Fore.RESET+Style.NORMAL)))
            showed_dir = False

        counter_label(count, s)
        '''if count == 0:
            print(Fore.BLACK+Back.RED+"No match with \'{}\'.".format(s)+Fore.RESET+Back.RESET+"\n")
        else:
            if count == 1:
                print(Fore.BLACK+Back.GREEN+"\n1 FILES FOUND."+Fore.RESET+Back.RESET+"\n")
            else:
                print(Fore.BLACK+Back.GREEN+"\n{} FILES FOUND.".format(count)+Fore.RESET+Back.RESET+"\n")'''
                
    except Exception as e:
        print(Fore.BLACK+Back.RED+'ERROR: {} '.format(str(e))+Fore.RESET+Back.RESET+"\n")
                
def show_dir(direc):
    global showed_dir
    if showed_dir == False:
        print(Fore.BLUE+Back.WHITE+direc+Fore.RESET+Back.RESET)
        showed_dir = True        

def show_files(t):
    print("")
    counter = 1
    try:
        with os.scandir() as entries:
            for entry in entries:
                if os.path.isdir(entry) and (t == 'ls' or t == 'fld'):
                    print(BMP(Fore.GREEN + str(counter) + "- " + entry.name))#############
                    counter += 1
                
                elif os.path.isfile(entry) and (t == 'ls' or t == 'fl'):
                    print(BMP(Fore.YELLOW + str(counter) + "- " + entry.name))
                    counter += 1
        if counter > 1:
            print(Back.GREEN+Fore.BLACK+"\n{} ITEMS FOUND ".format(str(counter-1))+Back.RESET+Fore.RESET+"\n")
        else:
            print(Back.RED+Fore.BLACK+"\n{} ITEMS FOUND ".format(str(counter-1))+Back.RESET+Fore.RESET+"\n")
            
    except Exception as e:
        print(Fore.RED + str(e) + Fore.RESET + "\n")

def start():
    init()
    print(Back.BLUE+"\n---------------------------------FILE MANAGER---------------------------------"+Back.RESET+"\n")
    print("Current Directory: {}\n".format(os.getcwd()))

commands = ['cd','q','ls','cl','sd','fl','fld','md','rmd','trs','rs']
start()
showed_dir = False
while True:
    command = input(os.getcwd()+"\FM:\> ").split(" ")
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
        elif command[0] == 'ls' or command[0] == 'fl' or command[0] == 'fld':
            if len(command) == 1:
                show_files(command[0])
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
        elif command[0] == 'md':
            if len(command) >= 2:
                command.pop(0)
                nf = (" ").join(command)
                make_dir(nf)
            else:
                print(Fore.RED+"INVALID ARGUMENT"+Fore.RESET+"\n")
        elif command[0] == 'rmd':
            if len(command) >= 2:
                command.pop(0)
                rd = (" ").join(command)
                remove_folder(rd)
            else:
                print(Fore.RED+"INVALID ARGUMENT"+Fore.RESET+"\n")
        elif command[0] == 'trs':
            if len(command) >= 2:
                command.pop(0)
                string = (" ").join(command)
                regex_search(string)
            else:
                print(Fore.RED+"INVALID ARGUMENT"+Fore.RESET+"\n")
        elif command[0] == 'rs':
            if len(command) >= 2:
                command.pop(0)
                string = (" ").join(command)
                regex_search_di(string)
            else:
                print(Fore.RED+"INVALID ARGUMENT"+Fore.RESET+"\n")
    else:
        print(Fore.RED+"UNKNOW COMMAND\n"+Fore.RESET)

