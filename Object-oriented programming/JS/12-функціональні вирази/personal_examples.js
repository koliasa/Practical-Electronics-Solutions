// Визначаємо функцію, яка повертає об'єкт з ім'ям, датою та випадковою фамілією
let namePlusDate = (name, date = new Date()) => {
  // Масив випадкових фамілій
  let randomLastNames = ['Barabolja', 'Inkvizutor', 'LaBomba', 'Koliasa'];

  // Випадково вибираємо фамілію з масиву
  let randomLastName =
    randomLastNames[Math.floor(Math.random() * randomLastNames.length)];

  // Створюємо рядок з даними
  let result = `{ date: '${date}', name + lastName: '${name}', '${randomLastName}' }`;

  // Виводимо рядок у консоль
  console.log(result);
};

// Викликаємо функцію з ім'ям "Ihor" та виводимо результат у консоль
namePlusDate('Ihor');
