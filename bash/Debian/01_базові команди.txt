sudo systemctl status cloudflared
sudo systemctl start cloudflared
sudo systemctl restart cloudflared

---* Мережа
sudo systemctl restart networking.service
sudo nano /etc/network/interfaces
sudo nano /etc/resolv.conf
sudo nano /etc/hosts

ip addr show
ethtool enp4s0
sudo ip link show
ping google.com

sudo ip link set enp4s0 down && sudo ip link set enp4s0 up
sudo ip link show enp4s0
sudo ip addr del fd9c:381c:f87f:0:222:15ff:fedd:7309/64 dev enp4s0
sudo ip addr del fe80::222:15ff:fedd:7309/64 dev enp4s0
Відключити IPV6
sudo sysctl -w net.ipv6.conf.enp4s0.disable_ipv6=1

---* Оновлення
Оновіть список доступних пакетів
sudo apt-get update
Онова пакунків
sudo apt update
Повна онова
sudo apt upgrade

Перезавантаження/Виключення
sudo shutdown -r now
sudo shutdown -h now

Повне видалення
sudo apt-get remove fancontrol
sudo apt-get autoremove
sudo apt-get purge fancontrol

Процеси
sudo lsof -i :3306
sudo kill <PID>
sudo systemctl start mariadb

---* Права доступу
sudo chmod -R 755 /var/www/
sudo chown -R dev:www-data /var/www/
sudo chown -R www-data:www-data /var/www/


sudo chown -R dev:www-data /var/www/koliasa
sudo chmod -R 755 /var/www/koliasa
sudo chown -R www-data:www-data /var/www/koliasa
sudo usermod -aG www-data dev

----* koliasa.com
koliasa
localhost
passwd
passwd

----* ua.mba
mba
localhost
passwd
Dev
passwd
passwd