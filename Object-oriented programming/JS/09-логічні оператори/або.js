// Оператор || (логічне "або") використовується для вибору першого істинного (true) значення серед декількох виразів або операндів.
// Якщо хоча б один з операндів є true, весь вираз поверне true. Якщо всі операнди є false, вираз поверне false.

let isSunny = true;
let isRaining = false;

let isWeatherGood = isSunny || isRaining;

console.log(isWeatherGood); // Виведе true, оскільки хоча б один з операндів (isSunny) є true

// У цьому прикладі isWeatherGood буде true, оскільки isSunny має значення true. Оператор || дозволяє нам обирати перше істинне значення
// серед isSunny та isRaining, тому весь вираз стає true.

let g = 'ihor';
let h = 'petro';

let atLeastOneStartsWithI = g.startsWith('i') || h.startsWith('i');

console.log(atLeastOneStartsWithI); // Виведе true, оскільки g починається з 'i'
// Тут, оскільки g починається з 'i', вираз g.startsWith('i') повертає true, і ми вже знаємо,
// що хоча б один з виразів є true, оскільки ми використовуємо оператор ||, тому результат буде true.
