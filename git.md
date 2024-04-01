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
pull
```

Відвантажити зміни

```bash
push
```

Показати всі гілки

```bash
branch -a
```

Перейти до гілки

```bash
checkout назва гілки
```

Підключитись до репозиторія

git remote add name url

Звязати гілки локальну з глобальною

push -u origin назва branch

Всі наступні відвантаження командою а також завантажити pull

push

**Ідентифікація з допомогою ключа**
запустити агент

```bash
eval $(ssh-agent)
```

добавити ключ

```bash
ssh-add '/c/Users/k1/.ssh/koliasa'
```

git commit -m "Додавання нового файлу"
git push git main

Оновити налаштування існуючого репо
git remote set-url origin https://github.com/koliasa/git.git
синхронізація
git remote add origin https://github.com/koliasa/git.git

Переглянути історію коментарів
git log
оновити віддалений репозиторій
git push --force
