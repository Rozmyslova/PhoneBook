def export_txt_contact(data):
    with open('phonebook.txt', 'a+', encoding="utf-8") as phb:
        phb.write(f'Фамилия: {data[0]}\nИмя: {data[1]}\nНомер телефона: {data[2]}\nОписание: {data[3]}\n\n')
