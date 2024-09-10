letter = '😘'
text = "(❁´◡`❁)"
total_text = text + ' ' + letter

print("Текстик:", end=' ')
print(letter, text, total_text, sep='==> ', end='!')
print()  # для отступа в консоли

## циферки

any_num = 1  # int
num = 2.4  # float

total_num = any_num + num  # вообще пофиг на разные типы данных
print(f"{any_num} + {num} = {total_num}")
print(f"{type(total_num)} + {type(num)} = {type(total_num)}\n")  # `\n` - перенос на следующую строку
