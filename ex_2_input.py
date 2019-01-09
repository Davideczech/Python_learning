''' 2. Prompt a user to enter in an IP address from standard input.
    Read the IP address in and break it up into its octets. Print out the octets in decimal, binary, and hex.
 '''

ip=input("Please insert and IP:")

ip=[int(i) for i in ip.split(".")]


print("\n")
print("{:^15}{:^15}{:^15}{:^15}".format("Octet1","Octet2","Octet3","Octet4"))
print("-"*80)
print("{:^15}{:^15}{:^15}{:^15}".format(*ip))
print("{:^15}{:^15}{:^15}{:^15}".format(bin(ip[0]),bin(ip[1]),bin(ip[2]),bin(ip[3])))
print("{:^15}{:^15}{:^15}{:^15}".format(hex(ip[0]),hex(ip[1]),hex(ip[2]),hex(ip[3])))

print("-"*80)
