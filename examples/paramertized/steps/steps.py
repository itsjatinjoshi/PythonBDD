from behave import given, when, then
import logging as logger


@given(u'Enter a int "{value}"')
def step_impl(context, value):
    value = int(value)
    logger.info(value)


@when(u'Multiply "{value}" up to 10')
def step_impl(context, value):
    for i in range(1, 10+1):
        print(value + " * ", i, " = ", int(value) * i)
        logger.info(value + " * ", i, " = ", value * i)


@then(u'Verify "{value}" run 10 times')
def step_impl(context, value):
    logger.info(f"{value} ran 10 times")
