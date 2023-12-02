import scapy.all as scapy
import argparse
import os

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t","--target",dest = "target" , help = "Target IP / IP range")
    options = parser.parse_args()
    return options

def scan(ip):
    # scapy.arping(ip) trying to make our own arping method
    arp_request = scapy.ARP(pdst = ip) # this is the ARP object and we have given it the ip value of whole subnet of ours
    # arp_request.show()

    
    
    # scapy.ls(scapy.ARP())  this is the commnad to check for every specific term of the packet  
    
    
    
    
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff") # this is the broadcast MAC address that doesn't exist but it is virtual and when we send some data to it all client will recieve it
    # broadcast.show()
    
    
    arp_request_broadcast = broadcast/arp_request # we are appending arp request to broadcast packet
    
    
    # arp_request_broadcast.show()
    # print(arp_request_broadcast.summary())  Created arp request directed to broadcast MAC asking for IP.
    # print(broadcast.summary())
    
    
    answered = scapy.srp(arp_request_broadcast , timeout = 1 ,verbose = False)[0] #we can also use sr(send recieve) method of scapy but srp allow us to send packets with custom ether 
    
    
    # above function will return two list one with answered packets and one with unanswered packets 
    # Timeout will wait for 1s and will terminate after 1s if it doesnt get response 
    # print(answered.summary())
    # answered.show()
    # unanswered.show()
    
    
    clients_list = []
    for element in answered:
        client_dict = {"ip":element[1].psrc , "MAC":element[1].hwsrc}
        clients_list.append(client_dict)
        # print(element[1].psrc + "\t\t" + element[1].hwsrc) #element[1] means the response given by device having the target IP
        # element contains tuple like thing with 2 elemnets first is element is response sent by me and second element is response recieved
        # 2nd element is needed that's why element[1]
        # print("- - - - - - - - - - - - - - - - - - - - - - - - -")
    return clients_list


def print_result(results_list):
    print("IP\t\t\tMAC Address\n- - - - - - - - - - - - - - - - - - - - - -  ")
    for client in results_list:
        print(client["ip"]+"\t\t"+client["MAC"])
    


def main():
    os.system('clear')
    options = get_arguments()
    scan_result = scan(options.target)
    print_result(scan_result)

if __name__ == "__main__":
    main()
