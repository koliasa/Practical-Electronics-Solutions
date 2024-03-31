Онова пакунків
sudo apt update
Повна онова
sudo apt upgrade

Встановлюю MariaDB
sudo apt install mariadb-server -y

Базові налаштування
mysql_secure_installation

Добавляю нового користувача (доступ тільки на рівні сервера)
sudo mysql
GRANT ALL ON *.* TO 'dev'@'localhost' IDENTIFIED BY 'passwd' WITH GRANT OPTION;
FLUSH PRIVILEGES;
exit

Перевіряю чи все ок
sudo systemctl status mariadb
sudo mysqladmin version

Відкриваю доступ до БД в мережі
sudo nano /etc/mysql/mariadb.conf.d/50-server.cnf
закоментовую рядок
#bind-address=0.0.0.0

Дозволяю загальний доступ користувачу dev
sudo mysql
GRANT ALL ON *.* TO 'dev'@'%' IDENTIFIED BY 'passwd' WITH GRANT OPTION;
FLUSH PRIVILEGES;
EXIT;

Перевіряю чи такий користувач існує в базі даних
SELECT user, host FROM mysql.user WHERE user = 'dev';

Переглядаю які дозволи має користувач dev
sudo mysql -u dev -p'passwd' -e "SELECT user, host FROM mysql.user;"


Існують два способи вимкнення режиму strict_trans_tables в MariaDB:

1. Змінити налаштування сервера MariaDB, додавши рядок sql-mode="NO_ENGINE_SUBSTITUTION" у файл /etc/mysql/mariadb.conf.d/50-server.cnf, а потім перезапустити службу MariaDB за допомогою команди systemctl restart mariadb.service.

2. Виконати запит на зміну режиму для поточного сеансу підключення до бази даних. Це можна зробити за допомогою команди: SET SESSION sql_mode='NO_ENGINE_SUBSTITUTION';

Якщо ви не маєте повного доступу до сервера MariaDB, зверніться до свого хост-провайдера, щоб він вимкнув режим strict_trans_tables для вас.

sudo systemctl status mariadb.service
sudo mysqladmin variables -u root -p
sudo systemctl restart mariadb.service
Щоб перезапустити базу даних без перезапуску служби, введіть команду:
sudo mysqladmin flush-tables
Щоб перезапустити базу даних MariaDB, введіть команду:
sudo systemctl restart mariadb.service


*************************************************

--- Повне видалення на прикладі MariaDB
sudo apt-get remove mariadb-server mariadb-client

sudo apt-get purge mariadb-server mariadb-client
sudo apt-get autoremove
sudo apt-get autoclean
- Інсталяція
sudo apt-get update
sudo apt-get install mariadb-server mariadb-client

--- Після цього падає мускул
sudo systemctl stop mariadb
sudo mysqld_safe --skip-grant-tables &
mysql -u root
FLUSH PRIVILEGES;
ALTER USER 'root'@'localhost' IDENTIFIED BY 'passwd';
exit;
sudo systemctl start mariadb
- Логи
sudo less /var/log/mysql/error.log
sudo dmesg | grep -i fs
