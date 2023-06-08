from behave import step

from utils.utilitiesHelper import generate_random_email_and_password
from BDDCommon.CommonAPI import user_api
from BDDCommon.CommonDAO.usersDAO import UserDAO


@step('Generate random email and password')
def i_generate_random_email_and_password(context):
    random_info = generate_random_email_and_password()
    context.email = random_info['email']
    context.password = random_info['password']


@step('I call create customer api')
def call_create_customer_api(context):
    payload = {"email": context.email, "password": context.password}
    response = user_api.create_user(data=payload)
    assert response['email'] == context.email, \
        f"Wrong email in response. Expected {context.email}," \
        f"Actual {response['email']}."


@step('customer should created')
def verify_user_created(context):
    verify_response = UserDAO().get_user_by_email_from_database(context.email)
    # import pdb; pdb.set_trace()
    print("USER EMAIL: ", verify_response)
    assert len(verify_response) == 1, f"User {context.email} not found."
    user_name = context.email.split('@')[0]
    assert verify_response[0]['user_login'] == user_name, "User Created in DB, doesn't exist"
