188.163.32.101
Tunnel name
Atom
Tunnel ID
9861f8d6-580a-45e9-a49e-0607334786bd
email i.koliasa@outlook.com
hostname koliasa.com

---* Інсталяція/видалення сервісу
sudo cloudflared service uninstall
sudo cloudflared service install
---* Автозавантаження сервісу в системі
sudo systemctl enable cloudflared.service
---* Стан тунеля
systemctl status cloudflared.service
curl -I koliasa.com
---* Ручне керування
enable disable start stop restart
sudo systemctl start cloudflared.service
sudo systemctl stop cloudflared.service
-------
sudo systemctl stop cloudflared
sudo systemctl disable cloudflared
sudo rm /etc/systemd/system/cloudflared.service
sudo cloudflared service uninstall
sudo cloudflared service install
sudo cloudflared tunnel login
sudo cloudflared tunnel create my-tunnel
sudo cloudflared tunnel run my-tunnel

-------------------------------------------------------------------
# Налаштування для Debian 11.7 i386 на прикладу домену: koliasa.com:84/localhost:84
sudo cloudflared service install eyJhIjoiOWViZGZmNzQwN2Q5NGNjNmQxODE4NmVhMDkxNzdjMDQiLCJ0IjoiOTg2MWY4ZDYtNTgwYS00NWU5LWE0OWUtMDYwNzMzNDc4NmJkIiwicyI6Ik1UazFNekpsWkdNdFkyWmlNUzAwTTJVNExUZzROVGt0TVRNeE9HRTVZMlZpWkdSaiJ9
---* тенета.com/xn--80aja5axd.com:83/localhost:83
sudo cloudflared service install eyJhIjoiZDJjMjNhZDIwZTdjNDg0ZDY0NzIwMjllYWEyMzFlMmMiLCJ0IjoiODhhMWFmYWQtMzFjYy00ZWMzLWFhMjQtZWFhZTdjOGNjYWIwIiwicyI6Ik4yWmxOVEUzWTJZdE16RmtNQzAwWVdKbUxXSTNNVEl0TnpFeFpXWmtObVkwT1dZMyJ9
---*ua.mba:82/localhost:82
CNAME ua.mba koliasa.github.io (Налаштований на ГІТ)
18e1014a-8e0a-496e-bc00-1c61e64870e3

sudo cloudflared service install --service-name=mba 
sudo cloudflared service install 
eyJhIjoiMTU3YzM5NmIzM2ZiZWRkNzM2ZThjM2U5ZDAyMjcxZTUiLCJ0IjoiMThlMTAxNGEtOGUwYS00OTZlLWJjMDAtMWM2MWU2NDg3MGUzIiwicyI6IlpXRmlNbUUxWmprdE5HVTRZUzAwWWpGaUxXRXlNakV0TmpSaU16WmtaVGN4TmpZMSJ9


Запустіть тунель як службу системи. Щоб тунель запускався автоматично при перезавантаженні сервера, його можна налаштувати як службу системи. Для цього створіть файл з налаштуваннями служби з іменем <domain>.service у папці /etc/systemd/system/ з наступним змістом:

[Unit]
Description=Cloudflare Tunnel: <domain>
After=network-online.target

[Service]
Type=simple
ExecStart=/usr/local/bin/cloudflared tunnel run <domain>
Restart=
