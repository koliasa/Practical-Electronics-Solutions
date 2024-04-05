systemctl reboot or systemctl poweroff.
ls -alh
ip -c addr show enp3s0

sudo systemctl restart networking.service
sudo systemctl status networking.service

#CHMOD
sudo chown -R k1:sambashare /media/nas/
sudo smbpasswd -a k1