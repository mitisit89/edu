import os
import time
#1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
source =["C:\\Windows10Upgrade","C:\\Documents/js_edu"]
# Заметьте, что для имён, содержащих пробелы, необходимо использовать
# двойные кавычки внутри строки
target_dir="C:\\Backup"# Подставьте тот путь, который вы будете использовать
# 3. Файлы помещаются в zip-архив.
# 4. Именем для zip-архива служит текущая дата и время.
today=target_dir+os.sep+time.strftime('%Y%m%d')
# Текущее время служит именем zip-архива
now = time.strftime('%H%M%S')

if not os.path.exists(today):
    os.mkdir(today) # создание каталога
target=today+os.sep+now+'.zip'

zip_commad="zip -qr {0} {1}".format(target,' '.join(source))
# Запускаем создание резервной копии
print(zip_commad)
if os.system(zip_commad)==0:
    print("Резервная копия успешно создана в",target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')
#ПРОВЕРЯЙ ОФРОГРАФИЮ!!!
