from utilities import cli
from utilities import constants


args = cli.get_cli_args()

browser = args.browser
env = args.env
report = args.report
scope = args.scope

base_url = constants.URLS[env]
