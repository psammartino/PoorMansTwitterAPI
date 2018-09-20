# Poor Man's Twitter API

## Build Setup

``` bash
# create python 3.6 virtualenv
virtualenv -p python3 .env

# install dependencies
pip install -r requirements.txt

# run migrations
python manage.py migrate

# run development server
python manage.py runserver
