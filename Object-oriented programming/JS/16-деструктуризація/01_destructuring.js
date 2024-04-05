const fruits = ['apple', 'banana'];

const [fruitOne, fruitTwo] = fruits; //призначає назви масивів згідно з ІД елементів основного масиву

console.log(fruitOne);
console.log(fruitTwo);

let strawberry = fruits.push('strawberry'); // так ще добавити метод полуниця
console.log(fruits);

fruits.push('avocado'); //добавив в масив елемент без масиву авокадо
console.log(fruits);

// let fruits2 = () => ({
//   date: 'set date',
//   au: 1,
// });
// console.log(fruits2());
