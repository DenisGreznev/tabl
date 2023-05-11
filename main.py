# Печать таблицы умножения 
print("Multiplication Table in Hexadecimal:")
for i in range(1, 16):
    row = ''
    for j in range(1, 16):
        result = ((i * j))
        hex_result = hex(result).upper()
        hex_result = hex_result[2:]
        if len(hex_result) < 2:
            hex_result = '0' + str(hex_result)
            row += hex_result + "\t"
        else:
            row += hex_result + "\t"
    print(row)

# Печать таблицы сложения 
print("Addition Table in Hexadecimal:")
for i in range(1, 16):
    row = ''
    for j in range(1, 16):
        result = i + j
        hex_result = hex(result).upper()
        hex_result = hex_result[2:]
        if len(hex_result) < 2:
            hex_result = '0' + str(hex_result)
            row += hex_result + "\t"
        else:
           row += hex_result + "\t"
    print(row)
