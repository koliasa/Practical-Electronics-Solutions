function myFn(a) {
    console.log(a);
}

const b = true;
let c = 10;

myFn(2 + 3);
myFn(b);
myFn((c = c + 1));
myFn((c = c + 1));
myFn((let = d));
