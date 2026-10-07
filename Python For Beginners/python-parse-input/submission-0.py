from typing import List

def read_integers() -> List[int]:
    number_line=input()
    string_number_list=number_line.split(",")
    int_number_list=list()
    for n in string_number_list:
        i=int(n)
        int_number_list.append(i)
    return int_number_list
        
    

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
