from behave import given, then, when



# @before_all("BEFORE ALL")
@given(u'Add 2 numbers')
def step_impl(context):
    context.a = 10
    context.b = 2


@when(u'pass first num')
def step_impl(context):
    assert context.a > 0, "First num is negative"


@when(u'pass second num')
def step_impl(context):
    assert context.b > 0, "Second num is negative"


@then(u'verify sum')
def step_impl(context):
    c = context.a + context.b
    assert c > context.a or c > context.b, "Total is lower after sum"


@then(u'Verify Multiplication')
def step_impl(context):
    c = context.a * context.b
    assert c > context.a or c > context.b, "Multiplication is lower after sum"


@then(u'verify subtraction')
def step_impl(context):
    c = context.a - context.b
    assert c < context.a or c < context.b, "Subtraction is higher after sum"
