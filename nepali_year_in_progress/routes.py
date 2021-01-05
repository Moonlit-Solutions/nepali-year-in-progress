from nepali_year_in_progress import application
from nepali_year_in_progress import basic_auth
from nepali_year_in_progress.models import TwitterClient


@application.route('/')
def hello():
    return '█░░░░░░░░░░░░░░░░░░░░░░░░░░░░'


@application.route('/basicauth')
@basic_auth.required
def basicauthtest():
    return 'it works'

@application.route('/post_tweet')
@basic_auth.required
def post_tweet():
    twitter_client = TwitterClient()
    twitter_client.post_tweet('█░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 100%')
    return 'done'