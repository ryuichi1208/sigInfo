#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

from argparse import ArgumentParser

SIGNAL_NUNMBER = (
    "SIGHUP",
    "SIGQUIT",
    "SIGILL",
    "SIGTRAP",
    "SIGABRT",
    "SIGIOT",
    "SIGBUS",
    "SIGFPE",
    "SIGKILL",
    "SIGUSR1",
    "SIGSEGV",
    "SIGUSR2",
    "SIGPIPE",
    "SIGALRM",
    "SIGTERM",
    "SIGSTKFLT",
    "SIGCHLD",
    "SIGCONT",
    "SIGSTOP",
    "SIGTSTP",
    "SIGTTIN",
    "SIGTTOU",
    "SIGURG",
    "SIGXCPU",
    "SIGXFSZ",
    "SIGVTALRM",
    "SIGPROF",
    "SIGWINCH",
    "SIGIO",
    "SIGPOLL",
    "SIGPWR",
    "SIGSYS",
    "SIGRTMIN",
)

class ProcInfo(object):
    def __init__(self, name, pid, ppid, fdsize):
        self.name = name
        self.pid = pid
        self.ppid = ppid
        self.fdsize = fdsize


def opt_parse(args):
    """
    オプション解析
    """
    usage = f"Usage: {__file__}"
    argparser = ArgumentParser(usage=usage)
    argparser.add_argument(
        "-f", "--file", type=str, dest="pidf_ile", help="concatnate target file name"
    )
    return argparser.parse_args()


def extract_rows(file_name: str) -> dict:
    """
    procファイルから必要な行だけを抽出して辞書を生成
    """
    try:
        with open(file_name, mode="r", buffering=-1, closefd=True) as f:
            er = dict(
                [
                    l.strip().split("\t")
                    for l in f
                    if l.startswith("Sig") and not l.startswith("SigQ")
                ]
            )
            # 2進数へ変換
            for k, v in er.items():
                er[k] = format(int(v, 16), "b")
            return er
    except Exception as e:
        print(e)
        sys.exit(255)


def print_sig_info(er: dict):
    """
    取得した情報から各シグナルの情報を表示
    """
    for k, v in er.items():
        print(k, end=" ")
        rv = v[::-1]
        for i, b in enumerate(rv):
            if int(rv[i]):
                print(SIGNAL_NUNMBER[i], end=" ")
        print()


def main(args):
    er = extract_rows(args.pidf_ile)
    print_sig_info(er)


if __name__ == "__main__":
    main(opt_parse(sys.argv))
