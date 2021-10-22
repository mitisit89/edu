
def reverse(text):
    return text[::-1]

def is_palidrome(text):
    return text ==reverse(text)
forbidden=('.','?','!',':',';','-','—',' ',)
something= input('Введите текст: ')
something=something.lower
if (is_palidrome(something) and forbidden):
    print  ("Да, это палиндром")
else:
    print("Нет, это не палиндром")
