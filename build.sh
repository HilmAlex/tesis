#!/bin/sh

pyuic5 -x ./src/view/source/main_window.ui -o ./src/view/build/main_window.py

pyuic5 -x ./src/view/source/reglas_IP.ui -o ./src/view/build/IPRules.py

pyuic5 -x ./src/view/source/reglas_MAC.ui -o ./src/view/build/MACRules.py
