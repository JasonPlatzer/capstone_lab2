nums = [2, 4, 6]
add_one = [num +1 for num in nums]
print(add_one)

numbers = [0, 3, 4, 0, 22 ,1]
non_zero = [num for num in numbers if num != 0]
print(non_zero)

classes = ['ITEC 2560', 'IBTEC 1010', 'ITEC 2905']
itec = [c for c in classes if c if 'ITEC' in c]
print(itec)

num_list = [0, 10 ,4, 0, 32]
doubled = [n * 2 for n in num_list if n != 0]
print(doubled)