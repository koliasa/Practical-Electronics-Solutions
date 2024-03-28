function myFn(a, b) {
  let c;
  (a = a + 1), (c = a + b);

  return c; //ключове слово, після ключового слова будь який код працювати вже не буде
}
// буде результат 14, але в консолі ми нічого не побачимо тому що в консоль даний виклик нічого не вводить
let valera = myFn(10, 3);
// console.log(valera);

function myFn1(a, b) {
  let c;
  (a = a + 1), (c = a + b);

  return c; //ключове слово, після ключового слова будь який код працювати вже не буде
}
// буде результат 14, але в консолі ми нічого не побачимо тому що в консоль даний виклик нічого не вводить
let valera2 = myFn1(22, 3);
// console.log(valera2);

function dev(alpha, beta, gama) {
  let omega = gama * alpha + beta;
  alpha = 10;
  beta = 20;
  gama = alpha + beta;
  console.log(omega);
  return omega; // після нього не виконується нічого, цей запис повертає результат
}
dev();

function dev(alpha, beta, gama) {
  alpha = 10;
  beta = 20;
  gama = alpha + beta;

  let omega = gama * alpha + beta;

  console.log(omega); // Виводимо значення omega всередині функції dev

  return omega;
}

dev(); // Викликаємо функцію dev
