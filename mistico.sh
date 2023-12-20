#!/bin/bash
chmod +x mistico.sh
chmod +x nmapt.sh
chmod +x nmapv.sh
echo  "_____________________"
echo  "Autor: Alan73zozz"
echo  "_____________________"
echo "1. escaneo de nmap"
echo "2. versiones de puertos"
echo "3. escaneo de red"
echo "4. ataque de fuerza bruta"
echo "x. salir"
echo "__________"

read -p "Opcion " opcion
case $opcion in

1) bash nmapt.sh ;;
2) bash nmapv.sh ;;
3) bash nmapr.sh ;;
4) python3 atacb.py ;;
x) exit
esac