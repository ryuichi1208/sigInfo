
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import siginfo

def test_gen_pid_file():
    assert siginfo.gen_pid_file(0) == None
    assert siginfo.gen_pid_file(99999) == None
