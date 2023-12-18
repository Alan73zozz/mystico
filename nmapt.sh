#!/bin/bash

echo "_________"

read -p "ingrese la ip: " ip

echo "_________"

nmap -Pn $ip