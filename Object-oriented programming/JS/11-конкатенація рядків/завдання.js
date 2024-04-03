const infoPlusName = {
  info: 'Мене звати',
  name: 'Ігор',
};

const infoMyPlaces = {
  infoPlaces: 'Я живу в місті:',
  town: 'Тернопіль',
};

// варіант з об'єднанням рядків
const announcements = { ...infoPlusName, ...infoMyPlaces };
// варіант з шаблонними виразами, рядками
let city = `${infoMyPlaces.infoPlaces} ${infoMyPlaces.town}`;

console.log(infoPlusName.info + ' ' + infoPlusName.name); //вивід в консоль мануальним способом
console.log(city); //вивів на консоль з допомогою шаблонів
console.log(JSON.stringify(announcements)); //вивів на консоль з допомогою об`єднання об`єктів
