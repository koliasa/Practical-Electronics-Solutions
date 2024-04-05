const firstName = 'Ihor',
      lastName = 'Koliasa';

let fullNamePlusDate = () => {
      let currentDate = new Date().toLocaleString('en-GB', {
            timeZone: 'Europe/Kiev',
      });
      return `${firstName} ${lastName}, ${currentDate}`;
};

console.log(fullNamePlusDate());

// спроба оголошення даних, назви функції кирилицею, працює;]
const ім_я = 'Ігор',
      прізвище = 'Коляса';

let повнеІм_яПлюсДата = () => {
      let поточнаДата = new Date().toLocaleString('uk-UA', {
            timeZone: 'Europe/Kiev',
      });
      return `${ім_я} ${прізвище}, ${поточнаДата}`;
};

console.log(повнеІм_яПлюсДата());
