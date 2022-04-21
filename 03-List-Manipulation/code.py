number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] 

remove_num = {50}# items to be removed
number_list = [num for num in number_list if num not in remove_num]
print("List after removing unwanted numbers: ", number_list)
