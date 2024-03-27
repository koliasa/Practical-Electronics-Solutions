
const gtmButton = {
    leftclick: true,
    add: {
        gtmOver: 'beta',
        gtmbad: true 
    }
}

gtmButton.rightclick = 'fail'
gtmButton.clickscroll = true
gtmButton.editbutton = 'dont touch me'

console.log(gtmButton.add.gtmOver)

delete gtmButton.leftclick
//delete gtmButton.add.gtmOver
//delete gtmButton.add.gtmbad

console.log(gtmButton)


let gtmCkick = 'left click';
gtmButton[gtmCkick] = 'je mazuta';

gtmCkick = null;

console.log(gtmCkick); 

///////

const gtmButton = document.querySelector('.gtm-button');

function toggleButton() {
  if (gtmButton.classList.contains('active')) {
    gtmButton.classList.remove('active');
    console.log('Button deactivated');
  } else {
    gtmButton.classList.add('active');
    console.log('Button activated');
  }
}

gtmButton.addEventListener('click', toggleButton);

// Функція toggleButton вмикає або вимикає клас 'active' для елемента з класом '.gtm-button'.
// Якщо елемент вже має цей клас, він видаляє його, і навпаки.
// Після зміни стану кнопки в консолі виводиться відповідне повідомлення.
function toggleButton() {
    gtmButton.classList.toggle('active');
    console.log(`Button ${gtmButton.classList.contains('active') ? 'activated' : 'deactivated'}`);
  }
  
  // Додаємо обробник події 'click' до кнопки '.gtm-button'.
  gtmButton.addEventListener('click', toggleButton);
  