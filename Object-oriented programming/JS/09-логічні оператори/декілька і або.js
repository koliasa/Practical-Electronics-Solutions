// У виразі a && b && c && d, всі змінні a, b, c і d є операндами оператора &&, який представляє логічне "І".
// Це означає, що весь вираз буде true лише тоді, коли всі змінні будуть true.

// Наприклад, якщо ми маємо такі значення змінних:

let a = true;
let b = false;
let c = true;
let d = true;

let result = a && b && c && d;
console.log(result); // Виведе false

// У цьому прикладі, змінна b має значення false, тому весь вираз буде false, оскільки всі операнди повинні бути true, щоб результат був true.

// Але, якщо ми змінимо значення змінної b на true:

let e = true;
let f = true;
let g = true;
let h = true;

let result1 = e && f && g && h;
console.log(result1); // Виведе true

// Тепер усі змінні a, b, c і d мають значення true, тому весь вираз також буде true.

// У виразі a || b || c || d, всі змінні a, b, c і d є операндами оператора ||, який представляє логічне "АБО".
// Це означає, що весь вираз буде true, якщо хоча б одна змінна буде true.

// Наприклад, якщо ми маємо такі значення змінних:

let n = false;
let o = true;
let p = false;
let q = true;

let result2 = n || o || p || q;
console.log(result2); // Виведе true

// У цьому прикладі, хоча змінні n та p мають значення false, змінні o та q мають значення true, тому весь вираз буде true, оскільки хоча б один операнд є true.

// Але, якщо ми змінимо значення змінної o на false:

let w = false;
let r = false;
let t = false;
let y = false;

let result3 = w || r || t || y;
console.log(result3); // Виведе false
// Тепер всі змінні мають значення false, тому весь вираз буде false.
