import subprocess
import optparse
import re


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i",'--interface',dest = "interface",help = "Interface to change its mac address")
    parser.add_option("-m","--mac",dest="new_mac",help ="New MAC address")
    (options,arguments)= parser.parse_args()
    if not options.interface:
        parser.error("[-] please specify an interface , use --help for more info")
    elif not options.new_mac:
        parser.error("[-] please specify new mac address , use --help for more info")
    return options

def change_mac(interface , new_mac):
    print(f"[+] Changing MAC address for {interface} to {new_mac}")
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    ifconfig_result = ifconfig_result.decode('utf-8')
    mac_address_pattern = r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w"
    mac_address_search_result = re.search(mac_address_pattern, ifconfig_result)
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address")


options = get_arguments()
current_mac = get_current_mac(options.interface)
print(f"Current MAC : {current_mac}")
change_mac(options.interface,options.new_mac)
current_mac = get_current_mac(options.interface)
if(current_mac == options.new_mac):
    print(f"[+] MAC address was successfully changed to {current_mac}")
else:
    print("[-] MAC address did not get changed .")