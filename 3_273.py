"""
Anuwat Khongchuai IT431 ID:273
"""
def FindAllAboutGAS(gas_type,litt,score):
	net_gas_price = 0
	gas_type_price = 0
	if gas_type == "Diesel":
		gas_type_price = 23.99
	elif gas_type == "E20":
		gas_type_price = 22.74
	elif gas_type == "E85":
		gas_type_price = 18.39
	elif gas_type == "Gasohol 91":
		gas_type_price = 24.98
	elif gas_type == "Gasohol 95":
		gas_type_price == 25.5
	else:
		gas_type_price = 0

	P = score/500
	P = P*100
	net_gas_price = (gas_type_price*litt)-P
	return net_gas_price

gas_type = input("Enter Gas Type : ")
litt = int(input("Enter litt of Gas : "))
score = int(input("Enter Gas Score : "))

net_price = FindAllAboutGAS(gas_type,litt,score)

print("Total Price : " + str(net_price))