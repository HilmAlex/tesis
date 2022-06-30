import os

from pox.core import core
import pox.openflow.libopenflow_01 as of
import pox.lib.packet as pkt
from pox.lib.revent import *
from pox.lib.addresses import EthAddr, IPAddr
# from src.services.pox.pox.misc.file_utils import read_ip_rules, read_mac_rules

print(os.getcwd())


log = core.getLogger()

class Firewall(EventMixin):
    
    def __init__(self):
    #Comienza a escuchar a conexion
        log.info("INICIANDO FIREWALL...")
        self.events = set()
        self.listenTo(core.openflow)
        
    def _handle_ConnectionUp(self, event):
        self.events.add(event)

        log.info("Installing rules")

        self.ip_rules = read_ip_rules()
        self.mac_rules = read_mac_rules()

        self.add_rules(event, self.ip_rules , self.mac_rules)

        

    def add_rules(self, event, ip_rules, mac_rules):

        for ip_rule, mac_rule in zip(ip_rules, mac_rules):
            #Crea un flujo de entrada
            msg = of.ofp_flow_mod()
            print(ip_rule, mac_rule)

            self.add_ip_rule(event, msg, ip_rule['from'], ip_rule['to'])

            self.add_mac_rule(event, msg, mac_rule['from'], mac_rule['to'])

    
    def add_ip_rule(self, event, msg, ip_rule_from, ip_rule_to):
        msg.match = of.ofp_match(dl_type = 0x800, nw_proto = pkt.ipv4.ICMP_PROTOCOL)      
        msg.match.nw_src = IPAddr(ip_rule_from)
        msg.match.nw_dst = IPAddr(ip_rule_to) 
        event.connection.send(msg) 
    
    def add_mac_rule(self, event, msg, mac_rule_from, mac_rule_to):
        msg.match = of.ofp_match()      
        msg.match.dl_src = EthAddr(mac_rule_from)
        msg.match.dl_dst = EthAddr(mac_rule_to)
        event.connection.send(msg)

# class SDNFirewall(EventMixin):
    
#     def __init__(self):
#     #Comienza a escuchar a conexion
#         log.info("INICIANDO FIREWALL...")
#         self.listenTo(core.openflow)
        
#     def _handle_ConnectionUp(self, event):
#         log.info("Instalando reglas, espere...")

#         self.ip_rules = read_ip_rules()
#         self.mac_rules = read_mac_rules()

#         for mac_rule in self.mac_rules:
#             block = of.ofp_match()
#             print(mac_rule)
#             print(mac_rule['from'])
#             print(mac_rule['to'])
#             block._dl_src = EthAddr(mac_rule['from'])
#             block._dl_dst = EthAddr(mac_rule['to'])

#             flow_mod = of.ofp_flow_mod()
#             flow_mod.match = block

#             event.connection.send(flow_mod)

def launch ():
    core.registerNew(Firewall)



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



import time
import traceback

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