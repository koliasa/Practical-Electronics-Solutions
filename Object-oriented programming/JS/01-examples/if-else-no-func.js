let fruit = {
      apple: 'Big apple',
      banana: 'Super Banana ;]',
};

if ('banana' in fruit) {
      console.log(`banana key ${fruit.banana} exists`); // Цей блок виконається, оскільки ключ "banana" є у об'єкті fruit
} else {
      console.log('banana key does not exist'); // Цей блок не виконається, бо ми маємо ключ "banana" у об'єкті fruit
}
