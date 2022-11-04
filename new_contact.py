from correct_enter import correct_enter as c_ent


def get_contact():
    data = []
    last_name = input('Enter a last name: ')
    data.append(last_name)
    first_name = input('Enter a first name: ')
    data.append(first_name)
    phone_number = c_ent()
    data.append(phone_number)
    description = input('Enter a comment: ')
    data.append(description)
    return data
