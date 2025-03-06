import requests
import json

headers = {"Content-Type": "application/json"}

def deletehook(hookurl):
    drk = requests.delete(hookurl, headers=headers)
    if drk.status_code == 204:
        print('[+] Successfully Deleted Webhook')
    else:
        print(f'[-] Failed To Delete Webhook: {drk.status_code}')
