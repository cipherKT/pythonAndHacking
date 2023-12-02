import scapy.all as scapy

def scan(ip):
    # scapy.arping(ip) trying to make our own arping method
    arp_request = scapy.ARP(pdst = ip) # this is the ARP object and we have given it the ip value of whole subnet of ours
    # arp_request.show()  
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff") # this is the broadcast MAC address that doesn't exist but it is virtual and when we send some data to it all client will recieve it
    # broadcast.show()
    arp_request_broadcast = broadcast/arp_request # we are appending arp request to broadcast packet
    # arp_request_broadcast.show()
    # print(arp_request_broadcast.summary())  Created arp request directed to broadcast MAC asking for IP.
    # print(broadcast.summary())
def main():
    scan("192.168.1.1/24")

if __name__ == "__main__":
    main()