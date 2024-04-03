// Оператор розгортання для об'єктів {...}

// Приклад 1: Створення нового об'єкту, розширення та копіювання властивостей
const obj1 = { a: 1, b: 2 };
const obj2 = { ...obj1, c: 3 }; // розгортаємо obj1 та додаємо властивість c

console.log(obj2); // { a: 1, b: 2, c: 3 }

// Приклад 2: Копіювання об'єкта
const original = { x: 1, y: 2 };
const copy = { ...original }; // розгортаємо original для створення копії

console.log(copy); // { x: 1, y: 2 }

// Приклад 3: Об'єднання об'єктів
const objA = { a: 1 };
const objB = { b: 2 };
const merged = { ...objA, ...objB }; // об'єднуємо objA та objB

console.log(merged); // { a: 1, b: 2 }
