#!/bin/sh
python3 src/view/index.py &

./pox/pox.py forwarding.l2_learning misc.myFirewall &

sudo python3 src/tree.py




