function drawSquare(square) {
    let squareString = "";

    // Верхня лінія квадрата
    squareString += "┌" + "─".repeat(square.sideLength) + "┐\n";

    // Бокові лінії квадрата та місце для пояснень
    for (let i = 0; i < square.sideLength - 2; i++) {
        squareString += "│" + " ".repeat(square.sideLength - 2) + "│" + ` Пояснення ${i + 1}\n`;
    }

    // Нижня лінія квадрата
    squareString += "└" + "─".repeat(square.sideLength) + "┘";

    return squareString;
}

// Об'єкт "квадрат"
let square = {
    sideLength: 6
};

// Виведення квадрата в консолі разом з поясненнями
console.log("Квадрат з поясненнями:");
console.log("Довжина сторони квадрата:", square.sideLength);
console.log(drawSquare(square));
