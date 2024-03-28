// ці скобки () потрібно коли не має жодних параметрів, та в тілі функції тільки виводиться наступне інфо
function printMyName() {
  console.log("Ihor");
}
console.log("start");
setTimeout(printMyName, 1000);
