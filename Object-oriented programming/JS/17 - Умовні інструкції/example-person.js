const person = {
      age: 20,
};
//!undefined === true !!undefined === false
if (!person.name) {
      //в цьому прикладі ми викликаємо текстову фразу якщо об'єкт не вказано в умові, або він має значення false
      console.log('Ім`я не вказано');
}

console.log(person.name);

// особистий приклад, якщо елемент іван присутній в оголошенні змінної неймс, то в консоль буде виводитись інформація що таке імя присутнє
let names = 'ivan';
if (names) {
      console.log('Так Іван є в переліку імен');
}

if (!!names) {
      console.log('Не таке імя');
}
