
from behave import given, when, then, step
from BDDCommon.CommonFunctions import webcommon
from BDDCommon.Configs import configs


@step('I go to "{website}" page')
@given(u'go to the site "{website}"')
def go_to_url(context, website):
    url = configs.URL_CONFIG.get(website)
    print(f"Navigate to the site: {url}")
    context.driver = webcommon.go_to(url)


@then(u'Verify the title should be "{expected_title}"')
def verify_title(context, expected_title):
    webcommon.assert_page_title(context, expected_title)


@then(u'Verify the url should be "{expected_url}"')
def verify_title(context, expected_url):

    webcommon.assert_current_url(context, expected_url)
