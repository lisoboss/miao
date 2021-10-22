#!/usr/bin/env python
# -*- coding: utf-8 -*-

from signal import (
    signal,
    SIGINT,
    SIGTERM
)
from engine import Engine


e = Engine()

def _exit(*_):
    e.stop()
    print('Exiting...')


signal(SIGINT, _exit)
signal(SIGTERM, _exit)

e.run()

print('Exit over!!!')

