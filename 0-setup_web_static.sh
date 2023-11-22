#!/usr/bin/env bash
# sets up web servers for the deployment of web_static:
# - installs nginx
# - creates /data/, /data/web_static/, /data/web_static/releases/,
# - /data/web_static/releases/test, /data/web_static/releases/test/index.html
# - creates a sym link /data/web_static/current -> /data/web_static/releases/test/
# - grants /data/ -> ubuntu and group
# - update nginx conf to serve /data/web_static/current/
# - restart nginx
apt-get -y update
apt-get -y install nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
web="<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"
echo "$web" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i "/^\tlocation \/ {$/ i\\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n}" /etc/nginx/sites-available/default
service nginx restart
exit 0
