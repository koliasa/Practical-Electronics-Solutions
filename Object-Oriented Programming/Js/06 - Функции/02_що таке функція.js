// let a = 5
// let b = 3

// let c

// c = a + b
// console.log(c)

// a = 8
// b = 12

// c = a / b * a
// console.log(c)
//   return c після нього не працює взагалі нічого

// let asgasdgasg = 25

//  console.log(asgasdgasg)

function sum(a, b) {
  const c = a + b;

  // Розраховуємо суму знижки (8% від значення c)
  const discount = c * 0.08;
  // Віднімаємо знижку від значення c
  const result = c - discount;

  console.log(c);
  console.log(result); // Виводимо результат без 8% знижки
}

// Передаємо значення a та b у функцію sum
const a = 10;
const b = 10;
sum(a, b);
