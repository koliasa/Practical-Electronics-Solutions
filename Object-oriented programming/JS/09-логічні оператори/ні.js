// оператор який присвоює значення навпаки !
// Оператор ! (логічне "НЕ") використовується для зміни логічного значення операнду на протилежне. Якщо операнд є true, то ! зробить його false, і навпаки.

let isSunny = true;

let isNotSunny = !isSunny; // isNotSunny буде false, оскільки оператор ! змінює true на false

console.log(isNotSunny); // Виведе false

let isRaining = false;

let isNotRaining = !isRaining; // isNotRaining буде true, оскільки оператор ! змінює false на true

console.log(isNotRaining); // Виведе true

let x = 10;
let y = 20;

let result = !(x > y); // результат буде true, оскільки x > y є false, а оператор ! змінює false на true

console.log(result); // Виведе true

// В цих прикладах оператор ! застосовується до різних типів даних, включаючи булеві значення та вирази, які повертають булеві значення.
