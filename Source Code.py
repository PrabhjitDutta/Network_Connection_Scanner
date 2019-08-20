import subprocess
import socket
import time
import re
from threading import Thread


class PingThread(Thread):
	def __init__(self, ip):
		Thread.__init__(self)
		self.ip = ip


	def run(self):
		try:
			subprocess.check_output(['ping', self.ip], timeout=9)
		except:
			pass


def ipScanner():
	ip_list = socket.gethostbyname_ex(socket.gethostname())[2]

	for ip in ip_list:
		ip = ip.split('.')
		ip = ip[0] + '.' + ip[1] + '.' + ip[2] + '.'

		print("Scanning for Devices...\n\n")
		
		for i in range(1, 255):
			ping_ip = ip + str(i)
			newthread = PingThread(ping_ip)
			newthread.start()

	time.sleep(10)
	result = str(subprocess.check_output(['arp', '-a']))
	result = result.split()

	regex = re.compile(r"(19[2-9]\.[\.0-9]*)|(2[0-2][0-3]\.[\.0-9]*)")

	result = list(filter(regex.search, result))
	return result


def main():
	ip = "127.0.0.1"

	while True:
		count = 1

		ip_list = ipScanner()
		for i in ip_list:
			print(f"{count}. {i}")
			count+=1

		z = input("\nEnter R to Rescan: ")
		if z == 'R':
			continue
		else:
			break


if __name__ == '__main__':
	main()