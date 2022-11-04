from user_interface import choice_to_do
from user_interface import choice_file_format
from import_tsv import import_tsv
from import_txt import import_txt
from new_contact import get_contact
from export_tsv_contact import export_tsv_contact
from export_txt_contact import export_txt_contact


def to_do():
    do_it = True
    while do_it:
        operation = choice_to_do()
        if operation == '1':
            data_file_format = choice_file_format()
            if data_file_format == '1':
                file_phb = import_tsv()
                print(file_phb)
            else:
                file_phb = import_txt()
                print(file_phb)
        elif operation == '2':
            data = get_contact()
            export_tsv_contact(data)
            export_txt_contact(data)
        else:
            break
