#!/usr/bin/env bash
# script thath sets up the web server for deployment

# install nginx
sudo apt-get update
sudo apt-get -y install nginx

#create folders
sudo mkdir -p /data
sudo mkdir -p /data/web_static
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/shared/test

# Create a fake HTML file
echo "Holberton School" > /data/web_static/releases/test/index.html

#simbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

#ownership and group
sudo chown -R ubuntu:ubuntu /data

#routing to web static
sudo sed -i '/listen 80 default_server;/a location /hbnb_static/ { alias /data/web_static/current/; }' /etc/nginx/sites-available/default

#restart nginx
sudo service nginx restart
