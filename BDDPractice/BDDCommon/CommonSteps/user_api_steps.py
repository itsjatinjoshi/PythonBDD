from behave import step

from utils.utilitiesHelper import generate_random_email_and_password


@step('Generate random email and password')
def i_generate_random_email_and_password(context):
    random_info = generate_random_email_and_password()
    context.email = random_info['email']
    context.pswd = random_info['password']
