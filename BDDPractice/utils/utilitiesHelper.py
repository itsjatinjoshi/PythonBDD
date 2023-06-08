import random
import string


def generate_random_email_and_password(domain=None, email_prefix=None):
    if not domain:
        domain = 'supersqa.com'
    if not email_prefix:
        email_prefix = 'testuser'

    random_email_string_length = 10
    random_string = ''.join(random.choices(string.ascii_lowercase, k=random_email_string_length))
    email = email_prefix + "_" + random_string + '@' + domain

    password_length = 20
    password_string = ''.join(random.choices(string.ascii_letters, k=password_length))

    random_info = {'email': email, 'password': password_string}
    print(f"Random Username is {random_info['email']} and password is {random_info['password']}.")
    return random_info


def generate_firstName_and_lastName():
    random_fName_length = 6
    random_lName_length = 6
    random_fName = ''.join(random.choices(string.ascii_letters.lower(), k=random_fName_length))

    random_lName = ''.join(random.choices(string.ascii_letters.lower(), k=random_lName_length))

    random_info = {'first_name': random_fName, 'last_name': random_lName}
    return random_info


def generate_Name():
    random_length = 6
    random_name = ''.join(random.choices(string.ascii_letters.lower(), k=random_length))
    return random_name
