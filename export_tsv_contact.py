def export_tsv_contact(data):
    with open('phonebook.tsv', 'a+', encoding="utf-8") as phb:
        if len(data[0]) > 10:
            phb.write(f'{data[0]}\t{data[1]}\t\t{data[2]}\t\t{data[3]}\n')
        elif len(data[0]) > 7:
            phb.write(f'{data[0]}\t\t{data[1]}\t\t{data[2]}\t\t{data[3]}\n')
        else:
            phb.write(f'{data[0]}\t\t\t{data[1]}\t\t{data[2]}\t\t{data[3]}\n')

