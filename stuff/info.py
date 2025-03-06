import requests
import json

headers = {"Content-Type": "application/json"}

def hookinfo(hookurl):
    info = requests.get(hookurl, headers=headers)
    if info.status_code == 200:
        hookinf = info.json()        
        hookpfp = f"https://cdn.discordapp.com/avatars/{hookinf['id']}/{hookinf['avatar']}"
        print(f"Webhook Name: {hookinf['name']}\nWebhook ID: {hookinf['id']}\nWebhook PFP: {hookpfp}\nChannel ID: {hookinf['channel_id']}\nServer ID: {hookinf['guild_id']}\nWebhook Type: {hookinf['type']}\nWebhook Token: {hookinf['token']}")
