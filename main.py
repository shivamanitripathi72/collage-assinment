from sympy import isprime

a = int(input("enter the number to perform operation:- "))
match a:
    case 1:
        operator = input("""enter the operator to perform operation
       ' +,-,*,/,^,%,>,<,<=,>=,='  :-  
        """)
        b = int(input("enter the first number  A :- "))
        c = int(input("enter the second number B :- "))
        if operator == "+":
            print(b + c)
        elif operator == "-":
            print(b - c)
        elif operator == "*":
            print(b * c)
        elif operator == "/":
            print(b / c)
        elif operator == "^":
            print(b ** c)
        elif operator == "%":
            print(b % c)
        elif operator == ">":
            print(b > c)
        elif operator == "<":
            print(b < c)
        elif operator == "<=":
            print(b <= c)
        elif operator == "=":
            print(b == c)
        elif operator == ">=":
            print(b >= c)
        else:
            print("enter the operator to perform operation:- which are invalid input")
    case 2:
        operations = input("""enter the number to perform operation
        1:- print number 1 to 100,
        2:- print even number
        3:- print odd number
        4:-  print prime number
        5:- print square pattern
        6:- print triangle pattern of star
        7:- print reverse triangle star 
        """)
        if operations == "1":
            for i in range(1,100+1):
                print(i,end=" ")
        elif operations == "2":
            number = int(input("enter the number print upto even number:- "))
            for i in range(2,number+1,2):
                print(i,end=" ")
        elif operations == "3":
            number = int(input("enter the number for print odd number:-"))
            for i in range(1,number+1,2):
                print(i,end=" ")
        elif operations == "4":
            number = int(input("enter the number for print prime number:-"))
            for i in range(1,number+1):
                if isprime(i):
                    print(i,end=" ")
        elif operations == "5":
            for i in range(1,5):
                print("*********")
        elif operations == "6":
            for i in range(1,8):
                for j in range(1,i):
                    print("*",end=" ")
                print()
        elif operations == "7":
            for i in range(8,0,-1):
                for j in range(1,i+1):
                    print("*",end=" ")
                print()
        else:
            print("invalid input")
    case 3:
        operations = input("""enter the number to perform operation
        1:- check even number
        2:- check odd number
        3:- check prime number
        4:- print tabel
        Use of bitwise operators
            5:- Bitwise operators and (&)
            6:- Bitwise operators or  (|)
            7:- Bitwise operators xor (^)
            8:- Bitwise operators not (~)
            9:- Left shift(<<)
            10:- Right shift(>>)
                                :-  
        """)
        if operations == "1":
            number = int(input("enter the number to check even number:-"))
            if number % 2 == 0:
                print("This is even number:- ",number)
        elif operations == "2":
            number = int(input("enter the number to check odd number:-"))
            if number % 2 != 0:
                print("This is odd number:- ",number)
        elif operations == "3":
            number = int(input("enter the number to check prime number:-"))
            if isprime(number):
                print("This is prime number:- ",number)
        elif operations == "4":
            number = int(input("enter the number to print tabel:- "))
            for i in range(1,10+1):
                print(f"{number} * {i} = {i*number}")
        elif operations == "5":
            number_1 = int(input("enter the first number:-"))
            number_2 = int(input("enter the second number:-"))
            print(number_1 & number_2)
        elif operations == "6":
            number_1 = int(input("enter the first number:-"))
            number_2 = int(input("enter the second number:-"))
            print(number_1 | number_2)
        elif operations == "7":
            number_1 = int(input("enter the first number:-"))
            number_2 = int(input("enter the second number:-"))
            print(number_1 ^ number_2)
        elif operations == "8":
            number_1 = int(input("enter the first number:-"))
            number_2 = int(input("enter the second number:-"))
            print(~number_1 , ~ number_2)
        elif operations == "9":
            number_1 = int(input("enter the first number:-"))
            number_2 = int(input("enter the second number:-"))
            print(number_1 << number_2)
        elif operations == "10":
            number_1 = int(input("enter the first number:-"))
            number_2 = int(input("enter the second number:-"))
            print(number_1 >> number_2)
        else:
            print("invalid input")
    case 4:
        operations = input("""enter the number to perform operation
        1:-    AND operator use :-
        2 :-   OR operator use :-
        3 :-   NOT :- operator use :-
        """)
        if operations == "1":
            number_1 = int(input("enter the first number:-"))
            number_2 = int(input("enter the second number:-"))
            if (number_1 > number_2) and (number_1 != number_2):
                print(True)
            else:
                print("False")
        elif operations == "2":
            number_1 = int(input("enter the first number:-"))
            number_2 = int(input("enter the second number:-"))
            if (number_1 > number_2) or (number_1 < number_2):
                print(True)
            else:
                print("False")
        elif operations == "3":
            number_1 = int(input("enter the first number:-"))
            number_2 = int(input("enter the second number:-"))
            if (number_1 > number_2) or not (number_1 != number_2):
                print(True)
            else:
                print("False")
        else:
            print("invalid operation")
    case 5:
        operations = input("""enter the number to perform operation
        1:- check list or not
        2:- check tuple or not
        3:- check dictionary or not
        4:- check set or not 
        5:- check integer or not
        6:- check float or not
        7:- check boolean or not
        """)
        if operations == "1":
            a = [1,2,3,4,5,6]
            print(a,type(a))
        elif operations == "2":
            a = (1,2,3,4,5,6)
            print(a,type(a))
        elif operations == "3":
            a = {
                "name": "shiva mani tripathi",
                "age": 18
            }
            print(a,type(a))
        elif operations == "4":
            a = {1,2,3,4,5,6,7,8,9}
            print(a,type(a))
        elif operations == "5":
            a = 4
            print(a,type(a))
        elif operations == "6":
            a = 4.0
            print(a,type(a))
        elif operations == "7":
            a = True
            print(a,type(a))
        else:
            print("invalid operation")
    case 6:
        operations = input("""enter the number to perform operation
        1:-  lower case convert into upper case
        2:-  upper case convert into lower case
        3:-  isupper check value upper are not
        4:-  islower check value lower are not
        5:-  isdigit check value digit are not
        6:-  isalpha check value alpha are not
        7:-  isalnum check value alnum are not
        8:-  isspace check value space are not
        9:-  isdecimal check value decimal are not
        10:- isnumeric check value numeric are not 
                                                :- 
        """)
        if operations == "1":
            a = input("enter the text to convert in upper case:- ")
            print(a.upper())
        elif operations == "2":
            a = input("enter the text to convert in lower case:- ")
            print(a.lower())
        elif operations == "3":
            a = input("enter the text to check text true or false:- ")
            print(a.isupper())
        elif operations == "4":
            a = input("enter the text to check text true or false:- ")
            print(a.islower())
        elif operations == "5":
            a = input("enter the number to check text true or false:- ")
            print(a.isdigit())
        elif operations == "6":
            a = input("enter the text to check text true or false:- ")
            print(a.isalpha())
        elif operations == "7":
            a = input("""enter the text and number '(alnum)'
             to check text true or false:- """)
            print(a.isalnum())
        elif operations == "8":
            a = input("""enter the text to check space in 
            or not in between in text true or false:- """)
            print(a.isspace())
        elif operations == "9":
            a = input("""enter the number to check value decimal 
            are not print in the form of TRUE or FALSE:- """)
            print(a.isdecimal())
        elif operations == "10":
            a = input("""enter the number to check value 
            numric are not print TRUE or FALSE:- """)
            print(a.isnumeric())
        else:
            print("invalid operation")
    case 7:
        operations = input("""enter the number to perform operation
        1:- print perimeter of square
        2:- print area of square
        3:- print perimeter of rectangle
        4:- print area of rectangle
        5:- print perimeter of triangle
        6:- print area of triangle
        7:- print semi-perimeter of triangle
        8:- print volume of cube
        9:- print Total surface area of cube
        :-  
        """)
        if operations == "1":
            number = int(input("enter the number for print square of perimeter:- "))
            square = number * 4
            print(square)
        elif operations == "2":
            number = int(input("enter the number for print square of Area:- "))
            square = number ** 2
            print(square)
        elif operations == "3":
            length = int(input("enter the length:- "))
            width = int(input("enter the width:- "))
            rectangle_perimeter = (length + width) * 2
            print(rectangle_perimeter)
        elif operations == "4":
            length = int(input("enter the length:- "))
            width = int(input("enter the width:- "))
            area_of_rectangle = length * width
            print(area_of_rectangle)
        elif operations == "6":
            base = int(input("enter the base:- "))
            height = int(input("enter the height:- "))
            area_of_triangle = 0.5 * base * height
            print(area_of_triangle)
        elif operations == "5":
            a = int(input("enter the number:- "))
            b = int(input("enter the number:- "))
            c = int(input("enter the number:- "))
            perimeter_of_triangle = a + b + c
        elif operations == "7":
            a = int(input("enter the number:- "))
            b = int(input("enter the number:- "))
            c = int(input("enter the number:- "))
            semi_perimeter_of_triangle = (a + b + c) / 2
            print(semi_perimeter_of_triangle)
        elif operations == "8":
            number = int(input("enter the number:- "))
            cube_volume = number ** 3
            print(cube_volume)
        elif operations == "9":
            number = int(input("enter the number:- "))
            total_surface_area_of_cube = 6 * (number ** 2)
            print(total_surface_area_of_cube)
        else:
            print("invalid operation")

    case _:
        print("invalid input")
