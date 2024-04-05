Покрокова інструкція по встановленню та налаштуванні сервера на базі ОС Debian 11.7 i386, NGINX, PHP, MariaDB для трьох доменів koliasa.com, ua.mba, teneta.com
після стандартної інсталяції першим кроком в налаштуваннях буде налаштування мережі
для цього перехожу в файл налаштувань /etc/network/interfaces та встановлюю там статичний адрес

---* Налаштування мережі
auto enp4s0
iface enp4s0 inet static
address 192.168.1.222/24
gateway 192.168.1.1
dns-nameservers 1.1.1.1 1.0.0.1

Перезавантажую мережу
sudo systemctl restart networking
sudo systemctl restart networking.service
Після чого налаштовую сервер для роботи з найновішим програмним забезпеченням з експереминтальних портів для цього редагую файл
sudo nano /etc/apt/sources.list
deb http://deb.debian.org/debian unstable main contrib non-free
також не забуваю закоментувати локальні порти

---* Встановлюю SUDO
apt-get update && apt-get install sudo
ln /usr/sbin/usermod /usr/bin
nano /etc/sudoers
dev ALL=(ALL) ALL

---* Wget/Curl/HTOP/MC/asciiquarium
#sudo apt-get update && sudo apt-get install wget curl htop mc -y
#sudo apt update
#sudo apt install snapd

sudo apt update && sudo apt install -y wget curl htop mc snapd
sudo snap install core
sudo snap install asciiquarium
/snap/bin/asciiquarium
asciiquarium

---* встановлюю NGINX, PHP, MariaDB
sudo apt update
sudo apt install --no-install-recommends nginx php mariadb-server
Команда яка встановить ПО з усіма залежностями
#sudo apt install nginx php mariadb-server

---* налаштовую Nginx
sudo systemctl start nginx
sudo systemctl restart nginx


------- Налаштовую хости
Створіть символічні посилання на файли конфігурації в папці /etc/nginx/sites-enabled/:
sudo ln -s /etc/nginx/sites-available/koliasa.com /etc/nginx/sites-enabled/
sudo ln -s /etc/nginx/sites-available/ua.mba /etc/nginx/sites-enabled/
sudo ln -s /etc/nginx/sites-available/xn--80aja5axd.com /etc/nginx/sites-enabled/
Переглянути лінки
ls -la /etc/nginx/sites-enabled/
Якщо потрібно видалити лінк
sudo unlink /etc/nginx/sites-enabled/koliasa.com


Перевіряю статус сервера
sudo systemctl status nginx
якщо все ок, створюю каталоги, даю їм доступ
sudo mkdir /var/www/koliasa
sudo mkdir /var/www/mba
sudo mkdir /var/www/teneta
Також права доступу для користувача та мережі
sudo chown -R dev:www-data /var/www/koliasa
sudo chmod -R 755 /var/www/koliasa
sudo chown -R dev:www-data /var/www/mba
sudo chmod -R 755 /var/www/mba
sudo chown -R dev:www-data /var/www/teneta
sudo chmod -R 755 /var/www/teneta
Додатково якщо потрібно перенести архів чи бекап роблю наступним чином
Для створення архіву, складіть команду наступним чином:
tar -czvf xn--80aja5axd.com.tar.gz /home/teneta/dir/sites/xn--80aja5axd.com
Для розархівування цієї папки, використовуйте наступну команду:
tar -xzvf xn--80aja5axd.com.tar.gz -C /home/teneta/dir/sites/

---* Встановлюю та налаштовую тунель
uname -m
wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-386
chmod +x cloudflared-linux-386
sudo mv cloudflared-linux-386 /usr/local/bin/cloudflared
cloudflared --version

sudo cloudflared service install eyJhIjoiOWViZGZmNzQwN2Q5NGNjNmQxODE4NmVhMDkxNzdjMDQiLCJ0IjoiOTg2MWY4ZDYtNTgwYS00NWU5LWE0OWUtMDYwNzMzNDc4NmJkIiwicyI6Ik1UazFNekpsWkdNdFkyWmlNUzAwTTJVNExUZzROVGt0TVRNeE9HRTVZMlZpWkdSaiJ9

Автозавантаження сервісу в системі
sudo systemctl enable cloudflared.service

Стан тунеля
systemctl status cloudflared.service
curl -I koliasa.com
curl -I ua.mba
curl -I xn--80aja5axd.com

---* Налаштовую MySQL
запускаємо менеджер першочергових налаштувань
sudo mysql_secure_installation
----------------
NOTE: RUNNING ALL PARTS OF THIS SCRIPT IS RECOMMENDED FOR ALL MariaDB
      SERVERS IN PRODUCTION USE!  PLEASE READ EACH STEP CAREFULLY!

In order to log into MariaDB to secure it, we'll need the current
password for the root user. If you've just installed MariaDB, and
haven't set the root password yet, you should just press enter here.

Enter current password for root (enter for none):
root
passwd
----------------
OK, successfully used password, moving on...

Setting the root password or using the unix_socket ensures that nobody
can log into the MariaDB root user without the proper authorisation.

You already have your root account protected, so you can safely answer 'n'.

Switch to unix_socket authentication [Y/n]n
----------------
You already have your root account protected, so you can safely answer 'n'.

Change the root password? [Y/n]
----------------
By default, a MariaDB installation has an anonymous user, allowing anyone
to log into MariaDB without having to have a user account created for
them.  This is intended only for testing, and to make the installation
go a bit smoother.  You should remove them before moving into a
production environment.

Remove anonymous users? [Y/n]Y
----------------
Normally, root should only be allowed to connect from 'localhost'.  This
ensures that someone cannot guess at the root password from the network.

Disallow root login remotely? [Y/n]n
----------------
Remove test database and access to it? [Y/n]
----------------
Reloading the privilege tables will ensure that all changes made so far
will take effect immediately.

Reload privilege tables now? [Y/n]
----------------
All done!  If you've completed all of the above steps, your MariaDB
installation should now be secure.

Thanks for using MariaDB!
----------------
Для входу в базу даних
mysql -u root -p
passwd
mysql -h hostname -u myuser -p

---
#Перевірити статус
sudo systemctl status mysql
# Зупинити сервер
sudo systemctl stop mariadb
# Зупинити всі процеси
sudo killall -u mysql
sudo killall -u mariadb

Логи
sudo less /var/log/mysql/error.log
#для перевірки наявності MariaDB на системі
#dpkg -l | grep mariadb
#Якщо відповідь містить назву пакету mariadb, то видаліть його та його залежності за допомогою наступної команди:
#sudo apt-get purge mariadb-*

--- Даю доступ до бази даних в мережі
sudo nano /etc/mysql/mariadb.conf.d/50-server.cnf
нахожу 
bind-address            = 127.0.0.1
та міняю на
bind-address = 0.0.0.0
skip-networking = false
Після чого перезавантажую БД
sudo systemctl restart mariadb
Тепер можна зєднатися з БД 
mysql -h <192.168.1.222> -u <root> -p
passwd

--- Відновити пароль рута
sudo systemctl stop mariadb
sudo mysqld_safe --skip-grant-tables &
mysql -u root
FLUSH PRIVILEGES;
ALTER USER 'root'@'localhost' IDENTIFIED BY 'passwd';
exit;
sudo systemctl start mariadb