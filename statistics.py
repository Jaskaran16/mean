numbers= [1,2,3,4,5]
length = len(numbers)
sum_num = sum(numbers)
print(length,sum_num)
mean= sum_num/length
print(mean)
numbers.sort()
#if length %2 == 0:
median = numbers[length//2]
print(median)
