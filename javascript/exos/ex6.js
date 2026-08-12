// What's the issue with this code and how to fix it?

function createHandlers(coverageIds) {
    const handlers = [];
    for (var i = 0; i < coverageIds.length; i++) {
      handlers.push(() => console.log(coverageIds[i]));
    }
    return handlers;
  }
  
  createHandlers(["theft", "fire", "flood"])[0](); // ?