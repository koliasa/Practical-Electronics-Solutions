--- WOL ---
#файл налаштувань для мережевих інтерфейсів
sudo nano /etc/network/interfaces
#щоб активувати WoL
up ethtool -s enp3s0 wol g
#перезавантажити мережевий інтерфейс
sudo ifdown enp3s0 && sudo ifup enp3s0
#перезавантажити систему
sudo reboot

#перевірити чи все працює
sudo ethtool enp3s0

#скачую софтулю з сайту
https://www.depicus.com/wake-on-lan/wake-on-lan-cmd
#сама софтуля
https://www.depicus.com/downloads/wolcmd.zip
#ввожу команду пробудження
wolcmd 00:22:15:dd:73:09 192.168.1.222 255.255.255.0 8900

--- офіційна довідка ---
https://wiki.debian.org/ru/WakeOnLan

sudo nano /etc/network/interfaces
--- особистий файл конфігурації, в котрому статичний ІП, відключенна бездротова мережа, та увімкнено WOL ---
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).

source /etc/network/interfaces.d/*

# The loopback network interface
auto lo
iface lo inet loopback

# The primary network interface
#allow-hotplug enp3s0
#iface enp3s0 inet dhcp
# This is an autoconfigured IPv6 interface
#iface enp3s0 inet6 auto

auto enp3s0
iface enp3s0 inet static
address 192.168.1.222
netmask 255.255.255.0
gateway 192.168.1.1
#dns-domain koliasa.com
dns-nameservers 192.168.1.1 1.1.1.1 1.0.0.1
#пробудження по мережі
up ethtool -s enp3s0 wol g
#автоматизація WOL з офіційної довідки
post-up /sbin/ethtool -s $IFACE wol g
post-down /sbin/ethtool -s $IFACE wol g

#Бездротова мережа
iface wlp2s0 inet manual