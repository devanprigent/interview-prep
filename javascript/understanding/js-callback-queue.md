investigation: What's the callback queue in Javascript?

We've seen there is a distinction between the Javascript engine - the thread of execution, the call stack and the memory - which runs the global code and the host APIs which runs whenever the code uses them.

For instance:

```javascript
function printHello(){
    console.log('Hello');
}

function blockForOneSecond(){
    // Some expensive work
}

setTimeout(printHello, 1000);
blockForOneSecond();
console.log("End!");
```

If you run this code, the console will show:
End!
Hello

How is it possible? The code printHello is before the code End! so how comes it's displayed later? If Javascript was purely synchronous, it shouldn't do this.

That's because of the callback queue.

It depends if the host API is synchronous or asynchronous.

A synchronous host API is added to the call stack.

But an asynchronous host API is added to the callback queue.

The callback queue starts to be dequeued and executed only when all the global code has been executed.

