def divide_numbers(a: str, b: str) -> None:
    try:
        number_int_a=int(a)
        number_int_b=int(b)
        result=number_int_a/number_int_b
        print(result)
    except Exception as error:
        print("An error occurred:",error)





# do not modify below this line
divide_numbers("10", "2")
divide_numbers("12", "0")
divide_numbers("2", "not a number")
