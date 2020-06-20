#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

from functools import lru_cache
from argparse import ArgumentParser

SIGNAL_NUNMBER = (
    "SIGHUP",  # ハングアップ
    "SIGQUIT",  # 終了とコアダンプ
    "SIGILL",  # 不正命令
    "SIGTRAP",  # トレース/ブレークポイントによるトラップ
    "SIGABRT",  # プロセスが中断された
    "SIGIOT",  # IOT 命令
    "SIGBUS",  # 「未定義メモリ領域へのアクセス」(SUS)によるバスエラー
    "SIGFPE",  # 浮動小数点例外 -- 「不正な算術操作」(SUS)
    "SIGKILL",  # Kill シグナル
    "SIGUSR1",  # ユーザー定義シグナル 1
    "SIGSEGV",  # 不正なメモリー参照
    "SIGUSR2",  # ユーザー定義シグナル 2
    "SIGPIPE",  #
    "SIGALRM",  # alarm() によるシグナル
    "SIGTERM",  #
    "SIGSTKFLT",  # 数値演算プロセッサにおけるスタックフォルト
    "SIGCHLD",  # 子プロセスが終了、停止（または再開*）した
    "SIGCONT",  #
    "SIGSTOP",  #
    "SIGTSTP",  #
    "SIGTTIN",  # バックグランドプロセスの端末入力
    "SIGTTOU",  # バックグランドプロセスの端末出力
    "SIGURG",  # ソケットの緊急事態 (urgent condition) (4.2BSD)
    "SIGXCPU",  # CPU時間制限超過 (4.2BSD)
    "SIGXFSZ",  #
    "SIGVTALRM",  #
    "SIGPROF",  # profiling タイマーの時間切れ
    "SIGWINCH",  #
    "SIGIO",  #
    "SIGPOLL",  #
    "SIGPWR",  # 電源喪失 (Power failure) (System V)
    "SIGSYS",  # ルーチンへの引き数が不正 (SVr4)
    "SIGRTMIN",  #
)


class ProcInfo(object):
    def __init__(self, name, pid, ppid, fdsize):
        self.name = name
        self.pid = pid
        self.ppid = ppid
        self.fdsize = fdsize


@lru_cache(maxsize=128, typed=False)
def gen_pid_file(pid: int) -> str:
    """
    対象のpidファイル名を生成して文字列でリターン
    """
    file_name = f"/proc/{pid}/status"
    return file_name if os.path.isfile(file_name) else None


def opt_parse(args: list):
    """
    オプション解析
    """
    usage = f"Usage: {__file__}"
    argparser = ArgumentParser(usage=usage)
    argparser.add_argument(
        "-f", "--file", type=str, dest="pid_file", help="concatnate target file name"
    )
    argparser.add_argument(
        "-p", "--pid", type=int, dest="pidf", help="concatnate target pid"
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


def main(args: list):
    er = extract_rows(args.pid_file)
    print_sig_info(er)


if __name__ == "__main__":
    main(opt_parse(sys.argv))
