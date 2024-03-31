*** ADD SUDO ***
apt-get update && apt-get install sudo
sudo apt-get update && sudo apt-get install sudo
/etc/sudoers
username ALL=(ALL) ALL
---
ln /usr/sbin/usermod /usr/bin
usermod -aG {Group} {Username}
usermod -aG sudo dev
*** ADD SUDO ***



*** ADD SUDO ***
apt-get update && apt-get install sudo
sudo apt-get update && sudo apt-get install sudo
/etc/sudoers
username ALL=(ALL) ALL
---
ln /usr/sbin/usermod /usr/bin
usermod -aG {Group} {Username}
usermod -aG sudo dev
*** ADD SUDO ***

# iface wlp3s0 inet dhcp
sudo systemctl restart networking.service

apt-get --user install -o APT::Install-Suggests=false --assume-yes htop

*** Використовувати останню версію пакунків ***
sudo nano /etc/apt/sources.list
deb http://deb.debian.org/debian unstable main contrib non-free


Debian 11.7 i386 встановити останню версію NGINX, PHP 8.2, MariaDB та інші компоненти для максимально швидкої роботи Wordpress на наступних доменах koliasa.com, ua.mba, xn--80aja5axd.com. Cloudflare tunel для того щоб сервер з віртуальним ІП працював в глобальній мережі як веб сервер для доменів koliasa.com, ua.mba, xn--80aja5axd.com на різних Cloudflare акаунтах