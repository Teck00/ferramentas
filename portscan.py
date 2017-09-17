#PORTSCAN feito por: Teck00
import socket
print('''
	______ ___________ _____ _____ _____   ___   _   _ 
	| ___ \  _  | ___ \_   _/  ___/  __ \ / _ \ | \ | |
	| |_/ / | | | |_/ / | | \ `--.| /  \// /_\ \|  \| |
	|  __/| | | |    /  | |  `--. \ |    |  _  || . ` |
	| |   \ \_/ / |\ \  | | /\__/ / \__/\| | | || |\  |
	\_|    \___/\_| \_| \_/ \____/ \____/\_| |_/\_| \_/
	              Feito por: Teck00                           
	              
	''')
ip = input('Digite o IP: ')
for porta in range(1, 65535):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	if s.connect_ex((ip, porta)) == 0:
		print('''
	===================
	|Porta {} [ABERTA]|
	==================='''.format(porta))
		s.close()