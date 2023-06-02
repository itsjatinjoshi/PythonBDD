from behave import given, when, then


@given(u'I login as a User')
def step_impl(context):
    print("Welcome User")


@when(u'I added a "{total_price}" book to the cart')
def step_impl(context, total_price):
    context.total_price = 40


@when(u'Select the "{state}"')
def step_impl(context, state):
    context.total = 0
    if state == 'CA':
        context.total = context.total_price + 5
        # print("$", context + 5)
    elif state == 'NY':
        context.total = context.total_price + 4
        # print("$", context + 4)
    elif state == 'TX':
        context.total = context.total_price + 3
        # print("$", context + 3)
    elif state == 'DC':
        context.total = context.total_price + 2
        # print("$", context + 2)
    else:
        print("There will be no tax on the book")


@then(u'Tax will calculate according to "{state}"')
def step_impl(context, state):
    print("The Total Price of the book is : ", context.total,
          "in the ", state)


@given(u'I have "{Quantity}" of items')
def step_impl(context, Quantity):
    context.Quantity = 1


@when(u'I checked out using "{Payment_Method}"')
def step_impl(context, Payment_Method):
    context.paymentMethod = Payment_Method


@then(u'I got "{percentage}" of discount.')
def step_impl(context, percentage):
    context.percentage = 0
    if context.Quantity > 2 and context.paymentMethod == 'credit card':
        context.percentage = 3
        print(f"You will get {context.percentage}% discount")
    elif context.Quantity > 2 or context.paymentMethod == 'master card':
        context.percentage = 2
        print(f"You will get {context.percentage}% discount")
    elif context.paymentMethod == 'debit card' or context.paymentMethod == 'visa card':
        context.percentage = 4
        print(f"You will get {context.percentage}% discount")
    else:
        print(f"There is no discount on the {context.paymentMethod}")
