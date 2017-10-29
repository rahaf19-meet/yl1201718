a = [1,1,2,3,5,8,13,21,34,55,89]
list1=[]
user=input("choose a number")
for number in a:
	if number < 5:
		list1.append(number)
		print(number)
print(list1)