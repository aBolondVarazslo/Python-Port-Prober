import socket
from datetime import datetime

# List of common ports
COMMON_PORTS = {
	21: 'FTP',
	22: 'SSH',
	23: 'Telnet',
	25: 'SMTP',
	53: 'DNS',
	80: 'HTTP',
	110: 'POP3',
	139: 'NetBIOS',
	143: 'IMAP',
	443: 'HTTPS',
	445: 'SMB',
	3306: 'MySQL',
	3389: 'RDP'
}




def scan_ports(target, ports):

	if not (target.startswith("127.") or target.startswith("192.168.") or target.startswith("10.")):
		print("[!] ERROR: This tool is for educational purposes only! Test it on a local network!")		
		return

	print(f"\n[*] Starting Scan on {target} at {datetime.now()}\n")

	# Iterate through dictionary of ports
	for port, service in COMMON_PORTS.items():
		try:
			# Create a new socket object (IPv4, TCP)
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

			# Set timeout to prevent hanging
			s.settimeout(1)

			# Try to connect to the port
			result = s.connect_ex((target, port))

			if result == 0:
				print(f"[+] Port {port} ({service}) is OPEN")
			s.close()

		except Exception as e:
			print(f"[!] ERROR Scanning Port {port}: {e}")



def main():
	target = input("Enter target IP or hostname:\n").strip()

	# Attempts to find host
	try:
		ip = socket.gethostbyname(target)

	# Error handling
	except socket.gaierror:
		print("[!] ERROR: Invalid Hostname")
		return

	open_ports = scan_ports(ip, COMMON_PORTS.keys())

if __name__ == "__main__":
	main()











