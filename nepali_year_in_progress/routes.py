from nepali_year_in_progress import application
from nepali_year_in_progress import basic_auth
from nepali_year_in_progress.models import TwitterClient
from nepali_year_in_progress.helpers import get_text
from apscheduler.schedulers.background import BackgroundScheduler
import requests
slack_hook = "https://hooks.slack.com/services/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"

@application.route('/')
def hello():
    return 'future home page'

@application.route('/post_tweet')
@basic_auth.required
def post_tweet():
    twitter_client = TwitterClient()
    tweet_text = get_text()
    if len(tweet_text)==0:
        return 'not the day to post tweet'
    twitter_client.post_tweet(tweet_text)
    return 'done'


@application.route('/slack_me')
def slack_me():
    requests.post(slack_hook, headers={'Content-type': 'application/json'}, json={'text': 'testing heroku scheduler, should send messages every hour, if not working we gotta pay shit shit shit'})
    return 'done'   

@application.route('/scheduler/start')
@basic_auth.required
def start_scheduler():
    try:
        sched_daily.add_job(slack_me, 'interval', minutes=60,
                            id='tweet_job')
        sched_daily.start()
        return 'start the tweet process'
    except:
        return 'The process might have already started'

@application.route('/scheduler/stop')
@basic_auth.required
def stop_scheduler():
    try:
        sched_daily.remove_job('tweet_job')
        return 'stopped'
    except:
        return 'Job not started or already stopped.'


@application.route('/scheduler/status')
@basic_auth.required
def monitor_daemon():
    try:
        chron_status = str(sched_daily.get_job('tweet_job'))
        return chron_status
    except:
        return 'Check the scheduler'