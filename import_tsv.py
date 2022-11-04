def import_tsv():
    file = open('phonebook.tsv', 'r', encoding="utf-8")
    phb = file.read()
    return phb
