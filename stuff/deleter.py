import requests
import json

headers = {"Content-Type": "application/json"}

def deletehook(hookurl):
    drk = requests.delete(hookurl, headers=headers)
    if drk.status_code == 204:
        print('[+] Successfully Deleted Webhook')
    else:
        print(f'[-] Failed To Delete Webhook: {drk.status_code}')

def deletehookmsg(hookurl, id):
    gng = requests.delete(f'{hookurl}/messages/{id}', headers=headers)
    if gng.status_code in [200, 201, 204]:
        print('[+] Deleted Message')
    else:
        print('[-] Failed To Delete Message')
