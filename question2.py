import random
num_list = []
rand_list=[]
#taking the array input
limit = int(input("Enter the amount of numbers you want in your array:- "))
for i in range(limit):
    number = int(input("Enter the number:- "))
    num_list.append(number)
print("Fetching your swapped array..")
print(num_list)
#creating random array
for n in range(len(num_list)):
    rand_num = random.randint(0,100000000000)
    if len(rand_list) != num_list:
        rand_list.append(rand_num)
#printing random array
print("your old array was.. ",num_list)
print("your new array is...",rand_list)