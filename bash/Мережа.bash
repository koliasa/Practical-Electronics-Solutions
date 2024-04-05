#переглянути мережеві пристрої
ip -c addr show
#відключити бездротову мережу
sudo nano /etc/network/interfaces
iface wlp2s0 inet manual
#виключаєм wi-fi карту
sudo ip link set dev wlp2s0 down
#перезавантажуємо мережеві служби
sudo systemctl restart networking





#добавити статичний IP в інтерфейс а також нейм сервера клаудфлеєра
sudo ip addr add 192.168.1.223/24 dev enp0s3 && sudo ip route add default via 192.168.1.1 dev enp0s3 && sudo sh -c 'echo "nameserver 1.1.1.1\nnameserver 1.0.0.1" > /etc/resolv.conf'
--- Ubuntu 23.10 ---
#налаштування мережі тут
sudo nano /etc/netplan/50-cloud-init.yaml
#статика
network:
  ethernets:
    enp0s3:
      dhcp4: false
      addresses: [192.168.1.223/24]
      gateway4: 192.168.1.1
      nameservers:
        addresses: [1.1.1.1, 1.0.0.1]
      optional: true
  version: 2
#перезавантажити мережеву службу в убунту 23.10
sudo systemctl restart systemd-networkd