from behave import given, when, then

from BDDCommon.CommonFunctions import webcommon


@given(u'go to the site "{url}"')
def go_to_url(context, url):
    print(f"Navigate to the site: {url}")
    context.driver = webcommon.go_to(url)


@then(u'Verify the title should be "{expected_title}"')
def verify_title(context, expected_title):
    assert webcommon.assert_page_title(context.driver.title, expected_title)


@then(u'Verify the url should be "{expected_url}"')
def verify_title(context, expected_url):
    assert webcommon.assert_current_url(context.driver.url, expected_url)
