// код з заздалегідь згенерованою помилкою
const fnWithError = () => {
    throw new Error('Some error');
};

// виловлюємо помилку
try {
    fnWithError();
} catch (error) {
    console.error(error); // Загальне повідомлення про помилку (в даному випадку вичерпне повідомлення про помилку)
    console.log('An error occurred:', error.message); // тільки повідомлення про помилку не обов'язково використовувати error можна використати log
}
// продовжуємо виконувати код
console.log('Continue...');
