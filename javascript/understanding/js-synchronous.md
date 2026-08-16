investigation: synchronous execution overview in Javascript

When you run a Javascript code, it uses a single thread.

This thread will run the process to read and execute the code line by line.

This way of doing things - a thread executing one line at a time - is called synchronous execution.

After reading a line, the thread needs somewhere to execute the code and to store values. This is what we call an execution context.

There are several execution contexts : global and locals.

At the start of the program, Javascript creates a global execution context - that's where the top-level code is executed and where the global variables are stored.

Whenever a function is called, Javascript creates a local execution context to run its code and stores its local variables.

So each time the thread encouters a variable, it stores it in the current execution context. Either in the global execution context if you are at the top of the file, or in a local execution context if you are into a function.

Now, how does Javascript know when to switch between the global execution context and the local ones?

It uses the call stack.

The call stack is a data structure which tracks all the execution contexts currently active. It tells Javascript which execution context is currently running.

The first element on the call stack is always the global execution context. Javascript pushes it right after creating it.

Then, whenever the thread encounters a function to execute, it creates the execution context for this function and then pushes it onto the call stack. 

Once the function has been executed and returns, its execution context is popped off the call stack. The thread execution returns to the next element in the call stack. If the function was nested into another function, then the thread execution will return to that parent function and so on. Once all functions have been executed, it returns to the last element of the call stack: the global execution context.

