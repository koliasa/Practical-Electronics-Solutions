const person = {
  name: "bob",
  age: 21,
};
//person.Age = 22
//person.isAdult = true
const person2 = Object.assign({}, person);
person2.age = 33;
person2.isAdult = true;
// console.log(person.age)
// console.log(person.name)
// console.log(person2.isAdult)
//
// console.log(person2.age)
// console.log(person.name)
// console.log(person2.isAdult)

// об'єкт та умова копіювання об'єкту, коли не має внутрішніх об'єктів. З внутрішніми об'єктами об'єкт не працює
const pid = {
  name: "pilar",
  age: 30,
};

const pid2 = Object.assign({}, pid); // працює тільки коли в умові відсутні внутрішні об'єкти
pid2.age = 20;
pid2.name = "duns";
// console.log(pid)
// console.log(pid2)

// Оператор Spread, або розділення об'єкта на властивості (якщо з spread поміняти вложені об'єкти то вони також будуть мутувати, будуть мінятись)
const person3 = { ...person };
person3.age = 33;
person3.isAdult = true;
// console.log(person3.age)
// console.log(person3.isAdult)
// console.log(person.age)
// console.log(person.name)

// Оператор з подвійною конвертацією який копіює повністью обєкт та вносить в нього зміни
const person4 = JSON.parse(JSON.stringify(person));
person4.name = "stepan";
person4.age = 55;

let person5 = {};
person5.name = person4.name;
person5.name = "PAN";

// console.log(person)
// console.log(person1)
// console.log(person2)
// console.log(person3)
// console.log(person4)
console.log(person.name);
console.log(person4.name);
console.log(person5.name);
