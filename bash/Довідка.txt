#під час завантаження системи зявляється вікно вводу логіну/паролю 
#в файлі /etc/issue знаходиться інформація яка відображається першою під час завантаження системи
#однією командою ми вносимо запис у файл issue з наступними даними
sudo nano /etc/issue SHA256:OAGlMO2xRC5RPNlQhvSXpJkPUtaTberZoPs9Deb+Ico \n \l
sudo echo -n "Koliasa Construction Management \n \l" | sudo tee /etc/issue
#в файлі /etc/motd знаходиться перша інформація після входу в систему, над користувачом
#в Ubuntu файли привітань знаходяться  тут /etc/update-motd.d
#10-help-text знаходиться заголовок та посилання
#60-unminimize інший текст
