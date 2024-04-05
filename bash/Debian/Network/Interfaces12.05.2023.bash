# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).

#source /etc/network/interfaces.d/*

# The loopback network interface
#auto lo
#iface lo inet loopback

# The primary network interface
#allow-hotplug enp4s0
#iface enp4s0 inet dhcp
# This is an autoconfigured IPv6 interface
#iface enp4s0 inet6 auto


#My
auto enp4s0
iface enp4s0 inet static
address 192.168.1.222/24
gateway 192.168.1.1
dns-nameservers 1.1.1.1 1.0.0.1 193.41.60.1