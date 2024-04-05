let profile = {
      firstName: 'Ihor',
      lastName: 'Koliasa',
      nickName: 'k1',
};

let userInfo = ({ firstName, lastName }) => {
      if (!lastName) {
            // return `First name ${firstName} and last name ${lastName}`;
      }
      return `First name ${firstName} and last name ${lastName}`;
};

let result = userInfo(profile);
console.log(result);

// Варік з фруктами
let fruit = {
      apple: 'Big apple',
      banana: 'Super Banana ;]',
};

let infoFruit = ({ apple, banana }) => {
      if (!banana) {
            return `Тільки зараз в магазині свіжі ${apple} та ${banana}`;
      }
      return `Тільки зараз в магазині свіжі ${apple} та ${banana}`;
};

let result1 = infoFruit(fruit);
console.log(result1);
