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

# def pruf():
#     """
#     Проверка дроби
#     """
#     num = (input("Введите ваше число: "))
#     prof = num.find(".")
#     prof2 = num.find(",")
#     if prof>0 or prof2>0: print("Ваше число дробное")
#     else: print("Ваше число не является дробью")
# pruf()

# Задача 3(3.12)

# def cut():
#     text = (input("Введите ваш текст и нажмите ENTER: "))
#     index = text.find('о')
#     index2 = text.rfind('о', text.find('о')-1 )  
    
#     if index<0 and index2<0: print("В вашем тексте нет буквы о!")
    
#     elif index>0 and index2==index: 
#         print("В вашем тексте одна буква о, вот текст после нее и до конца текста:")
#         print(text[index+1:])
#     else: 
#         print("Вот ваш срез: ")
#         print(text[index+1:index2])
    
# cut()