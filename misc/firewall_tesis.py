from pox.core import core
import pox.openflow.libopenflow_01 as of
import pox.lib.packet as pkt
from pox.lib.revent import *
from pox.lib.addresses import EthAddr, IPAddr
from utils.file import read_ip_rules, read_mac_rules


log = core.getLogger()

class Firewall(EventMixin):
    
    def __init__(self):
    #Comienza a escuchar a conexion
        log.info("INICIANDO FIREWALL...")
        self.listenTo(core.openflow)
        log.info("Leyendo reglas...")

        self.ip_rules = read_ip_rules()
        self.mac_rules = read_mac_rules()

        print(self.ip_rules, self.mac_rules)
        log.info("Instalando reglas, espere...")
        
    def _handle_ConnectionUp(self, event):

        log.info("Reglas instaladas :)")

        for ip_rule, mac_rule in zip(self.ip_rules, self.mac_rules):
            
            #Crea un flujo de entrada
            msg = of.ofp_flow_mod()
            
            #Bloque de MACs
            msg.match = of.ofp_match()      
            msg.match.dl_src = EthAddr(mac_rule['from'])
            msg.match.dl_dst = EthAddr(mac_rule['to'])
            event.connection.send(msg)
            
            #Bloqueo de IPs
            #En el atributo "nw_proto" puede ir 1 en lugar de pkt.ipv4.ICMP_PROTOCOL 
            msg.match = of.ofp_match(dl_type = 0x800, nw_proto = pkt.ipv4.ICMP_PROTOCOL)      
            msg.match.nw_src = IPAddr(ip_rule['from'])
            msg.match.nw_dst = IPAddr(ip_rule['to']) 
            event.connection.send(msg) 
              

def launch ():
    core.registerNew(Firewall)
