import requests
import json
import time

headers = {"Content-Type": "application/json"}

def sendmsg(hookurl, message):
    payload = {"content": message}
    msg = requests.post(hookurl, headers=headers, json=payload)
    if msg.status_code in [200, 201, 204]:
        print('[+] Sent Message')
    else:
        print(f'[-] Failed To Send Message: {msg.status_code}')
        
def spammsg(hookurl, message, amount, cooldown):
    for _ in range(amount):
        sendmsg(hookurl, message)
        time.sleep(cooldown)

def ghostmsg(hookurl, message):
    payload = {"content": message}
    hookurl2 = hookurl + '?wait=true'
    msg = requests.post(hookurl2, headers=headers, json=payload)
    if msg.status_code in [200, 201, 204]:
        print('[+] Sent Message')
        mj = msg.json()
        msgid = mj['id']
        md = requests.delete(f'{hookurl}/messages/{msgid}', headers=headers)
        if md.status_code in [200, 201, 204]:
            print('[+] Successfully Ghost Messaged')
        else:
            print(f'[-] Failed to delete message: {md.status_code}')
    else:
        print(f'[-] Failed To Send Message: {msg.status_code}')
