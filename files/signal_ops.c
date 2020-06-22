#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <errno.h>

#define unsigne long long u64
#define SLEEP_TIME 1

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
    SIGSTKFLT,
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
    SIGIO,
    SIGPWR,
    SIGSYS,
};

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
    sigset_t set;
    signal_mask(&set);
    sleep(SLEEP_TIME);

    // SIGINT のブロックを解除する
    sigprocmask(SIG_UNBLOCK, &set, NULL);

    fprintf(stdout, "Done !\n");

    return 0;
}
