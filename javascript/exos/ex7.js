// What's the issue with this code and how to fix it?

function hasSeenClaim(seenClaims, claim) {
    return seenClaims.includes(claim);
  }
  
const seen = [{ id: 1 }, { id: 2 }];
console.log(hasSeenClaim(seen, { id: 1 })); // ?


/*
SOLUTION

The issue is that includes compare objects by reference.

It's like doing `{ id: 1 } === { id: 1 }`. It will always return false because even if the

values are the same, those are two different objects with two different references.

So in the example, this would return false.

One solution would be to track only the ids in the seen object - instead of objects - and pass only

the id number in the claim parameter instead of an object.

*/