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

Права доступу
sudo chown -R dev:www-data /var/www/koliasa
sudo chmod -R 755 /var/www/koliasa

Дозволити вордпресу створювати файли та каталоги на сервері в папці /var/www/koliasa
sudo chown -R www-data:www-data /var/www/koliasa
