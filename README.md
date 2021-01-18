
# Installation

#### Clone the repository

`https://github.com/Moonlit-Solutions/nepali-year-in-progress`


#### CD into the cloned directory and create a virtualenv

`python -m venv env`


### Enable virtualenv

`.\env\Scripts\activate`


### Enable virtualenv (windows)

`.\env\Scripts\activate`

### Install dependency packages from requirements.txt

`pip install -r requirements.txt`

### Run flask app
`source FLASK_APP="app.py"`
`flask run`

### Run flask app (windows)
`$env:FLASK_APP="app.py"`
`flask run`

# URLs
`/post_tweet` posts progress tweet directly (depending on if the day of the year is "optimal" for posting tweet

`/scheduler/start` starts the scheduler which triggers every 24 hours

`/scheduler/stop` stops the scheduler


# .env

Add Twitter keys and BasicAuth keys to the .env_sample file. Once complete rename it to .env
