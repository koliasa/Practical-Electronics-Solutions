**Створити локального користувача**

```bash
git config --global user.name "Ihor Koliasa"
```

```bash
git config --global user.email ihor@koliasa.com
```

Перевірити налаштування

```bash
git config --list
```

Ініціалізація репозиторія

```bash
git init
```

Переглянути приховані папки та файли

```bash
ls -la
```

_Індекс репозиторія, переглянути його статус_

```bash
git status
```

Зберегти репозиторій локально

```bash
git clone
```

Завантажити зміни

```bash
git pull
```

Відвантажити зміни

```bash
git push
```

Показати всі гілки

```bash
git branch -a
```

Перейти до гілки

```bash
git checkout назва гілки
```

Підключитись до репозиторія

```bash
git remote add name url
```

Звязати гілки локальну з глобальною

```bash
gitpush -u origin назва branch
```

Всі наступні відвантаження командою а також завантажити pull

```bash
git push
```

**Ідентифікація з допомогою ключа**
запустити агент

```bash
eval $(ssh-agent)
```

добавити ключ

```bash
ssh-add '/c/Users/k1/.ssh/koliasa'
```

```bash
git commit -m "Додавання нового файлу"
```

```bash
git push git main
```

Оновити налаштування існуючого репо

```bash
git remote set-url origin https://github.com/koliasa/git.git
```

синхронізація

```bash
git remote add origin https://github.com/koliasa/git.git
```

Переглянути історію коментарів

```bash
git log
```

оновити віддалений репозиторій

```bash
git push --force
```
