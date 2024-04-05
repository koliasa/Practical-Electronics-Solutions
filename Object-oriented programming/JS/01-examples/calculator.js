// Оголошуємо функцію-калькулятор з параметрами a, b та операцією op
function calculator(a, b, op) {
      // В залежності від операції виконуємо відповідну дію
      switch (op) {
            case '+':
                  return a + b;
            case '-':
                  return a - b;
            case '*':
                  return a * b;
            case '/':
                  // Перевіряємо ділення на нуль
                  if (b === 0) {
                        throw new Error('Division by zero is not allowed');
                  }
                  return a / b;
            default:
                  throw new Error('Unsupported operation');
      }
}

// Приклад використання функції calculator
try {
      const result = calculator(10, 5, '+'); // 10 + 5 = 15
      const result1 = calculator(2048, 2, '/'); // 2048 / 2 = 1024
      const result2 = calculator(12, 867, '*'); // 12 * 867 = 10404

      console.log('Result:', result);
      console.log('Result:', result1);
      console.log('Result:', result2);
} catch (error) {
      console.error('Error:', error.message);
}
