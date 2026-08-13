// What's the issue with this code and how to fix it?

function addCoverage(policy, newCoverage) {
  policy.coverages.push(newCoverage);
  return policy;
}

const basePolicy = { id: 1, coverages: ["theft"] };
const updatedPolicy = addCoverage(basePolicy, "fire");

console.log(basePolicy.coverages);

/*
SOLUTION

In the code, we pass the basePolicy as an argument of the addCoverage function

and then we modify it. Because non-primitive parameters are passed by reference, we

don't actually copy basePolicy, we pass the reference to the same object and then

we mutate it.

It's not wrong per se but because the function returns the object and we assign

the returned value to the variable updatedPolicy, it looks like we were expecting

to create a copy without mutating the original object.

The solution is to make a deepcopy of the policy.

function addCoverage(policy, newCoverage) {
  const copyPolicy = structuredClone(policy);
  copyPolicy.coverages.push(newCoverage);
  return copyPolicy;
}

*/