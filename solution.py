print("Given a list of unsorted numbers, find the numbers that have the smallest absolute difference between them.")

print("If there are multiple pairs, find them all, and output them.\n")

numbers = input("Enter a list of numbers, separated by spaces: ")

num_list = [int(x) for x in numbers.split()]
num_list.sort()
length = len(num_list)

if length == 0:
    print("No pairs possible.")
elif length == 1:
    min_diff = 0
else:
    min_diff = num_list[1] - num_list[0] 
    pair_list = [num_list[0], num_list[1]]
	for i in range(2,length):
		if (abs(num_list[i] - num_list[i-1]) < min_diff):
			pair_list.clear()
			min_diff = abs(num_list[i] - num_list[i-1])
			pair_list = [num_list[i - 1], num_list[i]]

		elif ((num_list[i] - num_list[i-1]) == min_diff):
			pair_list.append(num_list[i-1])
			pair_list.append(num_list[i])
	print(pair_list)