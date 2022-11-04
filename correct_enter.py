def correct_enter():
    correct_phone_number = False
    while not correct_phone_number:
        num = input("Enter a phone number: ")
        if "+" == num[0]:
            num = num[1:]
        if not num.isdigit():
            print("This isn`t a correct phone number")
            continue
        else:
            int(num)
            if len(num) != 11:
                print('Phone number has 11 digits. Check the phone number')
                continue
            else:
                if 7 == num[0]:
                    plus = "+"
                    num = plus + str(num)
                return num
