import random
num=random.randint(1,50)
running=True

while running:
    guess=int(input('Введите целое число :'))
    if guess == num:
        print('Поздравляю, вы угадали.')
        running = False # это останавливает цикл while
    elif guess < num:
        print('Нет, загаданное число немного больше этого')
    else:
        print('Нет, загаданное число немного меньше этого.')
else:
    print('Цикл while закончен.')
# Здесь можете выполнить всё что вам ещё нужно
print('Завершение.')
