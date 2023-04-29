Оновити до останьої версії
```bash
Invoke-Expression "& { $(irm https://aka.ms/install-powershell.ps1) } -UseMSI"
```
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
Додайте змінені файли до репозиторію Git
```bash
git add .
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
git pull
```
