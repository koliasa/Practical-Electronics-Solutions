// найпримітивніший приклад
const value = 11;

value ? console.log('Умова дійсна') : console.log('Умова не вірна');
// З одними тернарними операторами
const value1 = 10;
const value2 = 20;

value1 && value2
      ? console.log('myFunction1 called with:', value1, value2)
      : console.log('myFunction2 called');

// З викликом функцій
const value3 = 10;
const value4 = 20;

// Визначення функцій
function myFunction1(val1, val2) {
      console.log('myFunction1 called with:', val1, val2);
}

function myFunction2() {
      console.log('myFunction2 called');
}

// Виклик функції згідно з умовою
value3 && value4 ? myFunction1(value3, value4) : myFunction2();

// Виведення посилань на функції
console.log(myFunction1);
console.log(myFunction2);
