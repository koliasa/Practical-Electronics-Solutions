# Завдання проекту
Цей проект розроблений для автоматичного управління освітленням з використанням мікроконтролерів Arduino та реле. Головною метою проекту є зменшення енергоспоживання шляхом автоматичного вимикання світла у відсутність людини.
# Матеріали та компоненти
Для розробки проекту необхідні такі компоненти:
- Arduino Uno;
- Реле (1 канал);
- Датчик руху PIR;
- Фоторезистор;
- Резистор 10К;
- Блок живлення (5 В);
- Комп'ютер з встановленим ПО Arduino IDE.

# Підключення компонентів
## Підключення PIR датчика
- PIR OUT підключається до D2 піна на Arduino Uno;
- VCC підключається до +5 В живлення;
- GND підключається до GND на Arduino Uno.

## Підключення фоторезистора
- Один кінець фоторезистора підключається до A0 піна на Arduino Uno;
- Інший кінець підключається до GND на Arduino Uno;
- Резистор 10К підключається між A0 піном та +5 В живленням.

## Підключення реле
- IN підключається до D3 піна на Arduino Uno;
- VCC підключається до +5 В живлення;
- GND підключається до GND на Arduino Uno.

# Програмне забезпечення
Для розробки програмного забезпечення необхідно встановити Arduino IDE на комп'ютері.
Код програми для Arduino Uno можна знайти в репозиторії за посиланням: 
`https://github.com/koliasa/astro/blob/main/uno/v1.ino`

# Інструкція з використання
1. Підключити Arduino Uno до комп'ютера за допомогою USB-кабелю.
2. Завантажити програму на Arduino Uno за допомогою Arduino IDE.
3. Підключити блок живлення до Arduino Uno.
4. Підключити реле до живлення та пристроїв, які потрібно керувати (освітленням).
5. Підключення компонентів
Для збирання проекту необхідно підключити наступні компоненти до плати Arduino Uno:
- DHT11 датчик температури та вологості
- RTC DS1307 модуль
- Реле для керування освітленням
6. Висновок<br />
Цей проект можна використовувати як стартовий пункт для створення більш складних систем автоматизації. Він показує, як можна використовувати датчики та модулі для керування освітленням в залежності від погодних умов та часу доби. Додавання додаткових функцій, таких як відключення освітлення в залежності від присутності людини або забезпечення безпеки в залежності від рівня шуму, може розширити можливості проекту.<br />
Для більшої ефективності та безпеки рекомендується здійснювати підключення компонентів тільки вимкненого живлення та дотримуватися всіх правил електробезпеки.<br />
7. Джерела та ліцензія<br />
Цей проект був створений з використанням документації та прикладів коду від Arduino та різних інтернет-джерел.<br />
### Ліцензія: MIT
Ви можете використовувати цей проект, його код та документацію, якщо дотримуєтеся умов ліцензії MIT.<br />
### Автори
Цей проект створено автором:
`Коляса Ігор`<br />
Якщо ви маєте будь-які запитання щодо цього проекту, будь ласка, зв'яжіться зі мною за адресою ihor@koliasa.com. Буду радий допомогти вам.
