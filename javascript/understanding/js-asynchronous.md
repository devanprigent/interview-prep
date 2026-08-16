investigation: asynchronous execution overview in Javascript

Standard Javascript code has two important properties:
1) It is single-threaded - one line runs at a time.
2) It is synchronous - the lines are read and executed in the order they appear.

It makes the code predictable and easy to understand. You execute a line and waits it finishes before executing the next one in the file.

The issue with this approach is that it's not adapted to modern web. 

What if you want to fetch a video from a distant server that could take seconds before appearing ? With the synchronous approach, the entire application is frozen until the video is received. 

That's the issue with having a single thread executing synchronous code: a long task will block it and prevent other tasks from being executed.

For that reason, Javascript alone is not enough and we need more tools to make it work.

