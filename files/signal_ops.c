#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>

int main(void)
{
    unsigned int sec = 10;
    sigset_t set;
    pid_t c_pid = getpid();

    fprintf(stdout, "%d\n", c_pid);

    // シグナル集合を空にし、SIGINT 追加
    //sigemptyset(&set);
    //sigaddset(&set, SIGINT);
    //sigaddset(&set, SIGHUP);
    //sigaddset(&set, SIGQUIT);
    //sigaddset(&set, SIGILL);
    //sigaddset(&set, SIGTRAP);
    //sigaddset(&set, SIGABRT);
    //sigaddset(&set, SIGBUS);
    //sigaddset(&set, SIGFPE);
    //sigaddset(&set, SIGUSR1);

    // SIGINT をブロック (保留) する
    sigprocmask(SIG_BLOCK, &set, NULL);
    printf("Block the SIGINT for %d sec\n", sec);

    sleep(sec);

    // SIGINT のブロックを解除する
    printf("\nPassed %d sec, unblock the SIGINT\n", sec);
    sigprocmask(SIG_UNBLOCK, &set, NULL);

    printf("Done !\n");

    return 0;
}
