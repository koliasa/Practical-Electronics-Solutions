let a;
let b;

function myFn() {
  let b;
  a = true; //такого типу перемінні вносять данні в глобальні параметри (не рекомендується робити)
  b = 10;
  console.log(b);
}

myFn();

console.log(a);
console.log(b);
