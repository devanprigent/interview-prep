function makeCounter() {
    let count = 0;
    return function () {
      count++;
      return count;
    };
  }
  
const counterA = makeCounter();
const counterB = makeCounter();

console.log(counterA()); // ?
console.log(counterA()); // ?
console.log(counterB()); // ?


/*
SOLUTION


console.log(counterA()); // 1
console.log(counterA()); // 2
console.log(counterB()); // 1

Because the inner function forms a closure over the count variable, its value will be persisted and the

counter will work as expected.

Each call on makeCounter will create a new independent count variable.

*/