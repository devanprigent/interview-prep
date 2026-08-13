// What's the issue with this code and how to fix it?

async function notifyUsers(userIds) {
    userIds.forEach(async (id) => {
      await sendEmail(id);
    });
    console.log("All emails sent");
  }

/*
SOLUTION

The issue is that forEach ignores the Promises. It doesn't wait for any of them.

As a result, the message "All emails sent" might be logged before any message are

actually sent.

There are several solutions.

Either you use a for loop instead which does wait for the promises and will send the 

request one by one:

for (let i=0; i<userIds.length; i++){
  await sendEmail(userIds[i]);
}
console.log("All emails sent");

Or if you want to send all the requests in parallel and wait for all to return, you can 

`Promise.all`:  

async function notifyUsers(userIds) {
  await Promise.all(userIds.map(id => sendEmail(id)));
  console.log("All emails sent");
}

*/