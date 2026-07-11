# Next.js — interview questions

## Table of contents

- [1. Why would you choose Next.js? What problem does Next.js solve?](#1-why-would-you-choose-nextjs-what-problem-does-nextjs-solve)
- [2. What's the difference between CSR and SSR?](#2-whats-the-difference-between-csr-and-ssr)
- [3. What's a Server Component? What are its benefits and limitations?](#3-whats-a-server-component-what-are-its-benefits-and-limitations)
- [4. What's a Client Component? What are its benefits and limitations?](#4-whats-a-client-component-what-are-its-benefits-and-limitations)
- [5. How do Client Components interact with Server Components?](#5-how-do-client-components-interact-with-server-components)
- [6. Where should you fetch data in Next.js?](#6-where-should-you-fetch-data-in-nextjs)
- [7. Why is fetching data in a Server Component often better than using useEffect?](#7-why-is-fetching-data-in-a-server-component-often-better-than-using-useeffect)
- [8. Explain the concept of request waterfalls.](#8-explain-the-concept-of-request-waterfalls)
- [9. What's Suspense?](#9-whats-suspense)
- [10. What's Streaming?](#10-whats-streaming)
- [11. What are React Server Actions?](#11-what-are-react-server-actions)
- [12. What's a Route Handler?](#12-whats-a-route-handler)
- [13. How does a request flow from the browser to the database?](#13-how-does-a-request-flow-from-the-browser-to-the-database)
- [14. What's a Route Group?](#14-whats-a-route-group)

---

#### 1. Why would you choose Next.js? What problem does Next.js solve?

<details>
<summary>Reveal answer</summary>

Next.js is a Javascript framework built on top of React.

By default, React gives only Client-Side Rendering (CSR) meaning that an empty HTML is sent to the client with a tag `<script>` and the entire UI is built in the client's browser. The problem of this approach is that your application starts as an empty shell and users have to stare at a blank screen before the JS bundle is finally downloaded and parsed. It's also harmful for the website's SEO because some search engine crawlers may not execute JS and see an empty page.

Next.js solves that problem by offering other rendering strategies such as SSR (render HTML per request on the server), SSG (render HTML at build time), ISR (rebuild static pages on a timer/on-demand) and CSR.

Then Next.js offers additional benefits:

- It offers an in-built file-based routing system whereas you have to build everything from scratch with React.
- It allows creating a full-stack application entirely in Javascript without needing a separate Node.js server.
- It offers various performance optimizations such as image optimization, font optimization, Server Components and Streaming.

</details>

---

#### 2. What's the difference between CSR and SSR?

<details>
<summary>Reveal answer</summary>

CSR stands for Client-Side Rendering. It means the server sends a minimal HTML file with a script tag as well as the JS bundle. The client's browser downloads, parses and executes that JS to build the entire UI on the client-side.

The problem with this approach is that it takes time to do all of that work. And while it's all happening, the user is staring at a blank white screen.

That's why SSR was introduced.

SSR stands for Server-Side Rendering. Instead of sending an empty HTML file, the server pre-builds an HTML which is then sent to the browser. That way, as soon as the html file is downloaded, the client will see content. This content won't yet be interactive however because it was created server-side. The browser still needs to run React and attach event listeners to the DOM to make the application interactive. This step is called the hydration. The browser receives a "dry" HTML and React "hydrates" it with interactivity by attaching event listeners.

If we talk in terms of Web performance, there are three steps when a browser renders an application received by the server:
- Time To First Byte (TTFB) which is the time before receiving the first byte of response from the server.
- First Contentful Paint (FCP) which is the time before showing the first piece of content to the user.
- Time To Interactive (TTI) which is the time before the user can actually use the application.

So SSR trades a slower TTFB (because server does rendering work) for a faster FCP whereas the TTI stays basically the same.

</details>

---

#### 3. What's a Server Component? What are its benefits and limitations?

<details>
<summary>Reveal answer</summary>

A Server Component is a component that runs exclusively on the server and is never sent to the client's browser. Only the resulting UI is sent to the client.

This new paradigm was first introduced in Next.js and later became officially part of React in React 19.

In the App Router of a Next.js project, all components are Server Components by default. If you want to declare a Client Component, you have to explicitly add the `"use client"` directive.

**Benefits**

1. A Server Component can use sensitive logic and secrets because it's never sent to the client. For example, it can use database credentials and API keys to query the database. There is no risk of exposing sensitive information because Server Components are never bundled into the client-side Javascript.

2. Dependencies used exclusively by Server Components are never included in the client bundle, reducing the amount of Javascript downloaded by the browser.

3. Server Components can be asynchronous and fetch data directly without using `useEffect`.

4. Combined with Suspense, Server Components enable Streaming SSR. The server can progressively stream parts of the page as soon as they become ready instead of waiting for the slowest data fetch.

**Limitations**

1. There is no interactivity.

An important concept to understand is that Server Components never re-render. They execute once on the server to generate the UI. The concept of re-rendering only exists for components running in the browser.

Because of that, they cannot use a large part of React's API.

For example:

- They cannot use `useState` because state updates require re-rendering.
- They cannot use `useEffect` because effects execute on the client after rendering.
- They cannot use browser APIs such as `window` or `localStorage`.
- They cannot register event handlers like `onClick` or `onChange`.
- They cannot consume React Context with `useContext`.

2. Server Components can render Client Components but can only pass serializable props because those props must cross the network boundary.

</details>

---

#### 4. What's a Client Component? What are its benefits and limitations?

<details>
<summary>Reveal answer</summary>

A Client Component is a standard React component.

The only difference is that in the App Router, Client Components must be declared using the `"use client"` directive.

**Benefits**

1. They support interactivity through event handlers such as `onClick` and `onChange`.

2. They can manage state and lifecycle using hooks such as `useState` and `useEffect`.

3. They can use browser APIs such as `window` and `localStorage`.

4. They can consume React Context using `useContext`.

**Limitations**

These benefits come with trade-offs.

1. Their code and dependencies must be bundled and downloaded by the browser.

2. They cannot directly access secrets or query the database.

3. They cannot import Server Components.

</details>

---

#### 5. How do Client Components interact with Server Components?

<details>
<summary>Reveal answer</summary>

Client Components can import Client Components.

Server Components can import Server Components.

A Server Component can also import a Client Component.

However, a Client Component cannot import a Server Component because everything imported by a Client Component becomes part of the client bundle, while Server Components never run in the browser.

A common workaround is for a Server Component to pass another Server Component as `children` or props to a Client Component. The nested Server Component is still rendered on the server before being inserted into the Client Component.

</details>

---

#### 6. Where should you fetch data in Next.js?

<details>
<summary>Reveal answer</summary>

TODO

</details>

---

#### 7. Why is fetching data in a Server Component often better than using useEffect?

<details>
<summary>Reveal answer</summary>

TODO

</details>

---

#### 8. Explain the concept of request waterfalls.

<details>
<summary>Reveal answer</summary>

TODO

</details>

---

#### 9. What's Suspense?

<details>
<summary>Reveal answer</summary>

TODO

**NB:**

- In general, it's good practice to move your data fetches down to the components that need it, and then wrap those components in `Suspense`.

</details>

---

#### 10. What's Streaming?

<details>
<summary>Reveal answer</summary>

TODO

</details>

---

#### 11. What are React Server Actions?

<details>
<summary>Reveal answer</summary>

TODO

</details>

---

#### 12. What's a Route Handler?

<details>
<summary>Reveal answer</summary>

TODO

</details>

---

#### 13. How does a request flow from the browser to the database?

<details>
<summary>Reveal answer</summary>

TODO

</details>

---

#### 14. What's a Route Group?

<details>
<summary>Reveal answer</summary>

TODO

</details>