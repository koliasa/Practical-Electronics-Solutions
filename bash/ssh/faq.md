```bash
ssh -i "C:\Users\k1\.ssh\koliasa" k1@192.168.1.222
```

```json

            {
                "guid": "{b453ae62-4e3d-5e58-b989-0a998e100000}",
                "name": "NAS - Debian ",
                "commandline": "ssh -i \"C:\\\\Users\\\\k1\\\\.ssh\\\\koliasa\" k1@192.168.1.222",
                "icon" : "C:\\Users\\k1\\.ssh\\debian.png"
            },
```

Перевіряю чи встановлений сервер
dpkg -l openssh-server

Копіюю ключ в домашній каталог свого користувача на сервері
ssh-copy-id -i ~/.ssh/atom.pub dev@192.168.1.222

/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "/c/Users/dev/.ssh/atom.pub"
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
dev@192.168.1.222's password:

Number of key(s) added: 1

Now try logging into the machine, with: "ssh 'dev@192.168.1.222'"
and check to make sure that only the key(s) you wanted were added.

---\* говорить про успіх

Добавляю в файл конфігурації метод аутентифікації тільки по ключу
sudo nano /etc/ssh/sshd_config

PasswordAuthentication no
ChallengeResponseAuthentication no
UsePAM no

Перезавантажую SSH сервер
sudo systemctl restart ssh

Дивлюсь його статус
sudo systemctl status ssh

Перевіряю чи все працює
ssh -i ~/.ssh/atom dev@192.168.1.222

Пишу для маздая JSON файл для аутентифікації по ключу
{
"guid": "{11111111-0000-1111-0000-111111111111}",
"name": "Atom",
"commandline": "ssh -i C:\\Users\\dev\\OneDrive\\Документи\\Atom\\Network\\ssh\\atom dev@192.168.1.222",
// "commandline": "ssh -i C:\\Users\\dev\\OneDrive\\Документи\\FreeBSD\\ssh\\atom\\w3c dev@192.168.1.222",
// "icon": "C:\\path\\to\\icon.png"
},

ssh-keygen -t ecdsa -b 256
Generating public/private ecdsa key pair.
Enter file in which to save the key (/c/Users/dev/.ssh/id_ecdsa): atom
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in atom
Your public key has been saved in atom.pub
The key fingerprint is:
SHA256:Pt+1edpQU1Fxk75TKdkr9zbXviURBTEe0F2nG7rw5lQ dev@DESKTOP-DAE6DPF
The key's randomart image is:
+---[ECDSA 256]---+
| .o=B@|
| ..**|
| O o|
| + Bo|
| S . . E.=|
| . o + B.|
| o = \* =|
| o = . BB|
| . o +**|
+----[SHA256]-----+
