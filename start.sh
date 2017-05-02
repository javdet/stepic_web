#!/bin/bash

sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm -f /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
/usr/bin/gunicorn -w 2 --bind 0.0.0.0:8080 -D hello:app
# cd ask && /usr/bin/gunicorn -w 2 --bind 0.0.0.0:8000 -D ask.wsgi:application
sudo /etc/init.d/mysql start

