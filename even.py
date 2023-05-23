#!usr/bin/env python3

number = [1, 2, 3, 4, 5, 6]
def even_number():
	even_num = []
	for angka in number:
		if angka % 2 == 1:
			even_num.append(angka)
	return even_num

even_number = even_number()
print(even_number)
