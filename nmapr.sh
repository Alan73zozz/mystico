#!/bin/bash

echo "____________________________"

read -p "ingrese la red wifi: " red

echo "____________________________"

sudo nmap -sn $red/24
