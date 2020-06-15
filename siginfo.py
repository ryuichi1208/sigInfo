#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

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
    "SIGPIPE",  # 読み手の無いパイプへの書き出し
    "SIGALRM",  # alarm() によるシグナル
    "SIGTERM",  # 終了 (termination) シグナル
    "SIGSTKFLT",  # 数値演算プロセッサにおけるスタックフォルト
    "SIGCHLD",  # 子プロセスが終了、停止（または再開*）した
    "SIGCONT",  # Cont	一時停止 (stop) からの再開
    "SIGSTOP",  # プロセスの一時停止
    "SIGTSTP",  # 端末より入力された一時停止
    "SIGTTIN",  # バックグランドプロセスの端末入力
    "SIGTTOU",  # バックグランドプロセスの端末出力
    "SIGURG",  # ソケットの緊急事態 (urgent condition) (4.2BSD)
    "SIGXCPU",  # CPU時間制限超過 (4.2BSD)
    "SIGXFSZ",  # ファイルサイズ制限の超過
    "SIGVTALRM",  # 仮想アラームクロック
    "SIGPROF",  # profiling タイマーの時間切れ
    "SIGWINCH",  # ウィンドウ リサイズ シグナル (4.3BSD, Sun)
    "SIGIO",  # 入出力が可能になった (4.2BSD)
    "SIGPOLL",  # Term	ポーリング可能なイベント (Sys V)
    "SIGPWR",  # 電源喪失 (Power failure) (System V)
    "SIGSYS",  # ルーチンへの引き数が不正 (SVr4)
    "SIGRTMIN",  #
    "SIGRTMIN+1",  #
    "SIGRTMIN+2",  #
    "SIGRTMIN+3",  #
    "SIGRTMIN+4",  #
    "SIGRTMIN+5",  #
    "SIGRTMIN+6",  #
    "SIGRTMIN+7",  #
    "SIGRTMIN+8",  #
    "SIGRTMIN+9",  #
    "SIGRTMIN+10",  #
    "SIGRTMIN+11",  #
    "SIGRTMIN+12",  #
    "SIGRTMIN+13",  #
    "SIGRTMIN+14",  #
    "SIGRTMIN+15",  #
    "SIGRTMAX-14",  #
    "SIGRTMAX-13",  #
    "SIGRTMAX-12",  #
    "SIGRTMAX-11",  #
    "SIGRTMAX-10",  #
    "SIGRTMAX-9",  #
    "SIGRTMAX-8",  #
    "SIGRTMAX-7",  #
    "SIGRTMAX-6",  #
    "SIGRTMAX-5",  #
    "SIGRTMAX-4",  #
    "SIGRTMAX-3",  #
    "SIGRTMAX-2",  #
    "SIGRTMAX-1",  #
    "SIGRTMAX",  #
)


class ProcInfo(object):
    def __init__(self, name, pid, ppid, fdsize):
        self.name = name
        self.pid = pid
        self.ppid = ppid
        self.fdsize = fdsize


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


def signal_doc():
    doc = """
* The job control signals also have other special effects.
*
*»-----+--------------------+------------------+
*»-----|  POSIX signal      |  default action  |
*»-----+--------------------+------------------+
*»-----|  SIGHUP            |  terminate»------|
*»-----|  SIGINT            |»-terminate»------|
*»-----|  SIGQUIT           |»-coredump »------|
*»-----|  SIGILL            |»-coredump »------|
*»-----|  SIGTRAP           |»-coredump »------|
*»-----|  SIGABRT/SIGIOT    |»-coredump »------|
*»-----|  SIGBUS            |»-coredump »------|
*»-----|  SIGFPE            |»-coredump »------|
*»-----|  SIGKILL           |»-terminate(+)»---|
*»-----|  SIGUSR1           |»-terminate»------|
*»-----|  SIGSEGV           |»-coredump »------|
*»-----|  SIGUSR2           |»-terminate»------|
*»-----|  SIGPIPE           |»-terminate»------|
*»-----|  SIGALRM           |»-terminate»------|
*»-----|  SIGTERM           |»-terminate»------|
*»-----|  SIGCHLD           |»-ignore   »------|
*»-----|  SIGCONT           |»-ignore(*)»------|
*»-----|  SIGSTOP           |»-stop(*)(+)  »---|
*»-----|  SIGTSTP           |»-stop(*)  »------|
*»-----|  SIGTTIN           |»-stop(*)  »------|
*»-----|  SIGTTOU           |»-stop(*)  »------|
*»-----|  SIGURG            |»-ignore   »------|
*»-----|  SIGXCPU           |»-coredump »------|
*»-----|  SIGXFSZ           |»-coredump »------|
*»-----|  SIGVTALRM         |»-terminate»------|
*»-----|  SIGPROF           |»-terminate»------|
*»-----|  SIGPOLL/SIGIO     |»-terminate»------|
*»-----|  SIGSYS/SIGUNUSED  |»-coredump »------|
*»-----|  SIGSTKFLT         |»-terminate»------|
*»-----|  SIGWINCH          |»-ignore   »------|
*»-----|  SIGPWR            |»-terminate»------|
*»-----|  SIGRTMIN-SIGRTMAX |»-terminate       |
*»-----+--------------------+------------------+
*»-----|  non-POSIX signal  |  default action  |
*»-----+--------------------+------------------+
*»-----|  SIGEMT            |  coredump»-------|
*»-----+--------------------+------------------+

(+) For SIGKILL and SIGSTOP the action is "always", not just "default".
    """

    enf_sampla_format = """
00000000280b2603 ==> 101000000010110010011000000011
                     | |       | ||  |  ||       |`->  1 = SIGHUP
                     | |       | ||  |  ||       `-->  2 = SIGINT
                     | |       | ||  |  |`----------> 10 = SIGUSR1
                     | |       | ||  |  `-----------> 11 = SIGSEGV
                     | |       | ||  `--------------> 14 = SIGALRM
                     | |       | |`-----------------> 17 = SIGCHLD
                     | |       | `------------------> 18 = SIGCONT
                     | |       `--------------------> 20 = SIGTSTP
                     | `----------------------------> 28 = SIGWINCH
                     `------------------------------> 30 = SIGPWR
    """


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
    if args.pid_file:
        er = extract_rows(args.pid_file)
    else:
        er = extract_rows(gen_pid_file(args.pidf))
    print_sig_info(er)


if __name__ == "__main__":
    main(opt_parse(sys.argv))
