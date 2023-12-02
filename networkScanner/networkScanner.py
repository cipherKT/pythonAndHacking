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
    answered= scapy.srp(arp_request_broadcast , timeout = 1 ,verbose = False)[0] #we can also use sr(send recieve) method of scapy but srp allow us to send packets with custom ether 
    # above function will return two list one with answered packets and one with unanswered packets 
    # Timeout will wait for 1s and will terminate after 1s if it doesnt get response 
    # print(answered.summary())
    # answered.show()
    # unanswered.show()
    print("IP\t\t\tMAC Address\n- - - - - - - - - - - - - - - - - - - - - - - - - ")
    for element in answered:
        print(element[1].psrc + "\t\t")
        print(element[1].hwsrc)
        print("-------------------------------------------")
    



def main():
    scan("192.168.66.1/24")

if __name__ == "__main__":
    main()
