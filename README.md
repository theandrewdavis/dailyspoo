A simple webserver that shows a new picture of our sadly departed [spoodle](https://en.wikipedia.org/wiki/Cockapoo) every day, made as a gift for my fiancée.

To install on Ubuntu 18.04 LTS:
```
sudo add-apt-repository ppa:certbot/certbot
sudo apt-get update
sudo apt-get install -y python3-venv nginx certbot python-certbot-nginx

git clone https://github.com/theandrewdavis/dailyspoo.git
cd dailyspoo
python3 -m venv venv
./venv/bin/pip install -r requirements.txt
mkdir spoos
chmod a+rx spoos
# copy pictures into spoos
chmod a+r spoos/*
nohup ./venv/bin/python app.py &

# Set up empty site for certbot
sudo rm -f /etc/nginx/sites-enabled/default
sudo cp nginx-http.conf /etc/nginx/sites-enabled/dailyspoos
sudo service nginx restart

# Set up https site
sudo certbot --nginx certonly
echo "renew_hook=service ngnix restart" | sudo tee -a /etc/letsencrypt/renewal/dailyspoo.com.conf
sudo cp nginx-https.conf /etc/nginx/sites-enabled/dailyspoos
sudo service nginx restart
```
