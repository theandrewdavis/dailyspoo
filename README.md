A simple webserver that shows a new picture of our sadly departed [spoodle](https://en.wikipedia.org/wiki/Cockapoo) every day, made as a gift for my fiancée.

To install on Ubuntu 14.04.2 LTS:
```
sudo apt-get update
sudo apt-get install -y git python-pip nginx
sudo pip install virtualenv

git clone https://github.com/theandrewdavis/dailyspoo.git
cd dailyspoo
virtualenv -p python3 venv
./venv/bin/pip install -r requirements.txt
mkdir spoos
chmod a+r spoos/*
# copy pictures into spoos
sudo nohup ./venv/bin/python app.py &

sudo cp nginx.conf /etc/ngnix/sites-enabled/dailyspoos
sudo service nginx restart
```
