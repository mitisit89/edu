def callback_1():
    print("Я первый коллбэк")


def callback_2():
    print("Я второй коллбэк")


def callback_3():
    print("Я третий коллбэк")


callbacks = [callback_1, callback_2, callback_3]  # Обратите внимание, что скобок нет.
# Мне нужны не результаты вызова функций, а сами функции

for callback in callbacks:
    callback()  # а вот здесь я уже вызываю функции
