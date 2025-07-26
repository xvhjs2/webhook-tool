import requests
import json
from datetime import datetime

def date(id):
    de = 1420070400000
    time = ((int(id) >> 22) + de) / 1000
    date = datetime.utcfromtimestamp(time)
    return date.strftime('%Y-%m-%d %H:%M:%S') + ' ' + 'UTC Timezone' 

headers = {"Content-Type": "application/json"}

def hookinfo(hookurl):
    info = requests.get(hookurl, headers=headers)
    if info.status_code == 200:
        hookinf = info.json()
        av = {hookinf['avatar']}
        hookpfp = f"https://cdn.discordapp.com/avatars/{hookinf['id']}/{av}" if av else 'None'
        
        return f"[!] Webhook Name: {hookinf['name']}\n[!] Webhook ID: {hookinf['id']}\n[!] Webhook Creation Date: {date(hookinf['id'])}\n[!] Webhook PFP: {hookpfp if not 'None' in hookpfp else 'None'}\n[!] Channel ID: {hookinf['channel_id']}\n[!] Server ID: {hookinf['guild_id']}\n[!] Webhook Type: {hookinf['type']}\n[!] Webhook Token: {hookinf['token']}"
