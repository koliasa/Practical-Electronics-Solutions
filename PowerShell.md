Оновити до останьої версії
```bash
Invoke-Expression "& { $(irm https://aka.ms/install-powershell.ps1) } -UseMSI"
```

## GIT шпаргалка
Генеруєм
ssh-agent.cmd
```bash
@echo off
echo Starting ssh-agent...
start ssh-agent
echo Adding SSH key...
ssh-add C:\path\to\your\ssh\key
echo Done.
```
Згенерувати ключ
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
ssh-keygen -o -t rsa -C "your_email@example.com"
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```
Перевірити, чи вже є SSH-ключ на вашому комп'ютер
```bash
cat ~/.ssh/
```
Якщо виникнуть проблеми з підключенням, ви можете перевірити статус SSH-ключа, виконавши команду:
```bash
ssh -T git@github.com
```
Налаштувати Git на використання SSH замість HTTPS. Це можна зробити за допомогою команди:
```bash
git ls-remote https://github.com/koliasa/w3c.git
git ls-remote git@github.com:koliasa/w3c.git
```
Налаштуйте Git для автоматичної аутентифікації за допомогою вашого SSH-ключа, щоб ви могли здійснювати операції з GitHub без потреби вводити свій логін та пароль кожен раз. Для цього виконайте наступну команду в терміналі:
```bash
git config --global credential.helper wincred
```
Це налаштування збереже ваші дані авторизації в менеджері авторизації Windows і автоматично надасть доступ до репозиторіїв на GitHub, якщо ви авторизуєтеся на своєму комп'ютері.

## Перевіряємо служби
Переконайтеся, що служба ssh-agent включена. Введіть наступну команду в командному рядку:
```bash
Get-Service ssh-agent | Select-Object Status
```
Якщо статус служби вказує на те, що вона вимкнена, введіть наступну команду, щоб увімкнути її
```bash
Set-Service ssh-agent -StartupType Automatic
```
```bash
Start-Service ssh-agent
```
Перевірити статус агента
```bash
eval "$(ssh-agent -s)"
```
Добавити ключ до агента
```bash
ssh-add ~/.ssh/
```
Скопіювати ключ
```bash
clip < ~/.ssh/
```

## Дії
Щоб склонувати репозиторій з використанням SSH ключа, потрібно виконати таку команду:
```bash
git clone git@github.com:<ваше-ім'я-користувача>/<назва-репозиторію>.git
```
```bash
GIT_SSH_COMMAND="ssh -i ~/.ssh/git.pub" git clone git@github.com:koliasa/w3c.git C:\www\git
```
```bash
set GIT_SSH_COMMAND=ssh -i D:\www\w3c\git
git clone git@github.com:koliasa/w3c.git
```
Для клонування репозиторію з використанням SSH ключа і збереження його в папку D:\www\w3c можна використати наступну команду:
```bash
GIT_SSH_COMMAND="ssh -i D:\www\w3c\git" git clone git@github.com:koliasa/w3c.git D:\www\w3c
```
Зафіксуйте зміни в репозиторії Git, додавши коментар про зміни.
```bash
git commit -m "Додав файли для синхронізації з GitHub"
```
Оновіть віддалений репозиторій на GitHub, використовуючи ключ SSH
```bash
git push
```


Додайте змінені файли до репозиторію Git
```bash
git add .
```
```bash
git pull
```
