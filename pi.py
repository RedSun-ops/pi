import time, math
a = 1
b = 1
num1 = input("number (pi, e, phi, other) : ")
if num1 == "pi":
	num2 = 3.14
if num1 == "e":
	num2 = 2.71
if num1 == "phi":
	num2 = 1.61
if num1 == "other":
	num2 = float(input("num : "))
while True:
	limit = 100
	c = a / b
	d = float(round(c, 2))
	if d == (num2 + 0.01):
		d = num2
	if d == num2:
		print(str(a) + " / " + str(b) + " = " + str(c))
		time.sleep(0)
		if a == 100:
			break
	if b == 100: # если б больше 100 то лимит увеличиваеться
		limit = 1000
	a = a + 1
	if a == limit: # если a больше лимита
		b = b + 1
		a = 0