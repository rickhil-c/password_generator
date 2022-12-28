import random
import string

print("Hello,welcome to this random Random_Password_Generator")
print("")
initial_response = input("Do you want to generate some passwords?")
yes = True
no = False


def get_password(length):
    # r = "".join(random.choice(chars) for i in range(int(length)))
    r_string = ""
    for i in range(int(length)):
        c = random.choice(chars)
        r_string = r_string + c
    return r_string


if initial_response:
    length = input("How long do you want your password to be?")
    number = input("How many passwords do you want to generate?")
    chars = string.ascii_letters + string.digits

    for _ in range(int(number)):
        r = get_password(length)
        print(r)
else:
    exit()
