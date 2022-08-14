# def binaryToDecimal(binary_num):
# binary_num = list(input("Input the binary number to convert: "))
# value = 0

# for i in range(len(binary_num)):
# 	digit = binary_num.pop()
	
# 	if digit == "1":
# 		value = value + pow(2,i)

# if digit == "1":
# 	print("The decimal value of the number is", value)
# else:
# 	print("Invalid input")

def octalToDecimal(value):
	chk = 0
	i = 0
	decimal_num = 0

	while value != 0:
		remainder = value % 10
		if remainder > 7:
			chk = 1
			break

		decimal_num = decimal_num + (remainder * (8 ** i))
		i = i+1
		value = int(value/10)

	if chk == 0:
		return decimal_num
	
	return None

def hexToDecimal(value):
	conversion_table = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "A": 10 , "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}

	value = value.upper()
	decimal = 0

	power = len(value) -1

	for digit in value:
		decimal += conversion_table[digit]*16**power
		power -= 1

	return decimal

