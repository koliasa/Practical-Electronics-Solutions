let a = 5,
    b = 10,
    c = 20;

function calc() {
    let d = a + a;
    let e = c - b;
    let f = a * 2;
    return {
        text: 'Your result',
        result: [d, e, f],
    };
}

console.log(calc());
