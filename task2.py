string = str(input("Введите строку: "))

count_c = 0
length = len(string)
nw_string = str()

for i in range(length):
    if (i == 2):
        continue
    if (string[i] == 'с'):
        count_c += 1                                    
        print(f"Есть символ 'с'. Количество: {count_c}.")
        
    nw_string += string[i]
    
    if (i + 1 == length):
        print("Строка без последнего символа:", nw_string[:-1])

print(f"Длина строки равна = {len(string)}")

