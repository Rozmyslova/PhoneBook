from user_interface import choice_file_format


def import_tsv():
    dicts_phb_tsv = {}
    with open('phonebook.tsv', 'r', encoding="utf-8") as file_phb:
        phb_list = []
        for line in file_phb:
            line = str(line)
            print(line)
            one_line = tuple(line,)
            phb_list.append(one_line)
    print(phb_list)
    num_phb_list = enumerate(phb_list)
    print(num_phb_list)
    for i, j in num_phb_list:
        dicts_phb_tsv.setdefault(i, []).append(j)
    print(dicts_phb_tsv)
    """else:
        file_phb = import_txt()
        print(file_phb)"""