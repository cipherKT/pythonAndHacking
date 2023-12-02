import scapy.all as scapy

def scan(ip):
    scapy.arping(ip)
def main():
    scan("192.168.1.1/24")

if __name__ == "__main__":
    main()