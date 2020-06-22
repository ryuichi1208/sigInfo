#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <errno.h>

#ifdef DEBUG
#define SLEEP_TIME 30
#endif
#ifndef DEBUG
#define SLEEP_TIME 1
#endif

#ifndef _CONSOLE
#define unsigne long long u64
#define swap(type,a,b)  {type tmp=a;a=b;b=tmp;}w
#endif

unsigned int SIGNAL_ARR[] = {
    SIGHUP,
    SIGINT,
    SIGQUIT,
    SIGILL,
    SIGTRAP,
    SIGABRT,
    SIGBUS,
    SIGFPE,
    SIGKILL,
    SIGUSR1,
    SIGSEGV,
    SIGUSR2,
    SIGPIPE,
    SIGALRM,
    SIGTERM,
#if defined (__linux__) || defined (__linux) || defined (__unix)
    SIGSTKFLT,
#endif
    SIGCHLD,
    SIGCONT,
    SIGSTOP,
    SIGTSTP,
    SIGTTIN,
    SIGTTOU,
    SIGURG,
    SIGXCPU,
    SIGXFSZ,
    SIGVTALRM,
    SIGPROF,
    SIGWINCH,
#if defined (__linux__) || defined (__linux) || defined (__unix)
    SIGIO,
    SIGPWR,
#endif
    SIGSYS,
};

typedef void (*__sighandler_t)(int);

void print_proc_info()
{
    pid_t c_pid = getpid();
    pid_t p_pid = getppid();

    fprintf(stdout, "%d %d\n", c_pid, p_pid);
}

void signal_mask(sigset_t *set)
{
    // シグナル集合を空にし、SIGINT 追加
    sigemptyset(set);

    for (int i = 0; i < sizeof(SIGNAL_ARR)/sizeof(*SIGNAL_ARR); i++) {
        if (sigaddset(set, *(SIGNAL_ARR + i)))
            fprintf(stderr, "[FAILED] Signal = %d  errno =%d", *(SIGNAL_ARR + 1), errno);
    }
    sigprocmask(SIG_BLOCK, set, NULL);

}

int main(void)
{
    print_proc_info();
    sigset_t set;
    signal_mask(&set);
    sleep(SLEEP_TIME);

    // SIGINT のブロックを解除する
    sigprocmask(SIG_UNBLOCK, &set, NULL);

    fprintf(stdout, "Done !\n");

    return 0;
}
