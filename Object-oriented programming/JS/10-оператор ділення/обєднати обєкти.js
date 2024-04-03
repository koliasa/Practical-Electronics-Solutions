const buttonInfo = {
  test: "Buy",
};

const buttonStyle = {
  color: "Red",
  innerWidth: 200,
  innerHeight: 300,
};

//розділяємо два об'єкта на властивості після чого об'єднуємо їх в один об'єкт
const button = {
  ...buttonInfo, //порядок розділення на властивості важливий, відображатись будуть дубльовані властивості останнього об'єкта
  ...buttonStyle,
};

console.table(button);
