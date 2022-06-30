from mininet.topo import Topo
from mininet.log import info, setLogLevel
from PyQt5.QtWidgets import QApplication
import sys
from view import Window

class MiTopo(Topo):
    
    def __init__(self):
        Topo.__init__(self)
        
        info('Custom network by KEVIN :)...\n')

        h1 = self.addHost('Fb')
        h2 = self.addHost('Google')
        h3 = self.addHost('Instagram')
        h4 = self.addHost('Telegram')
        h5 = self.addHost('Twitch')
        h6 = self.addHost('Twitter')   
        h7 = self.addHost('Whatsapp')
        h8 = self.addHost('YT')

        s1 = self.addSwitch('sw1')
        s2 = self.addSwitch('sw2')
        s3 = self.addSwitch('sw3')
        s4 = self.addSwitch('sw4')
        s5 = self.addSwitch('sw5')
        s6 = self.addSwitch('sw6')
        s7 = self.addSwitch('sw7')

        self.addLink(h1, s3)
        self.addLink(h2, s3)
        self.addLink(h3, s4)
        self.addLink(h4, s4)
        self.addLink(h5, s6)
        self.addLink(h6, s6)
        self.addLink(h7, s7)
        self.addLink(h8, s7)
    
        principal = s1
        capa1 = [s2,s5]
        capa2 = [s3,s4,s6,s7]
    
        for idx,c1 in enumerate(capa1):
            self.addLink(principal,c1)
            self.addLink(c1, capa2[2*idx])
            self.addLink(c1, capa2[2*idx + 1])

topos = {'mitopo': (lambda: MiTopo())} 
   
if __name__ == '__main__':
    setLogLevel('info')
    MiTopo()
    
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    
    sys.exit(app.exec())
    
    
    
