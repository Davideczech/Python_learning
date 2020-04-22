number = int(input("Give me the number!"))
div_number = range(2,number+1)
list=[]

for number_div in div_number:

    if number % number_div == 0:
        list.append(number_div)

print("List of divisors is:",list)
