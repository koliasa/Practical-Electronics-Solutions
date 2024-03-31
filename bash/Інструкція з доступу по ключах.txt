#згенерувати ключ
ssh-keygen -t rsa -b 2048 -C "Ihor Koliasa <ihor@koliasa.com>" -f koliasa
#Стандартне Windows сховище ключів
C:\Users\k1\.ssh
#Передати публічний ключ на сервер
scp C:\Users\k1\.ssh\koliasa.pub k1@192.168.1.222:~/.ssh/
#Добавити на сервері в список авторизованих ключів
ssh k1@192.168.1.222 "cat ~/.ssh/koliasa.pub >> ~/.ssh/authorized_keys"
#Перевірити чи працює ключ
ssh -i "C:\Users\k1\.ssh\koliasa" k1@192.168.1.222

--- додатково ---
#перезавантажити SSH сервер
sudo systemctl restart sshd

--- налаштування ---
sudo nano /etc/ssh/sshd_config

PasswordAuthentication no
PubkeyAuthentication yes
AuthorizedKeysFile      .ssh/authorized_keys


--- стара довідка ---


#Добавити наступні записи у файл sshd_config
#відключаємо доступ по паролю
PasswordAuthentication yes
#доступ з допомогою сертифікату
PubkeyAuthentication yes
#шукати ключі в домашній директорії користувача у папці
AuthorizedKeysFile      .ssh/authorized_keys
#Перевірити чи запущений SSH сервер
sudo systemctl status sshd
#Перевірити чи відкриті порти
sudo ss -tlpn
#зайти в директорію та згенерувати ключ для доступу (щоб не вводити пароль кожного разу потрібно поле паролів залишити пустим)
cd ~/.ssh/ && ssh-keygen -t ecdsa -b 256 -f nas
#добавити ключ в список авторизованих ключів
cat nas.pub >> ~/.ssh/authorized_keys
#скопіювати ключ в каталог клієнта
scp k1@192.168.1.222:/home/k1/.ssh/nas C:\Users\k1\.ssh\nas
#перевірити чи працює ключ
ssh -i "C:\Users\k1\.ssh\nas" k1@192.168.1.222
--- кінець довідки ---




--- додатково ---
# як добавити сервер в закладки до Windows терміналу
            {
                "guid": "{b453ae62-4e3d-5e58-b989-0a998e100000}",
                "name": "NAS - Debian ",
                "commandline": "ssh -i \"C:\\\\Users\\\\k1\\\\.ssh\\\\nas\" k1@192.168.1.222",
                "icon" : "C:\\Users\\k1\\.ssh\\debian.png"
            },




--- NAS Debian ---
SHA256:4yQmwHRUbw1awGa2SkZsQCwXVcPGJ5WirVrSgqh7ku0 k1@atom
The key's randomart image is:
+---[ECDSA 256]---+
| o=*+*=o+.       |
|.oo.+ @=oo       |
| ooo B.=o .      |
|   .+ o.         |
|.. +.oo S        |
|o o =o + .       |
|.o =    .        |
|+ +              |
|.=E              |
+----[SHA256]-----+

















---інші нотатки
#витерти ключ
ssh-keygen -R 192.168.1.222

C:\Users\k1\.ssh
mkdir -p ~/.ssh && touch ~/.ssh/authorized_keys && cat nas-debian.pub >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
#вказати повний шлях до файлу nas-debian.pub
cat /home/k1/.ssh/nas-debian.pub >> ~/.ssh/authorized_keys
#скопіювати ключ на клієнт
scp k1@192.168.1.222:~/.ssh/nas-debian.pub C:\Users\k1\.ssh\nas-debian.pub

# Відредагувати файл конфігурації 
sudo nano /etc/ssh/sshd_config
#добавити наступні написи
PasswordAuthentication no
PubkeyAuthentication yes

#для того щоб відключити доступ з ключами
PasswordAuthentication no
ChallengeResponseAuthentication no
UsePAM no

--- помилки ---
# якщо випадково видалено всі ключі то згенерувати їх по новому можна командою
sudo ssh-keygen -A
sudo service ssh --full-restart
# скопіювати ключ до директорії
cat ~/.ssh/nas-debian-public.pub | ssh k1@192.168.1.222 "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"

#згенерувати складний ключ
ssh-keygen -t rsa -b 4096 -C "ihor@koliasa.com" -f nas-debian
scp k1@192.168.1.222:/home/k1/.ssh/nas C:\Users\k1\.ssh\nas
scp k1@192.168.1.222:/home/k1/.ssh/nas.pub C:\Users\k1\.ssh\nas.pub