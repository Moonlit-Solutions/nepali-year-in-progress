from nepali_year_in_progress import application
from nepali_year_in_progress import basic_auth


@application.route('/')
def hello():
    return 'hello'


@application.route('/basicauth')
@basic_auth.required
def basicauthtest():
    return 'it works'
