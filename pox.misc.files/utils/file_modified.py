import json
import os
import time
import traceback

cwd = os.getcwd()
ip_rules_path = f'{cwd}/src/data/initIPRules.json'
mac_rules_path = f'{cwd}/src/data/initMACRules.json'

class FileModified():
    def __init__(self, file_path, callback):
        self.file_path = file_path
        self.callback = callback
        self.modified_on = os.path.getmtime(file_path)
    
    def start(self):
        try:
            while (True):
                time.sleep(0.5)
                modified = os.path.getmtime(self.file_path)

                if modified != self.modified_on:
                    self.modified_on = modified
                    if self.callback():
                        break
        except Exception as e:
            print(traceback.format_exc())

def read(path):
    with open(path) as file:
        json_data = file.read()
        data = json.loads(json_data)
    
    return data

def write(path, info):
    with open(path, 'w') as out_file:
        json_data = json.dumps(info, indent=4)
        out_file.write(json_data)

def read_ip_rules():
    ip_rules = read(ip_rules_path)
    return ip_rules

def read_mac_rules():
    mac_rules = read(mac_rules_path)
    return mac_rules