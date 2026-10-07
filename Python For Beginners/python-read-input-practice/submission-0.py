def add_two_numbers() -> int:
    numbers=input()
    number_list=numbers.split(",")
    sum=0
    for i in number_list:
        number=int(i)
        sum+=number
    return sum

    



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
