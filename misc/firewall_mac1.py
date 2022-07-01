from pox.core import core
import pox.openflow.libopenflow_01 as of
import pox.lib.packet as pkt
from pox.lib.revent import *
from pox.lib.util import dpidToStr
from pox.lib.addresses import EthAddr, IPAddr

log = core.getLogger()

class Firewall(EventMixin):
    
    def __init__(self):
    #Comienza a escuchar a conexion
        self.listenTo(core.openflow)
        self.reglas = [["10.0.0.1","10.0.0.3"],["10.0.0.3","10.0.0.2"]]
        log.info("Leyendo reglas...")
        log.info("Instalando reglas, espere...")
        
    def _handle_ConnectionUp(self, event):
        log.info("Reglas instaladas :)")
        #Lee cada regla
        for regla in self.reglas:
            #Bloque de MACs
            #Enviar un flujo de entrada
           """
            msg = of.ofp_flow_mod()
            msg.match = of.ofp_match()
            msg.match.dl_src = EthAddr(regla[0])
            msg.match.dl_dst = EthAddr(regla[1])
            event.connection.send(msg)
           """
           
            #Bloqueo de IPs
            #Enviar un flujo de entrada
            msg = of.ofp_flow_mod()
            #En el atributo "nw_proto" puede ir 1 en lugar de pkt.ipv4.ICMP_PROTOCOL
            msg.match = of.ofp_match(dl_type = 0x800, nw_proto = pkt.ipv4.ICMP_PROTOCOL) 
            msg.match.nw_src = IPAddr(regla[0])
            msg.match.nw_dst = IPAddr(regla[1])
            event.connection.send(msg)
           
           
    log.info("INICIANDO FIREWALL...")

def launch ():
   
    core.registerNew(Firewall)
