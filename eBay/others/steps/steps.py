from behave import given, then, when


@given(u'take the "{first_number}" and "{second_number}"')
def step_impl(context, first_number, second_number):
    print("FIRST NUMBER : ", int(first_number))
    print("SECOND NUMBER : ", int(second_number))


@when(u'calculate the sum of "{first_number}" and "{second_number}"')
def step_impl(context, first_number, second_number):
    context.total = int(first_number) + int(second_number)


@then(u'Print the total result')
def step_impl(context):
    print("RESULT IS : ", context.total)


@when('multiply "{first_number}" and "{second_number}"')
def step_impl(context, first_number, second_number):
    context.total = int(first_number) * int(second_number)


@when('subtract "{first_number}" and "{second_number}"')
def step_impl(context, first_number, second_number):
    context.total = int(first_number) - int(second_number)


@when('verify if greater number between "{first_number}" and "{second_number}"')
def step_impl(context, first_number, second_number):
    if int(first_number) or int(second_number) == 0:
        print("Not divide by Zero")
        context.total = 0
    elif int(first_number) == int(second_number):
        context.total = 0
    elif int(first_number) > int(second_number):
        context.total = int(first_number)/int(second_number)
    else:
        context.total = int(second_number) / int(first_number)


@when('divide greater with lower')
def step_impl(context):
    pass


@then('if both are same, return 0')
def step_impl(context):
    if int(context.first_number) == int(context.second_number):
        print(0)
