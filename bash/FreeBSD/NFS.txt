sudo chown -R dev:wheel /usr/local/www/nginx-dist
sudo chmod -R 750 /usr/local/www/nginx-dist
sudo chown -R www:www /usr/local/www/nginx-dist


sudo pkg install nfs-server
sudo sysrc nfs_server_enable="YES"

sudo mkdir /atom
sudo chmod -R 777 /atom
sudo nano /etc/exports
/atom -alldirs -network 192.168.1.0 -mask 255.255.255.0

sudo service nfsd start
sudo service nfsd status
sudo service nfsd restart

*NIX
mount -t nfs 192.168.1.222:/Atom /home/Atom
*WIN

New-PSDrive -Name Z -PSProvider FileSystem -Root "\\192.168.1.222\atom" -Persist -Credential (Get-Credential)




----------------
 ls -l /atom
ps -afxu | grep nfs
sudo chmod -R 777 /atom
/usr/local/www/nginx-dist -alldirs -maproot=root
