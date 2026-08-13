// What's the issue with this code and how to fix it?

function createHandlers(coverageIds) {
    const handlers = [];
    for (var i = 0; i < coverageIds.length; i++) {
      handlers.push(() => console.log(coverageIds[i]));
    }
    return handlers;
  }
  
  createHandlers(["theft", "fire", "flood"])[0](); // ?


/*
SOLUTION

The current code logs undefined, whereas we would expect "theft".

The issue is that var is function-scoped, so every iteration shares the same i variable.

When the handlers are called later, the loop has already finished and i is 3. Therefore, every handler evaluates coverageIds[3], which is undefined.

The fix is to use let, which is block-scoped. In a for loop, let creates a new binding for i on each iteration, so each handler closes over the correct value.

*/