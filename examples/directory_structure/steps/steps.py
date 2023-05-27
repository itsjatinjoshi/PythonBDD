from behave import given, when, then
import logging as logger


@given(u'Enter the Wrong username.')
def step_impl(context):
    print("Enter the Wrong username.")
    logger.info("Hi Hello")
    # raise NotImplementedError(u'STEP: Given Enter the Wrong username.')


@when(u'Click on the login button')
def step_impl(context):
    print("Click on the login button")
    # raise NotImplementedError(u'STEP: When Click on the login button')


@then(u'Send an error wih "user not found"')
def step_impl(context):
    print("Then Send an eror wih user not found")
    # raise NotImplementedError(u'STEP: Then Send an eror wih \'user not found\'')


@given(u'Enter the Wrong password.')
def step_impl(context):
    print("Enter the Wrong password")
    # raise NotImplementedError(u'STEP: Given Enter the Wrong password.')


@then("Send an error wih 'user not found'")
def step_impl(context):
    print("Send an error wih 'wrong password'")
    # raise NotImplementedError(u'STEP: Then Send an error wih \'wrong password\'')


@given(u'leave the username box empty.')
def step_impl(context):
    print("leave the username box empty.")
    # raise NotImplementedError(u'STEP: Given leave the username box empty.')


@then(u'Send an error wih \'Please enter the username\'')
def step_impl(context):
    print("Send an error wih \'Please enter the username\'")
    # raise NotImplementedError(u'STEP: Then Send an eror wih \'Please enter the username\'')


@given(u'leave the password box empty.')
def step_impl(context):
    print("leave the password box empty.")
    # raise NotImplementedError(u'STEP: Given leave the password box empty.')


@then(u'Send an eror wih \'Please enter the password\'')
def step_impl(context):
    print("Send an eror wih \'Please enter the password\'")
    # raise NotImplementedError(u'STEP: Then Send an eror wih \'Please enter the password\'')


@given(u'Enter User\'s Credentials')
def step_impl(context):
    print("Enter User\'s Credentials")
    # raise NotImplementedError(u'STEP: Given Enter User\'s Credentials')


@when(u'Click on Login button')
def step_impl(context):
    print("Click on Login button")
    # raise NotImplementedError(u'STEP: When Click on Login button')


@then(u'Verify it will return 200 response message')
def step_impl(context):
    print("Verify it will return 200 response message")
    # raise NotImplementedError(u'STEP: Then Verify it will return 200 response message')


@given(u'Enter the correct credentials')
def step_impl(context):
    print("Enter the correct credentials")
    # raise NotImplementedError(u'STEP: Given Enter the correct credentials')


@then(u'Click on the login button')
def step_impl(context):
    print("Click on the login button")
    # raise NotImplementedError(u'STEP: Then Click on the login button')


@when(u'Print \'Welcome on home Screen with Username\'')
def step_impl(context):
    print("Print \'Welcome on home Screen with Username\'")
    # raise NotImplementedError(u'STEP: When Print \'Welcome on home Screen with Username\'')


@then("Send an error wih 'Please enter the password'")
def step_impl(context):
    print("Send an error wih 'Please enter the password'")
    # raise NotImplementedError(u'STEP: Then Send an error wih \'Please enter the password\'')


@then("Send an error wih 'wrong password'")
def step_impl(context):
    print('STEP: Then Send an error wih \'wrong password\'')
