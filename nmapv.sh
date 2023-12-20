#!/bin/bash

echo "_________"

read -p "ingrese la ip: " ip
read -p "ingrese los puertos: " pu

echo "_________"

nmap -sV -p $pu  $ip -Pn