const name = {
    person: () => {
        const names = ["John", "Alice", "Bob", "Emily"];
        const ages = [20, 25, 30, 35];
        
        const randomNameIndex = Math.floor(Math.random() * names.length);
        const randomAgeIndex = Math.floor(Math.random() * ages.length);
        
        const randomName = names[randomNameIndex];
        const randomAge = ages[randomAgeIndex];
        
        const personData = {
            name: randomName,
            age: randomAge
        };
        
        return personData;
    }
};

// Викликаємо функцію person для отримання випадкових даних про особу
const randomPerson = name.person();
console.log(randomPerson);