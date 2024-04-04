//масив це об'єкт з цифровими іменами властивостей
// масив 1, 2, 3 в об'єктах myArray та myArray2 хоч і виглядають однаково але находяться в різних місцях пам'яті та є двома окремими об'єктами
const myArray = [1, 2, 3];
// console.log(myArray);
const myArray2 = new Array(1, 2, 3); // в цьому випадку = new назва класу створює новий клас, таким чином можна створювати нові класи.
// console.log(myArray2);

const example = [1, true, 'Ihor'];
// console.log(example);

const example2 = [1, true, 'Ihor'];

let example3 = example; // якщо ми скопіюємо об'єкт то в результаті логу порівняння об'єктів скаже шо це правда
console.log(example3 === example);
console.log(example3 === example2); //а тут буде не правда, тому що це різні об'єкти хоча з однаковими масивами, але з різними об'єктами та даними в пам'яті
