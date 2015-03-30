#!/usr/bin/env python

import fcntl
import socket
import struct

def Get_IP(ifname):
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', ifname[:15]))[20:24])

ip = Get_IP('eth0')
print(ip)
