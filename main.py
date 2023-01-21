# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 21:22:29 2023

@author: hex
"""

import platform
import subprocess
import ipaddress
from multiprocessing import Pool

    
def get_sub(addr, octe): #192.168.0.0 #which # of the octet
    
    lista = []
    
    for i in range(256):
        addr = addr.split('.')
        addr[octe] = str(i)
        s = "."
        addr = s.join(addr)
        lista.append(str(addr) + "/24")
    return lista
        
 
    
def ping_hosts(cidr_addr, gtwp=0):  #CIDR NOTATION / NO HOST BITS    #PING ALL(1) OR PING JUST GATEWAY ADDRESS(0)
    '''Takes network address in CIDR 
       and pings all the hosts in the subnet'''
       
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    ip_network = ipaddress.ip_network(cidr_addr)
    hosts = list(ip_network.hosts())
    
    
    var = str(subprocess.Popen(['ping', param, '1', '-w', '50', str(hosts[0])], stdout=subprocess.PIPE).communicate())
    if gtwp == 1: var = "TTL"

    if "TTL" in var:

        for i in range(len(hosts)):
           
            output = subprocess.Popen(['ping', param, '1', '-w', '50', str(hosts[i])], stdout=subprocess.PIPE).communicate()[0]
            if "TTL" in output.decode('utf-8'):
                
                print(str(hosts[i]), "is Online")
            else:
                #print(str(hosts[i]), "is Offline")
                pass
                
    else:
        print(f"")
    
 
def get_mac(host_ip):
    pass

def get_name(host_ip):
    pass
 


# 10.0. 0.0 to 10.255. 255.255, a range that provides up to 16 million unique IP addresses.
# 172.16. 0.0 to 172.31. 255.255, providing about 1 million unique IP addresses.
# 192.168. 0.0 to 192.168. 255.255, which offers about 65,000 unique IP addresses.
listb = []
for i in range(256):
     var = get_sub("192.168.0.0", 2)[i]
     listb.append(var)
    
# pool = Pool(processes=1) 
# pool.map(ping_hosts, listb)   
#    ping_hosts(var)
    
if __name__ == '__main__':
    with Pool(10) as p:
        print(p.map(ping_hosts, listb))
#print(listb)




