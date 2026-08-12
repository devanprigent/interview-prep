// What's the issue with this code and how to fix it?

function hasSeenClaim(seenClaims, claim) {
    return seenClaims.includes(claim);
  }
  
const seen = [{ id: 1 }, { id: 2 }];
console.log(hasSeenClaim(seen, { id: 1 })); // ?