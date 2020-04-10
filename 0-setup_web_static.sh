#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static.
apt-get update -y
apt-get install -y nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/ 
echo "This is my sample content" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current 
chown ubuntu:ubuntu -R /data/
regex="^\tlocation+"
location="\n\n\tlocation \/hbtn_static\/ \{\
\n\t\talias \/data\/web_static\/current\/\
\n\t\tautoindex off\;\
\n\t\}"
sed -i -r "s/$regex/$location\n\n\0/g" /etc/nginx/sites-enabled/default
service nginx stop
service nginx start
