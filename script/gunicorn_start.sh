#!/bin/bash

NAME="news_stat_app"                                        # Name of the application
DJANGODIR=/opt/interface/news_stat                          # Django project directory
SOCKFILE=/opt/interface/run/gunicorn.sock                   # we will communicte using this unix socket
USER=admin                                                  # the user to run as
GROUP=statapps                                              # the group to run as
NUM_WORKERS=3                                               # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=news_stat.settings                   # which settings file should Django use
DJANGO_WSGI_MODULE=news_stat.django_uwsgi                   # WSGI module name
VIRTUALENV_COMMAND=" activate venv2711"                     # virtual env command
LOG_FILE_PATH=/opt/interface/log/gunicorn_log.log           # gunicorn log path
GUNICORN_PATH=/root/.pyenv/versions/2.7.11/envs/venv2711/bin/gunicorn       # gunicorn location

echo "Starting $NAME as 'who am i'"

# Activate the virtual environment
cd $DJANGODIR
source $VIRTUALENV_COMMAND                                    #source ../bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec $GUNICORN_PATH ${DJANGO_WSGI_MODULE}:application \
--name $NAME \
--workers $NUM_WORKERS \
--bind 0.0.0.0:8001 \
--log-level=debug \
--log-file=$LOG_FILE_PATH

#--bind=unix:$SOCKFILE

# Change Permission: sudo chmod u+x bin/gunicorn_start
# Execute: ./gunicorn_start.sh