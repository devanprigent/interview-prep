// This code triggers IDE warnings when turning it into a typescript file, why ?

try {
  runFragileOperation();
} catch (err) {
  console.log(err.message);
}

/*
SOLUTION

If you are in strict mode, the err object in a catch is typed as unknown.

It sounds confusing at first because you would expect it to be an error. So why type it as unknown ?

Because in the crazy world of Javascript, you can actually throw anything - 

strings, numbers, promises, etc - and not just Errors.

That's why in strict mode, you have this additional defense that forces you to check the type

of the err object.

In the example, the type of err is unknown so you cannot access the message property which

might not exist. You first need to ensure the type of the object.

try {
  runFragileOperation()
} catch (err) {
  if (err instanceof Error) console.log(err.message)
  // Handle err if it's not an `Error`
}

*/