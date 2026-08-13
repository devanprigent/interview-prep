## Table of contents

- [1. What is the difference between == and ===? Give an example of a comparison that would surprise you if you didn't know about type coercion.](#1-what-is-the-difference-between--and--give-an-example-of-a-comparison-that-would-surprise-you-if-you-didnt-know-about-type-coercion)
- [2. Explain the difference between null, undefined, and NaN — in which cases does each naturally appear in code?](#2-explain-the-difference-between-null-undefined-and-nan--in-which-cases-does-each-naturally-appear-in-code)
- [3. What is hoisting in JavaScript? What's the difference in behavior between a function declaration and an arrow function assigned to a variable?](#3-what-is-hoisting-in-javascript-whats-the-difference-in-behavior-between-a-function-declaration-and-an-arrow-function-assigned-to-a-variable)
- [4. What is a closure? Give a concrete example where a misunderstood closure creates a bug (e.g., in a loop using var vs let).](#4-what-is-a-closure-give-a-concrete-example-where-a-misunderstood-closure-creates-a-bug-eg-in-a-loop-using-var-vs-let)
- [5. What's the difference between a deep copy and a shallow copy in JS? Give an example where this silently breaks application state.](#5-whats-the-difference-between-a-deep-copy-and-a-shallow-copy-in-js-give-an-example-where-this-silently-breaks-application-state)
- [6. When would you choose a Map over a plain object ({}) for storing key-value data in JS?](#6-when-would-you-choose-a-map-over-a-plain-object--for-storing-key-value-data-in-js)
- [7. What's the difference between interface and type in TypeScript? Give a case where one is objectively more suitable than the other.](#7-whats-the-difference-between-interface-and-type-in-typescript-give-a-case-where-one-is-objectively-more-suitable-than-the-other)
- [8. What's the difference between Promise.all, Promise.allSettled, and Promise.race? Give a use case for each.](#8-whats-the-difference-between-promiseall-promiseallsettled-and-promiserace-give-a-use-case-for-each)
- [9. What happens if an async function throws an error but you forget the try/catch around its call? How would you properly handle the error?](#9-what-happens-if-an-async-function-throws-an-error-but-you-forget-the-trycatch-around-its-call-how-would-you-properly-handle-the-error)
- [10. What are `window` and `document` in the browser?](#10-what-are-window-and-document-in-the-browser)
- [11. How does the event loop work in Node.js? What happens if you block the main thread with a heavy synchronous computation?](#11-how-does-the-event-loop-work-in-nodejs-what-happens-if-you-block-the-main-thread-with-a-heavy-synchronous-computation)
- [12. How would you handle a background task (e.g., sending a confirmation email after subscribing) without blocking the HTTP response to the client?](#12-how-would-you-handle-a-background-task-eg-sending-a-confirmation-email-after-subscribing-without-blocking-the-http-response-to-the-client)
- [13. You have a list of insurance coverages and need to quickly retrieve the ones applicable to a given profession. Which data structure would you choose and why (array, Set, Map, index)?](#13-you-have-a-list-of-insurance-coverages-and-need-to-quickly-retrieve-the-ones-applicable-to-a-given-profession-which-data-structure-would-you-choose-and-why-array-set-map-index)

---
#### 1. What is the difference between == and ===? Give an example of a comparison that would surprise you if you didn't know about type coercion.

<details>
<summary>Reveal answer</summary>

The difference is that `==` compares the values of the variables whereas `===` compares the values WITHOUT coercion - which means different types never match.

Why does it matter?

Because Javascript does type coercion. It means that even if you manipulate variables of different types, Javascript will try its best to combine them.

```javascript
console.log("test " + 123) 
// returns "test 123" whereas we're combining string and number
```

It's sometimes useful but when you want to compare, it can lead to unexpected behavior. If you use the simple comparison `==` on variables of different types, Javascript will first try to coerce them and then perform the comparison. Which means you can compare two variables of two different types and Javascript will tell you that those variables are equal.

```javascript
console.log("1" == 1) // returns true
console.log("1" === 1) // return false
```

</details>

---
#### 2. Explain the difference between null, undefined and NaN ?

<details>
<summary>Reveal answer</summary>

In Javascript, you can define a variable without assigning a value and you can display that variable using `console.log`.

For that reason, the language needs a way to represent the lack of value.

The confusing thing in Javascript is that you have two ways to represent the lack of value: `undefined` and `null`.

- `undefined` means a variable exists but has no value assigned yet ;
- `null` means you have intentionally set a variable to have no value.


On the other hand, NaN means "Not a Number" and is the result of an invalid math operation like `0/0`.

</details>

---
#### 3. What is hoisting in JavaScript? What's the difference in behavior between a function declaration and an arrow function assigned to a variable?

<details>
<summary>Reveal answer</summary>

Hoisting refers to the way Javascript treats functions at compilation.

In order to call a variable, you have to initialize it before. If not, you'll get an error. But that's not true for functions. You can call a function at the top of the file and define it only at the bottom.

This is possible because of hoisting. What Javascript does conceptually is that it moves all the functions at the top of the file at compilation so they're available everywhere.

It allows you to use functions before defining them which makes it easier to organize your code. That way, you can have the main logic at the top of the file, define all the sublogic in functions at the bottom - and the code will still run properly.

The tricky part is that only functions are hoisted. However, because arrows functions are essentially variables (they're defined using the keywork let or const), they're not hoisted and will return an error if you try to call them before initialization.

</details>

---
#### 4. What is a closure? Give a concrete example where a misunderstood closure creates a bug (e.g., in a loop using var vs let).

<details>
<summary>Reveal answer</summary>

We talk of closure when an inner function has access to the variables defined in an outer function.


```javascript
function outerFunction(a){
    function innerFunction(b){
        console.log(a,b);
    }

    return innerFunction
}

const myFunc = outerFunction(1);
myFunc(2); // Returns 1,2
```

In this example, we could wonder whether `myFunc(2)` has access to the variable `a` because ``outerFunction`` is gone by the time you execute ``innerFunction``.

That's the whole idea of closure: yes, `innerFunction` still has access to the variable `a`. The function has access to all its variables - called lexical environment - and to the lexical environements of all its parents functions, even if those functions have returned since.

```javascript
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100);
}
// 3, 3, 3  ← bug: all callbacks share the same `i`

for (let i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100);
}
// 0, 1, 2  ← each iteration gets its own `i`
```

</details>

---
#### 5. What's the difference between a deep copy and a shallow copy in JS? Give an example where this silently breaks application state.

<details>
<summary>Reveal answer</summary>

The concept of deep and shallow copy matters when talking about objects.

When you perform a shallow copy of an object, Javascript will copy all the attributes of the object inside the new container.

BUT it will copy different things based on the type of the property. For primitive types - string, number, boolean - Javascript will copy the value.

```javascript
const user = {name: "Alice", age: 25};
const copy = {...user};
copy.name = "Bob";
console.log(user); // {name: Alice, age: 25}
console.log(copy); // {name: Bob, age: 25}
```

In that case, we created a shallow copy, all the attributes were primitive types hence copied by value. Everything works fine.

For complex types - array, object - however, Javascript will copy the reference to the object, and not the value.

```javascript
const user = {name: "Alice", age: 25, data: {city: "Paris", number: 19}};
const copy = {...user};
copy.data.number = 20;
console.log(user); // {name: Alice, age: 25, data: {city: "Paris", number: 20}}
console.log(copy); // {name: Alice, age: 25, data: {city: "Paris", number: 20}}
```

That's when issues arise. Here, we are unvolontarily modifying the original object.

The issue is that the copy holds the reference to the same nested object. Both copy and original are pointing to the same nested object, if one modifies it, the other will see the change.

It can lead to tricky bug where you think you are modifying a local copy, whereas you're actually alterating the original data.

In order to create a completely independent copy, you need to make a deep copy.

A deep copy recursively copies nested objects too, so no shared references remain.

```javascript
const user = {name: "Alice", age: 25, data: {city: "Paris", number: 19}};
const copy = structuredClone(user);
copy.data.number = 20;
console.log(user); // {name: Alice, age: 25, data: {city: "Paris", number: 19}}
console.log(copy); // {name: Alice, age: 25, data: {city: "Paris", number: 20}}
```

</details>

---
#### 6. When would you choose a Map over a plain object ({}) for storing key-value data in JS?

<details>
<summary>Reveal answer</summary>

It's easy to confuse Map and dictionary objects in Javascript because they both can be used to store key-value data.

```javacript
const map = new Map();
map.set("a", 1);
map.set("b", 2);
map.set("c", 3);

const dict = {a:1, b:2, c:3}
```

Historically, the only way to create a hash map was to use a plain object. But later, it was decided to add this new `Map` structure to cover some of the limitation of the object.

First, `Map` accepts any type of keys. You can use string, number, objects, etc, as a key. On the other hand, a plain object accepts only string as keys.

Second, `Map` is iterable directly whereas a plain object is not. It's still possible to iterate over the elements of an object but you first need to transform it into an iterable data structure which costs memory.

```javascript
const map = new Map();
map.set("a", 1);
map.set("b", 2);
map.set("c", 3);

map.forEach((value, key) => console.log(value, key));

const dict = {a:1, b:2, c:3}
Object.entries(dict).forEach(([key, value]) => console.log(key, value));
```
</details>

---
#### 7. What's the difference between interface and type in TypeScript? Give a case where one is objectively more suitable than the other.

<details>
<summary>Reveal answer</summary>

They're basically the same, most of the time you can choose either of them.

The only major difference is that if you have multiple interfaces with the same name, they'll merge into one. It's common when augmenting a library.

```javascript
interface User { name: string }
interface User { age: number }
// → User has both name and age
```

This is not possible with types and would return an error. You would need to use union or advanced composition for that.

</details>

---
#### 8. What's the difference between Promise.all, Promise.allSettled, and Promise.race? Give a use case for each.

<details>
<summary>Reveal answer</summary>

TODO: short answer.

</details>

---
#### 9. What happens if an async function throws an error but you forget the try/catch around its call? How would you properly handle the error?

<details>
<summary>Reveal answer</summary>

TODO: short answer.

</details>

---
#### 10. What are `window` and `document` in the browser?

<details>
<summary>Reveal answer</summary>

`window` is a massive global object accessible in the browser. All global functions and variables are properties of the window object. For instance, `console.log` comes from `window.console.log`.

`document` is the entry point to the DOM i.e the HTML of the entire page represented as a Javascript object.

The link between `window` and `document` is that `document` is a property : `window.document`.

</details>

---
#### 11. How does the event loop work in Node.js? What happens if you block the main thread with a heavy synchronous computation?

<details>
<summary>Reveal answer</summary>

TODO: short answer.

</details>

---
#### 12. How would you handle a background task (e.g., sending a confirmation email after subscribing) without blocking the HTTP response to the client?

<details>
<summary>Reveal answer</summary>

TODO: short answer.

</details>

---
#### 13. You have a list of insurance coverages and need to quickly retrieve the ones applicable to a given profession. Which data structure would you choose and why (array, Set, Map, index)?

<details>
<summary>Reveal answer</summary>

TODO: short answer.

</details>