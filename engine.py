#!/usr/bin/env python
# -*- coding: utf-8 -*-


from plug.miaomiao import MiaoMiao
from pool_by_asyncio import Pool


class Engine:

    def __init__(self):
        self.m = MiaoMiao()
        self.pool = []

    def stop(self):
        self.m.running = False
        for p in self.pool:
            p.running = False
    
    def _miao_kill(self, data):
        p = Pool(data)
        self.pool.append(p)
        p.run()

    def run(self):
        for d in self.m.iter():
            self._miao_kill(d)
            
            
