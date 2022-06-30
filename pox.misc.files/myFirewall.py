import threading

from pox.core import core
import pox.openflow.libopenflow_01 as of
import pox.lib.packet as pkt
from pox.lib.revent import *
from pox.lib.addresses import EthAddr, IPAddr
from ..utils.file_modified import read_ip_rules, read_mac_rules, ip_rules_path, mac_rules_path, FileModified

log = core.getLogger()

class Firewall(EventMixin):
    
    def __init__(self):
    #Comienza a escuchar a conexion
        log.info("INICIANDO FIREWALL...")
        self.events = set()
        self.listenTo(core.openflow)
        self.demon = threading.Thread(target=self.rules_listener, args=())
        self.demon.start()
    
    def rules_listener(self):
        ip_rules_listener = FileModified(ip_rules_path, self.reset_rules)
        mac_rules_listener = FileModified(mac_rules_path, self.reset_rules)
        ip_rules_listener.start()
        mac_rules_listener.start()

    def say_hello(self):
        print('Hola')

    def _handle_ConnectionUp(self, event):
        log.info("Installing rules")
        self.read_rules()
        self.add_rules(event, self.ip_rules, self.mac_rules)
        self.events.add(event)


    def reset_rules(self):
        self.read_rules()
        for event in self.events:
            self.add_rules(event, self.ip_rules, self.mac_rules)

    def read_rules(self):
        self.ip_rules = read_ip_rules()
        self.mac_rules = read_mac_rules()

    def add_rules(self, event, ip_rules, mac_rules):
        for ip_rule in ip_rules:
            self.add_ip_rule(event, msg, ip_rule['from'], ip_rule['to'])
        
        for mac_rule in mac_rules:
            msg = of.ofp_flow_mod()
            print( mac_rule)

            self.add_mac_rule(event, msg, mac_rule['from'], mac_rule['to'])
        
    def add_ip_rule(self, event, msg, ip_rule_from, ip_rule_to):
        msg = of.ofp_flow_mod()
        msg.match = of.ofp_match(dl_type = 0x800, nw_proto = pkt.ipv4.ICMP_PROTOCOL)      
        msg.match.nw_src = IPAddr(ip_rule_from)
        msg.match.nw_dst = IPAddr(ip_rule_to) 
        event.connection.send(msg) 
    
    def delete_ip_rule(self, event, msg, ip_rule_from, ip_rule_to):
        msg = of.ofp_flow_mod(command=of.OFPFC_DELETE)
        msg.match = of.ofp_match(dl_type = 0x800, nw_proto = pkt.ipv4.ICMP_PROTOCOL)      
        msg.match.nw_src = IPAddr(ip_rule_from)
        msg.match.nw_dst = IPAddr(ip_rule_to) 
        event.connection.send(msg) 

    def add_mac_rule(self, event, msg, mac_rule_from, mac_rule_to):
        msg = of.ofp_flow_mod()
        msg.match = of.ofp_match()      
        msg.match.dl_src = EthAddr(mac_rule_from)
        msg.match.dl_dst = EthAddr(mac_rule_to)
        event.connection.send(msg)

def launch ():
    core.registerNew(Firewall)

