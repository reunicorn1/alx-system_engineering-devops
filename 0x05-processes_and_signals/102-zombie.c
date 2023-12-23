#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

/**
 * infinite_while - create an infinite while loop
 *
 * Return: Always 0.
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - creates zombie processes
 *
 * Return: Always 0.
 */

int main(void)
{
	int i;
	pid_t pid = 1;

	for (i = 0; i < 5; i++)
	{
		if (pid > 0)
			pid = fork();
		if (pid == 0)
		{
			printf("Zombie process created, PID: %i\n", getpid());
			exit(0);
		}
	}
	infinite_while();
}
