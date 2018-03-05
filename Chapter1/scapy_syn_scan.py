#!/usr/bin/python3.4
# -*- coding=utf-8 -*-

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
from scapy_ping_one_new import scapy_ping_one

def syn_scan_final(hostname,lport,hport):
	ping_result = scapy_ping_one(hostname)
	if ping_result[1] == 2:
		print('设备' + hostname + '不可达！！！')
	else:
		result_raw = sr(IP(dst=hostname)/
						TCP(dport=(int(lport),int(hport)),flags="S"),
						timeout = 1, 
						verbose = False)

		result_list = result_raw[0].res #类型为清单
		for i in range(len(result_list)):
			if result_list[i][1].haslayer(TCP):
				TCP_Fields = result_list[i][1].getlayer(TCP).fields
				if TCP_Fields['flags'] == 18:
					print('端口号: ' + str(TCP_Fields['sport']) + '  is Open!!!')

if __name__ == '__main__':
	host = input('请你输入扫描主机的IP地址: ')
	port_low = input('请你输入扫描端口的最低端口号: ')
	port_high = input('请你输入扫描端口的最高端口号: ')
	syn_scan_final(host,port_low,port_high)