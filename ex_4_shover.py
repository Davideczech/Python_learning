'''
4. Create a show_version variable that contains the following

show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "

Remove all leading and trailing whitespace from the string.

Split the string and extract the model and serial_number from it.

Check if 'Cisco' is contained in the model string (ignore capitalization).

Check if '881' is in the model string.

Print out both the serial number and the model.
'''

show_version = "      *0        CISCO881-SEC-K9       FTX0000038X    "
show_version=show_version.strip()
print(show_version)

split_sh=show_version.split( )
model=split_sh[1]
serial_number=split_sh[2]

boolmanuf="cisco" in model.lower()
boolnumber="881" in model

print(f"Manufacturer is Cisco: {boolmanuf} and Number contains 881: {boolnumber} ")

print(f"Serial number is: {serial_number} and the model is: {model}")
