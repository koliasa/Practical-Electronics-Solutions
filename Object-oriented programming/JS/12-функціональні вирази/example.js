const currentDate = new Date(); // Створення нового екземпляру дати
console.log(currentDate); // Виведення поточної дати у консоль

const newPost = (post, addedAt = Date()) => ({ ...post, addedAt }); //неявний виклик функції визивається дужками для того щоб не створювати нового імені
const firstPost = {
    id: 1,
    author: 'Ihor',
};

let result = newPost(firstPost);
console.log(result);
