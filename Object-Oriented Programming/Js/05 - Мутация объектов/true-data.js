const name = {
  person: () => {
    const personData = {
      name: "John",
      age: 25,
      gender: "male",
      occupation: "engineer",
      // додайте інші дані, які вам потрібно
    };

    return personData;
  },
};

// Викликаємо функцію person для отримання точних даних про особу
const exactPerson = name.person();
console.log(exactPerson);
