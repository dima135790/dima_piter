numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
place=4
sum_numbers=sum(numbers[0:place]) + sum(numbers[place+1:])
calculation=len(numbers)
arithmetic_mean=sum_numbers/calculation
numbers[place] = arithmetic_mean
print("Измененный список:",numbers)
