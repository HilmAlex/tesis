import json
import os

cwd = os.getcwd()
ip_rules_path = f'{cwd}/src/data/initIPRules.json'
mac_rules_path = f'{cwd}/src/data/initMACRules.json'

def read(path):
    with open(path) as file:
        json_data = file.read()
        data = json.loads(json_data)
    
    return data

def write(path, new_data):
    with open(path, 'w') as out_file:
        json_data = json.dumps(new_data, indent=4)
        out_file.write(json_data)

def read_json(path):
    json_data = read(path)
    return json_data

def read_ip_rules():
    ip_rules = read_json(ip_rules_path)
    return ip_rules

def read_mac_rules():
    mac_rules = read_json(ip_rules_path)
    return mac_rules