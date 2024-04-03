// Функція для генерації випадкових імен та фамілій
const generateRandomName = () => {
  const names = ['Сергій', 'Юля', 'Петро', 'Олег', 'Володимир'];
  const lastNames = ['Порошенко', 'Тимошенко', 'Ляшко', 'Труш', 'Надал'];
  const randomName = names[Math.floor(Math.random() * names.length)];
  const randomLastName =
    lastNames[Math.floor(Math.random() * lastNames.length)];
  return `${randomName} ${randomLastName}`;
};

// Функція для отримання статичної дати з київським часовим поясом
const getKyivDate = () => {
  const currentDate = new Date();
  return currentDate.toLocaleString('uk-UA', { timeZone: 'Europe/Kiev' });
};

// Вивід результату в консоль
console.log(
  `Ім'я та фамілія: ${generateRandomName()}, Дата у Києві: ${getKyivDate()}`,
);
