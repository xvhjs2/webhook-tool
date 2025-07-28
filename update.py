import requests
import os

def update(file, content):
    print(f'Updating file {file}')
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        print(f'Successfully updated {file}')
        
def recieve():
    files = ['main.py', 'update.py', 'stuff/deleter.py', 'stuff/editor.py', 'stuff/info.py', 'stuff/message.py']
    for fs in files:
        n = requests.get(f'https://github.com/xvhjs2/webhook-tool/raw/refs/heads/main/{fs}')
        update(fs, n.text)

recieve()

print('Finished updating all files')
os.system('pause')
