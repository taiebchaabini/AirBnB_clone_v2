#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static.
apt-get install -y nginx
service nginx start
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/ 
echo "This is my sample content" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current 
chown ubuntu:ubuntu -R /data/
service nginx restart
