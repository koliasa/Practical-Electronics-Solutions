// НЕ РЕКОМЕНДУЄТЬСЯ ВИКОРИСТОВУВАТИ МУТАЦІЇ ТАКОГО ТИПУ
const personOne = {
  name: "Bob",
  age: 21,
};
// Викликаємо функцію в котрій добавляємо один рік,
function increasePersonAge(person) {
  person.age += 1;
  return person;
}
// Повертає значення з personOne
console.log(personOne.age);
// повертає значення з функції increasePersonAge
increasePersonAge(personOne);
console.log(personOne.age);
