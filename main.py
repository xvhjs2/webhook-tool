import requests
import time
import json
import stuff
from stuff import *
from stuff.deleter import *
from stuff.editor import *
from stuff.message import *
from stuff.info import *
import os
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)


headers = {
    "Content-Type": "application/json"
}

    
g = '''
              _                 _             
             | |               | |                    
 __  ____   _| |__   ___   ___ | | _____ _ __ 
 \ \/ /\ \ / / '_ \ / _ \ / _ \| |/ / _ \ '__|        V1.1
  >  <  \ V /| | | | (_) | (_) |   <  __/ |   
 /_/\_\  \_/ |_| |_|\___/ \___/|_|\_\___|_|   
                                              

'''
print(Fore.BLUE + g)

def enterwebhook():
    hookurl = input('[!] Webhook URL: ')
    def uiwopt():
        print(Fore.BLUE + g)
        print(Fore.WHITE + options)
        option = input('[!] Enter An Option: ')
        if option == "1":
            stuff.info.hookinfo(hookurl)
            input("[!] Press Enter")
            cls()
            uiwopt()
            
        elif option == "2":
            message = input('[!] Enter Message: ')
            sendmsg(hookurl, message)
            input('[!] Press Enter')
            cls()
            uiwopt()
            
        elif option == "3":
            message = input('[!] Enter Message: ')
            amount =  int(input('[!] Enter Message Amount: '))
            cooldown = int(input('[!] Enter Cooldown: '))
            spammsg(hookurl, message, amount, cooldown)
            input('[!] Press Enter')
            cls()
            uiwopt()

        elif option == "4":
            choice = input('[!] Change Webhook Name Or PFP?: ')
            if choice == "name":
                newname = input("[!] Enter New Webhook Name: ")
                edithookname(hookurl, newname)
                input('[!] Press Enter')
                cls()
                uiwopt()

            elif choice == "pfp":
                i = input('[!] File Path Or Image URL? (say either "url" or "path"): ')
                if i == "url":
                    img = input('[!] Enter Image URL: ')
                    edithookpfp(hookurl, img)
                    input('[!] Press Enter')
                    cls()
                    uiwopt()
                elif i == "path":
                    img = input('[!] Enter File Path (TIP: You can drag and drop the image file instead of typing the path): ')
                    edithookpfpalt(hookurl, img)
                    input('[!] Press Enter')
                    cls()
                    uiwopt()
                else:
                    print('[!] Choose an option ngia')
                    time.sleep(0.5)
                    cls()
                    uiwopt()
            else:
                print("[!] Choose one nigger. ")
                time.sleep(1)
                cls()
                uiwopt()
        
        elif option == "5":
            deletehook(hookurl)
            input('[!] Press Enter')
            cls()
            uiwopt()
            
        elif option == "6":
            enterwebhook()
            
        else:
            print('[-] Nigger Choose An Option')
            time.sleep(1)
            cls()
            uiwopt()
    def validate(hookurl):
        v = requests.get(hookurl, headers=headers)
        if v.status_code == 200:
            print('[+] Valid Webhook')
            time.sleep(1.5)
            cls()
            uiwopt()
        else:
            print('[-] Invalid Webhook')
            time.sleep(1)
            enterwebhook()
    validate(hookurl)


def ui():
    print(Fore.BLUE + g)

        
def cls():
    os.system('cls')
    
options = '''
    [1] Webhook Info
    [2] Send Message
    [3] Spam Messages
    [4] Edit Webhook
    [5] Delete Webhook
    [6] Change Webhook
'''

def tool():
    enterwebhook()
    
tool()
