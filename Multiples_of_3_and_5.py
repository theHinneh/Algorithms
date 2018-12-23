'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''
add = 0 # a variable to store values

for i in range(1000): # count from the range 0<= i < 1000
	if i % 3 == 0 or i % 5 == 0: # check if there's a remainder when the value of 'i' is divided by 3 or 5
		add += i # if true, add the value of i to add

print(add) # display the final value of add
