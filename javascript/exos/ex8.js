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