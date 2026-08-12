// What's the issue with this code and how to fix it?

async function notifyUsers(userIds) {
    userIds.forEach(async (id) => {
      await sendEmail(id);
    });
    console.log("All emails sent");
  }