A simple webserver that shows a new picture of our sadly departed [spoodle](https://en.wikipedia.org/wiki/Cockapoo) every day, made as a gift for my fiancée.

To install on Ubuntu 20.04 LTS:
```
sudo apt-get update
sudo apt-get install -y python3-venv nginx certbot python3-certbot-nginx

git clone https://github.com/theandrewdavis/dailyspoo.git
cd dailyspoo
python3 -m venv venv
./venv/bin/pip install -r requirements.txt
chmod o+x ~
mkdir spoos
chmod o+rx spoos
# copy pictures into spoos
chmod o+r spoos/*
nohup ./venv/bin/python app.py &

# Set up empty site for certbot
sudo rm -f /etc/nginx/sites-enabled/default
sudo cp nginx-http.conf /etc/nginx/sites-enabled/dailyspoos
sudo service nginx restart

# Set up https site
sudo certbot --nginx certonly
echo "renew_hook=sudo service ngnix restart" | sudo tee -a /etc/letsencrypt/renewal/dailyspoo.com.conf
sudo cp nginx-https.conf /etc/nginx/sites-enabled/dailyspoos
sudo service nginx restart
```
