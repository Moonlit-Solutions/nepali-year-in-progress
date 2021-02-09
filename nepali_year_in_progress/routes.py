from nepali_year_in_progress import application
from nepali_year_in_progress import basic_auth
from nepali_year_in_progress.models import TwitterClient
from nepali_year_in_progress.helpers import get_text
from flask import render_template



@application.route('/')
def hello():
    return render_template('homepage.html')

@application.route('/post_tweet')
@basic_auth.required
def post_tweet():
    twitter_client = TwitterClient()
    tweet_text = get_text()
    if len(tweet_text)==0:
        return 'not the day to post tweet'
    twitter_client.post_tweet(tweet_text)
    return 'done'
