sudo pkg install nginx
sudo nano /etc/rc.conf
nginx_enable="YES"
sudo service nginx status
sudo service nginx start
sudo service nginx restart
sudo service nginx stop

sudo service nginx onestatus

sudo nginx -t

sudo pkg install nginx-module-<назва-модуля>
sudo pkg remove nginx-module-<назва-модуля>
