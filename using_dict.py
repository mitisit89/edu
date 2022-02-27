adreess_book = {
    "Swaroop": "swaroop@swaroopch.com",
    "Larry": "larry@wall.org",
    "Matsumoto": "matz@ruby-lang.org",
    "Spammer": "spammer@hotmail.com",
}
print("Адрес Swaroop'а:", adreess_book["Swaroop"])

del adreess_book["Spammer"]

print("\nВ адресной книге {0} контактов\n".format(len(adreess_book)))

for name, adreess in adreess_book.items():
    print("Контакт {0} с адресом {1}".format(name, adreess))

adreess_book["Guido"] = "Guido@python.org"
if "Guido" in adreess_book:
    print("\nАдрес Guido:", adreess_book["Guido"])
print("\nВ адресной книге {0} контактов\n".format(len(adreess_book)))
