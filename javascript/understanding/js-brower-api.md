investigation: What's the Web Browser APIs for Javascript?

If you look at the core Javascript features - the thread of execution, the call stack and the memory - it's actually not much.

You can't do much with only this.

Thanksfully, Javascript doesn't run in isolation. It runs either in the browser for the frontend, or in the node environment for the backend.

And those environments, offer additional features that make Javascript powerful.

For instance, the browser gives access to the DOM, or to useful APIs like `console`, `fetch` or the `localStorage`. 

They're called Web Browsers APIs or host APIs which sound confusing at first.

Like, aren't they just Javascript features ?

No they're not and that's the whole point. They're APIs offered by the environment so Javascript can do lot of stuff it couldn't do otherwise. But it also means they don't work exactly the same as the global code. To understand how they work, we need two other concepts: the callback queue and the event loop.