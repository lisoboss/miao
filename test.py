#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import json
from plug.miaomiao import MiaoMiao


if __name__ == "__main__":
    
    m = MiaoMiao()
    print(m._server_time)
    print(int(time.time() * 1000))
    # for rq in m.iter():
        # print(json.dumps(rq))



