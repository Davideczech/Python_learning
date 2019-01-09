'''
3.   Create three different variables the first variable should use all lower case characters with underscore ( _ ) as the word separator.
The second variable should use all upper case characters with underscore as the word separator.
The third variable should use numbers, letters, and underscore, but still be a valid variable Python variable name.

Make all three variables be strings that refer to IPv6 addresses.

Use the from future technique so that any string literals in Python2 are unicode.

compare if variable1 equals variable2
compare if variable1 is not equal to variable3

'''

ip_addr="10.0.0.1"
IP_ADDR="11.0.0.1"
ip_addr_2="12.0.0.0"

stat=ip_addr==IP_ADDR
stat1=ip_addr!=IP_ADDR

print(f"{stat} and {stat1}")
