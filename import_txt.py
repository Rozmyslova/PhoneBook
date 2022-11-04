def import_txt():
    file = open('phonebook.txt', 'r', encoding="utf-8")
    phb = file.read()
    return phb
