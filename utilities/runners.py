from unittest import TextTestRunner
from HtmlTestRunner import HTMLTestRunner
from utilities import constants

html_test_runner = HTMLTestRunner(
    output=constants.REPORTS_DIR,
    report_name=constants.REPORT_NAME,
    report_title=constants.PROJECT_NAME,
    combine_reports=True,
    add_timestamp=True,
)

text_test_runner = TextTestRunner(verbosity=2)
