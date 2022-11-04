def choice_to_do():
    your_choice = False
    while not your_choice:
        print("Choose phone book operations:\n\
            1 - reading;\n\
            2 - adding new contact;\n\
            3 - exit")
        op = input("Enter a operation's number: ")
        your_choice = True
    return op


def choice_file_format():
    print("Choose file format:\n\
        1 - tsv;\n\
        2 - txt")
    file_for = input("Choose a file format: ")
    return file_for
