const hello = "Hello";
const world = "World";

const greeting = hello + " " + world; //в даному випадку між лапками присутній "пробіл" так отримуємо пробіл між словами,
// але, для автоматичного форматування можна використовувати шаблонні рядків, приклад далі

console.log(greeting);
// використання шаблонних рядків
const greeting1 = `${hello} ${world}`;
console.log(greeting1);
