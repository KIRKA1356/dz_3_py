#Задача 1(3.10)
# def convert():
#     """ 
#     Функция переобразовывает десятичное число в 16ое
#     """
#     num = int(input("Введите число в десятичной системе: "))
#     result =  []
#     while (num>0):
        
#         if num % 2 == 0:
#             result.insert(0,"0")
#         else: 
#             result.insert(0,"1")
#         num //= 2
    
    
#     a = (f"Ваше число в 16ой системе: ")   
#     b = "{0:X}".format(int("".join((str(i) for i in result)), 2))
#     word = a + b
#     print (word)
# convert()

# Задача 2(3.11)

def pruf():
    """
    Проверка дроби
    """
    num = (input("Введите ваше число: "))
    prof = num.find("/" or ".")
    print(prof)
