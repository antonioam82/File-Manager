#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from colorama import init, Fore, Back, Style
import shutil
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

def show_commands():
    print(Fore.GREEN+"\n--------------------------------------------COMMANDS-------------------------------------------")
    print("cd <path>--------------------------------------------------------------Change current directory")
    print("cp <regex string> <destination path>--------------------------Copy files into a given directory")
    print("ct <regex string> <destination path>--------------------------Move files into a given directory")
    print("ls----------------------------------------------------------List all items in current directory")
    print("fl----------------------------------------------------------List all files in current directory")
    print("fld-------------------------------------------------------List all folders in current directory")
    print("sd-----------------------------------------------------------------------Show current directory")
    print("md <new folder name>-----------------------------------Create a new folder in current directory")
    print("rmd <empty folder>----------------------------------Remove an empty folder in current directory")
    print("rmt <not empty folder>---------------------------Remove a not empty folder in current directory")
    print("trs <regex string>-------------------------------------Tree search files from current directory")
    print("rs <regex string>---------------------------------------------Search files in current directory")
    print("rmf <regex string>--------------------------------------------Remove files in current directory")
    print("raf-----------------------------------------------------Remove all files from current directory")
    print("help--------------------------------------------------------------------------Show command list")
    print("q----------------------------------------------------------------------------Finish the program")
    print("cl---------------------------------------------------------------------------------Clear screen"+Fore.RESET+"\n")
    

def remove_folder(f):
    try:
        if os.path.isdir(f):
            if os.path.getsize(f) == 0:
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
                print(Fore.RED+"THE FOLDER IS NOT EMPTY (FOR NOT EMPTY FOLDERS YOU CAN USE 'rmt' COMMNAD INSTEAD)."+Fore.RESET+"\n")
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

def counter_label(n, s, fc):
    if n == 0:
        print(Fore.BLACK+Back.RED+"No match with \'{}\'.".format(s)+Fore.RESET+Back.RESET+"\n")
    else:
        if n == 1:
            print(Fore.BLACK+Back.GREEN+"\n1 ITEMS FOUND."+Fore.RESET+Back.RESET+"\n")
        else:
            print(Fore.BLACK+Back.GREEN+"\n{} ITEMS FOUND IN {} FOLDER/S.".format(n, fc)+Fore.RESET+Back.RESET+"\n")

def remove_ne_folder(f):
    global showed_dir, folder_counter
    count = 0
    num_folders = 0
    if os.path.isdir(f):
        print("")
        for root, folders, files in os.walk(f):
            for file in files:
                show_dir(root)
                count+=1
                print(Fore.RED+'{}-'.format(count)+os.path.join(root,BMP(Fore.RED+Style.DIM+file+Fore.RESET+Style.NORMAL)))
            showed_dir = False
            num_folders+=1

        folder_counter = 0

        if count > 0:
            print(Back.RED+Fore.BLACK+"\nWARNING!!"+Back.RESET+Fore.RESET)
            num = Fore.RED+str(count)+Fore.RESET
            flds = Fore.RED+str(num_folders)+Fore.RESET
            print("You are going to remove {} files and {} folders.".format(num,flds))
            c = ny(input("CONTINUE?[Y/n]: "))
            if c.upper() == "Y":
                try:
                    shutil.rmtree(f)
                    print("\nREMOVED {} FILES AND {} FOLDERS.".format(num, flds))
                except Exception as e:
                    print(Fore.RED + str(e) + Fore.RESET + "\n")
            else:
                print(Fore.GREEN+"Action Cancelled by user"+Fore.RESET+"\n")
    else:
        print(Fore.RED+"Directory not found."+Fore.RESET+"\n")


def regex_search_di(s):
    count = 0
    try:
        print("")
        for i in os.listdir():
            match_ = re.search(s, i)
            if match_:
                count+=1
                print(Fore.GREEN+'{}-'.format(count)+os.path.join(os.getcwd(),BMP(Fore.YELLOW+Style.DIM+i+Fore.RESET+Style.NORMAL)))
        counter_label(count, s, 1)
        
    except Exception as e:
        print(Fore.RED+str(e)+Fore.RESET+"\n")

def regex_search(s):
    global folder_counter, showed_dir
    count = 0
    try:
        print("")
        '''for dirpath, dirnames, files in os.walk(os.getcwd()):
            print(f'Found directory: {dirpath}')
            for file_name in files:
                print(file_name)'''
        for root, folders, files in os.walk(os.getcwd()):
            for file in files:
                match_ = re.search(s, file)
                if match_:
                    show_dir(root)
                    count+=1
                    print(Fore.GREEN+'{}-'.format(count)+os.path.join(root,BMP(Fore.YELLOW+Style.DIM+file+Fore.RESET+Style.NORMAL)))
            showed_dir = False
            
        counter_label(count, s, folder_counter)
        folder_counter = 0
                
    except Exception as e:
        print(Fore.BLACK+Back.RED+'ERROR: {} '.format(str(e))+Fore.RESET+Back.RESET+"\n")
                
def show_dir(direc):
    global showed_dir, folder_counter
    if showed_dir == False:
        print(Fore.BLUE+Back.WHITE+direc+Fore.RESET+Back.RESET)
        showed_dir = True
        folder_counter += 1

def remove_all_files():
    c_d = os.getcwd()
    counter = 0
    for i in os.listdir(c_d):
        if os.path.isfile(i):
            try:
                os.remove(i)
                counter+=1
            except Exception as e:
                print(Fore.RED+"ERROR "+Fore.RESET+str(e))
    num = Fore.RED+str(counter)+Fore.RESET
    dire = Fore.GREEN+os.getcwd()+Fore.RESET
    print("\nREMOVED {} FILE/S FROM {}\n".format(num, dire))

def files_to_remove():
    count = 0
    print("")
    for i in os.listdir():
        if os.path.isfile(i):
            count+=1
            print(Fore.RED+'{}-'.format(count)+i+Fore.RESET)
    if count > 0:
        print(Back.RED+Fore.BLACK+"\nWARNING!!"+Back.RESET+Fore.RESET)
        num = Fore.RED+str(count)+Fore.RESET
        dire = Fore.GREEN+os.getcwd()+Fore.RESET
        print("You are going to remove {} file/s from {}".format(num,dire))
        c = ny(input("CONTINUE?[Y/n]: "))
        if c.upper() == "Y":
            remove_all_files()
        else:
            print(Fore.GREEN+"Action Cancelled by user"+Fore.RESET+"\n")
    

def files_managed(s, act):
    file_list = []
    count = 0
    print("")
    for i in os.listdir():
        match = re.search(s, i)
        if match:
            count+=1
            print(Fore.RED+'{}-'.format(count)+i+Fore.RESET)
            file_list.append(i)
    if count > 0:
        print(Back.RED+Fore.BLACK+"\nWARNING!!"+Back.RESET+Fore.RESET)
        num = Fore.RED+str(count)+Fore.RESET
        dire = Fore.GREEN+os.getcwd()+Fore.RESET
        print("You are going to {} {} file/s from {}".format(act,num,dire))
        c = ny(input("CONTINUE?[Y/n]: "))
        if c.upper() == "Y":
            return file_list, count
        else:
            print(Fore.GREEN+"Action Cancelled by user"+Fore.RESET+"\n")
    else:
        print(Fore.BLACK+Back.RED+"No match with \'{}\'.".format(s)+Fore.RESET+Back.RESET+"\n")
            
def cut_or_copy(s,act,dest):
    files = files_managed(s,"move")
    count = 0
    if files:
        src = Fore.GREEN+os.getcwd()+Fore.RESET
        dst = Fore.GREEN+dest+Fore.RESET
        print("")
        if act == "cp":
            for i in files[0]:
                try:
                    shutil.copy(i,dest)
                    #print(Fore.YELLOW+"COPIED "+Fore.RESET+i+" FROM {} TO {}".format(src,dst))
                    count += 1
                except Exception as e:
                    print(Fore.RED+"ERROR "+Fore.RESET+str(e))
            print("\nCOPIED {} FILE/S FROM {}\n".format(count, src))
        else:
            for i in files[0]:
                try:
                    shutil.move(i,dest)
                    #print(Fore.YELLOW+"MOVED "+Fore.RESET+i+" FROM {} TO {}".format(src,dst))
                    count += 1
                except Exception as e:
                    print(Fore.RED+"ERROR "+Fore.RESET+str(e))
            print("\nMOVED {} FILE/S FROM {}\n".format(count, src))
   
def remove_files(s):
    files = files_managed(s,"remove")
    if files:
        print("")
        for i in files[0]:
            try:
                os.remove(i)
                print(Fore.RED+"DELETED "+Fore.RESET+i)
            except Esception as e:
                print(Fore.BLACK+Back.RED+"ERROR"+Fore.RESET+Back.RESET+str(e))
        num = Fore.RED+str(files[1])+Fore.RESET
        dire = Fore.GREEN+os.getcwd()+Fore.RESET
        print("\nREMOVED {} FILE/S FROM {}\n".format(num, dire))
            
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

def lfws():
    if len(command) >= 2:
        extrc = command.pop(0)
        string = (" ").join(command)
        if extrc == 'md':
            make_dir(string)
        elif extrc == 'cd':
            change_dir(string)
        elif extrc == 'rmd':
            remove_folder(string)
        elif extrc == 'trs':
            regex_search(string)
        elif extrc == 'rs':
            regex_search_di(string)
        elif extrc == 'rmf':
            remove_files(string)
        else:
            remove_ne_folder(string)
    else:
        print(Fore.RED+"INVALID ARGUMENT"+Fore.RESET+"\n")

def start():
    init()
    print(Back.BLUE+"\n-----------------------------------------FILE MANAGER-----------------------------------------"+Back.RESET+"\n")
    print("Current Directory: {}\n".format(os.getcwd()))

commands = ['cd','q','ls','cl','sd','fl','fld','md','rmd','raf','trs','rs','rmt','rmf','ct','cp','help']
start()
showed_dir = False
folder_counter = 0
while True:
    command = input(os.getcwd()+"\FM:\> ").split(" ")
    if command[0] in commands:
        if command[0] == 'q':
            if len(command) == 1:
                break
            else:
                print(Fore.RED+"INVALID ARGUMENT"+Fore.RESET+"\n")
        elif command[0] == 'raf':
            if len(command) == 1:
                files_to_remove()
            else:
                print(Fore.RED+"INVALID ARGUMENT"+Fore.RESET+"\n")
        elif command[0] == 'help':
            if len(command) == 1:
                show_commands()
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
        elif command[0] == 'cp' or command[0] == 'ct':
            if len(command) >= 3:
                com = command.pop(0)
                folder = command.pop()
                if os.path.isdir(folder):
                    string = (" ").join(command)
                    cut_or_copy(string,com,folder)
                else:
                    print(Fore.RED+"FOLDER NOT FOUND."+Fore.RESET+"\n")
            else:
                print(Fore.RED+"INVALID ARGUMENT"+Fore.RESET+"\n")
                
        else:
            lfws()

    else:
        print(Fore.RED+"UNKNOW COMMAND\n"+Fore.RESET)
            
