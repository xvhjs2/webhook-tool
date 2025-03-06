import requests
import json
import time

headers = {"Content-Type": "application/json"}

def sendmsg(hookurl, message):
    payload = {"content": message}
    msg = requests.post(hookurl, headers=headers, json=payload)
    if msg.status_code == 204:
        print('[+] Sent Message')
    else:
        print(f'[-] Failed To Send Message: {msg.status_code}')
        
def spammsg(hookurl, message, amount, cooldown):
    for _ in range(amount):
        sendmsg(hookurl, message)
        time.sleep(cooldown)
