// У цьому випадку, якщо b має значення, яке вважається true (наприклад, будь-яке число, окрім 0), тоді виконається console.log("Виконано!").
// Якщо b має значення, яке вважається false (наприклад, 0), тоді console.log("Виконано!") не виконається.
// Отже, якщо b має значення, відмінне від нуля, то в консолі буде виведено "Виконано!".
let b = 10;
b && console.log("Виконано!");
// Але, якщо b має значення 0, то нічого не буде виведено в консоль.
let с = 0;
с && console.log("Виконано!"); // Нічого не виведе в консоль
