// Оператор && (логічне "і") використовується для перевірки, чи обидва операнди є істинними (true). Якщо обидва операнди є true, то результат виразу також буде true.
// Якщо хоча б один з операндів є false, то результат виразу буде false.

let isSunny = true;
let isWarm = false;

let isGoodWeather = isSunny && isWarm;

console.log(isGoodWeather); // Виведе false, оскільки хоча б один з операндів (isWarm) є false

// У цьому прикладі isGoodWeather буде false, оскільки хоча isSunny має значення true, але isWarm має значення false.
// Оператор && потребує, щоб обидва операнди були true, щоб результат був true. Таким чином, весь вираз стає false.

let a = 10;
let b = 20;
let c = 30; // Додавання змінної c для порівняння

const beta = {
  isEqual: a === c, // Порівняння a з c
  result: a && b, // Використання оператора && для знаходження результату a && b
};

console.log(beta);

let e = 10;
let f = 20;

let bothNonZero = e && f; // Якщо обидва a і b не є нульовими, результат буде true (або значення b), інакше результат буде false (або значення a)

console.log(bothNonZero); // Виведе 20, оскільки обидва a і b є true (не нульовими)

let g = 'ihor';
let h = 'petro';

let bothStartWithI = g.startsWith('i') && h.startsWith('i');

console.log(bothStartWithI); // Виведе false, оскільки хоча g починається з 'i', h починається з 'p'
// У цьому прикладі, ми перевіряємо, чи обидві змінні g та h починаються з літери 'i'. Вираз g.startsWith('i') повертає true, оскільки рядок 'ihor' починається з 'i'.
// Проте, вираз h.startsWith('i') повертає false, оскільки рядок 'petro' не починається з 'i'. Коли ми використовуємо оператор &&, обидва вирази повинні бути true,
// щоб результат був true. У нашому випадку, один з них є false, тому результат буде false.
