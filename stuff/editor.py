import requests
import json
import os
import base64

headers = {"Content-Type": "application/json"}

def edithookname(hookurl, newname):
    payload = {"name": newname}
    geo = requests.patch(hookurl, headers=headers, json=payload)
    if geo.status_code == 200:
        print('[+] Successfully Changed Webhook Name')
    else: 
        print(f'[-] Failed To Change Webhook Name: {geo.status_code}')

        
def edithookpfp(hookurl, img):
    mm = requests.get(img)
    if mm.status_code == 200:
        print('[+] Fetched Image')
        gkk = base64.b64encode(mm.content).decode('utf-8')
    else:
        print('[-] Failed To Fetch Image')

    payload = {"avatar": f"data:image/png;base64,{gkk}"}    
    rge = requests.patch(hookurl, headers=headers, json=payload)
    if rge.status_code == 200:
        print('[+] Changed Webhook PFP')
    else:
        print('[-] Failed To Change Webhook PFP')
        
def edithookpfpalt(hookurl, img):
    with open(img, "rb") as george:
        floyd = base64.b64encode(george.read()).decode("utf-8")
    payload = {"avatar": f"data:image/png;base64,{floyd}"}
    flo = requests.patch(hookurl, headers=headers, json=payload)
    if flo.status_code == 200:
        print('[+] Changed Webhook PFP')
    else:
        print('[-] Failed To Change Webhook PFP')
        
def edithookmsg(hookurl, msg, id):
    payload = {'content': msg}
    gng = requests.patch(f'{hookurl}/messages/{id}', json=payload, headers=headers)
    if gng.status_code == 200:
        print('[+] Edited Message')
    else:
        print('[-] Failed To Edit Message')
