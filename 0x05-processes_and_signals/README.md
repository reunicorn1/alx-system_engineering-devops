# 0x05. Processes and signals

## Introduction

In Linux and Unix-like operating systems, a process is an instance of a running program. Each process has a unique identifier called a Process ID (PID). Processes can spawn child processes, creating a parent-child relationship between processes.

Signals are a form of communication between processes in Unix and Linux systems. They are software interrupts that provide a way to handle asynchronous events. For example, the system sends a signal to a process when the user presses Ctrl+C.

There are various types of signals. Some common ones include:

-   SIGINT: The interrupt signal, which is sent when a user types Ctrl+C. This signal causes the process to terminate.
-   SIGKILL: This signal immediately terminates the process and cannot be caught or ignored.
-   SIGSTOP: This signal pauses the process.
-   SIGCONT: This signal resumes a paused process.

In Bash, you can use commands like  `kill`  to send signals to processes. For example,  `kill -SIGINT [pid]`  would send the SIGINT signal to the process with the given PID.

## Tasks/Files

  
|     Tasks           |Files                       |
|----------------|-------------------------------|
|0. What is my PID|``0-what-is-my-pid``            |
|1. List your processes|`1-list_your_processes`            |
|2. Show your Bash PID|`2-show_your_bash_pid`|
|3. Show your Bash PID made easy|`3-show_your_bash_pid_made_easy`|
|4. To infinity and beyond|`4-to_infinity_and_beyond`|
|5. Don't stop me now!|``5-dont_stop_me_now``|
|6. Stop me if you can|`6-stop_me_if_you_can`|
|7. Highlander|`7-highlander`|
|8. Beheaded process|`8-beheaded_process`|
