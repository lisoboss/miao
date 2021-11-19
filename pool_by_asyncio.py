#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio
from logging import getLogger
from time import time
from aiohttp import (
    ClientSession,
    TCPConnector,
)


LOG = getLogger(__name__)


class Pool:

    def __init__(self, rq: dict, max_workers=50):
        self.rq = rq
        self.max_workers = max_workers
        self.running = True
        self.f = open('./pool.log', 'a+', encoding='utf-8')

    async def async_sub_worker(self):
        target = self.rq.get('ret') or {}
        target_time = (self.rq.get('start_time') or 0)
        while self.running:
            start_time = target_time - int(time() * 1000)
            if start_time < -10:
                break
            if start_time > 1000:
                await asyncio.sleep(0.3)
                continue
            try:
                async with ClientSession(connector=TCPConnector(ssl=False)) as se:
                    async with se.request(
                        method=self.rq.get('method', ''),
                        url=self.rq.get('url', ''),
                        headers=self.rq.get('headers'),
                        data=self.rq.get('data'),
                        json=self.rq.get('json'),
                        params=self.rq.get('params'),
                        timeout=self.rq.get('timeout') or 30,
                        ssl=False,
                        proxy='',
                    ) as rp:
                        status = rp.status
                        if status == 200:
                            data = await rp.json()
                            if data.get(target.get('json_key') or '') == target.get('json_value'):
                                self.running = False
                                print('ok ok ok ok ok ok ok ok ok')
                                print('ok ok ok ok ok ok ok ok ok', file=self.f)
                            else:
                                print(start_time, status, data, file=self.f)
                        else:
                            text = await rp.text()
                            print(start_time, status, text, file=self.f)
            except Exception as e:
                print(e)
                print(e, file=self.f)

    async def async_worker(self):
        await asyncio.gather(
            *[asyncio.create_task(self.async_sub_worker()) for _ in range(self.max_workers)]
        )

    def worker(self):
        asyncio.run(self.async_worker(), debug=False)

    def run(self):
        self.worker()


