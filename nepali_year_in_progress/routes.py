from nepali_year_in_progress import application
from nepali_year_in_progress import basic_auth
from nepali_year_in_progress.models import TwitterClient
from nepali_year_in_progress.helpers import get_text
from apscheduler.schedulers.background import BackgroundScheduler
import requests
from flask import render_template


slack_hook = "https://hooks.slack.com/services/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"
sched_daily = BackgroundScheduler(daemon=True)


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


@application.route('/slack_me')
def slack_me():
    requests.post(slack_hook, headers={'Content-type': 'application/json'}, json={
        'text': 'testing heroku scheduler'})
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
