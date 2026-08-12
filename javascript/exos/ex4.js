// What's the issue with this code and how to fix it?

function addCoverage(policy, newCoverage) {
  policy.coverages.push(newCoverage);
  return policy;
}

const basePolicy = { id: 1, coverages: ["theft"] };
const updatedPolicy = addCoverage(basePolicy, "fire");

console.log(basePolicy.coverages); // ?