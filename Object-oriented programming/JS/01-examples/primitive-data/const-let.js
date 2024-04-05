const firstName = 'Ihor'; //const - статичні дані які не міняються в продовж коду які не можна змінити після того, як вони були призначені.
const lastName = 'Koliasa';

let title = () => {
    //let - дані які впродовж коду можна змінити
    return {
        fullName: firstName + ' ' + lastName,
    };
};

let title1 = () => {
    return {
        fullName: `${firstName} ${lastName}`,
    };
};

console.log(title()); // { fullName: 'Ihor Koliasa' }
console.log(title1()); // { fullName: 'Ihor Koliasa' }
