from utils.utilitiesHelper import generate_firstName_and_lastName, generate_random_email_and_password, generate_Name


def user_info(first_name=None, last_name=None, company="", country="United State (US)",
              street_address="", city="", state="", postal_code="",
              phone="", email=""):

    if first_name is None or first_name == "":
        first_name = generate_Name()

    if last_name is None or last_name == "":
        last_name = generate_Name()

    if email is None or email == "":
        random_info = generate_random_email_and_password()
        email = random_info['email']

    address = {"firstName": first_name,
               "lastName": last_name,
               "company": company,
               "country": country,
               "street": street_address,
               "city": city,
               "state:": state,
               "postalCode": postal_code,
               "phone": phone,
               "email": email,
               }

    return address

# #
# if __name__ == '__main__':
#     aa = user_info('fn', "ln", 'com', 'cont', 'str', 'ct', 'stat', 'pc', 'ph', 'em')
#     print(aa['firstName'])
#     print(aa['email'])
