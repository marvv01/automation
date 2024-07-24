import ipaddress
def calc_network(ip_address, subnet_mask):
    try:
        interface = ip_address.IPv4Interface(f"{ip_address}/{subnet_mask}")
        #calculate network Address
        network_address = str(interface.network.network_address)
        #calculate host Address
        host_address =str(interface.ip)
        #calculate number of hosts

        #Subtract 2 for network address and broadcast address
        number_of_hosts = interface.network.num_addresses - 2

        return network_address, host_address, number_of_hosts

    except ValueError as e:
        print(f"Error: {e}")
        return None, None, None
def main():
#main function to get user input and display results
    print("Network Address ")
    print("===="
          "===="
          "=====")
    #Get user input
    ip_address=input("Enter IP address: ")
    subnet_mask=input("Enter subnet mask: ")
    #calculate network information
    network_address, host_address, number_of_hosts = calc_network(ip_address, subnet_mask)
    #Display results
    if network_address and host_address and number_of_hosts is not None:
        print("\nResults: ")
        print(f"Network Address: {network_address}")
        print(f"Host Address: {host_address}")
        print(f"number of hosts: {number_of_hosts}")

if __name__ == "__main__":
        main()