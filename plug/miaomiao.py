#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import copy
from time import (
    sleep,
)
from datetime import (
    datetime,
)
from hashlib import md5
import urllib3
import requests as rs
import settings


class MiaoMiao:

    URLS = {
        # 服务器当前时间戳
        "SERVER_TIME": "https://miaomiao.scmttec.com/seckill/seckill/now2.do",
        # 疫苗列表
        "VACCINE_LIST": "https://miaomiao.scmttec.com/seckill/seckill/list.do",
        # 校验库存
        "CHECK_STOCK": "https://miaomiao.scmttec.com/seckill/seckill/checkstock2.do",
        # 接种人信息
        "USER_INFO": "https://miaomiao.scmttec.com/seckill/linkman/findByUserId.do",
        # 秒杀疫苗
        "SEC_KILL": "https://miaomiao.scmttec.com/seckill/seckill/subscribe.do"
    }

    # common headers
    REQ_HEADERS = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 7.1.2; SHARK KLE-A0 Build/NZH54D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2899 MMWEBSDK/20210601 Mobile Safari/537.36 MMWEBID/1363 MicroMessenger/8.0.10.1960(0x28000A3D) Process/appbrand0 WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "Referer": "https://servicewechat.com/wxff8cad2e9bf18719/21/page-frame.html",
        "Accept": "application/json, text/plain, */*",
    }

    # ecc_hs盐
    ECC_HS_SALT = 'ux$ad70*b'

    def __init__(self):
        self.running = True
        self._user_name = settings.user_name
        self._tk = settings.miaomiao_tk
        self._cookie = settings.miaomiao_cookie
        self._region_codes = settings.region_codes
        self.f = open('./miao.log', 'a+', encoding='utf-8')
        # 
        urllib3.disable_warnings()
        # init user info
        self._user_id = None
        for user in self._get_users():
            if user.get('name') == self._user_name:
                self._user_id = user.get('id')
                self._user_card = user.get('idCardNo')
                break
        if not self._user_id:
            print('init user info err not fund', self._user_name)
            exit(-1)

    @property
    def _headers(self):
        headers = copy.deepcopy(self.REQ_HEADERS)
        headers.update(dict(
            tk=self._tk,
            Cookie=self._cookie
        ))
        return headers

    def _get(self, url, params=None, **kwargs) -> dict:
        sleep(0.3)
        kwargs.update(dict(
            verify=False
        ))
        try:
            rp = rs.get(url, params=params, **kwargs)
            rp.raise_for_status()
            return rp.json()
        except Exception as e:
            print(url, e)
        return {}
    
    @property 
    def _server_time(self) -> int:
        return self._get(self.URLS.get('SERVER_TIME')).get('data') or 0

    def _get_users(self) -> list[dict]:
        data = self._get(self.URLS.get('USER_INFO'), headers=self._headers)
        if '0000' != data.get('code'):
            print('get_user err', data)
            exit(-1)
        return data.get('data') or [{}]

    def _get_vaccine_list(self):
        for region_code in self._region_codes:
            print('get_vaccine_list:', region_code)
            params = {'offset': '0', 'limit': '10', 'regionCode': region_code}
            data = self._get(self.URLS.get('VACCINE_LIST'), params=params, headers=self._headers)
            if '0000' != data.get('code'):
                print('get_vaccine_list err', data)
                continue
            for d in data.get('data') or [{}]:
                yield d

    def _build_skill_request(self, v):
        start_time = int(datetime.strptime(v.get('startTime') or '', '%Y-%m-%d %H:%M:%S').timestamp() * 1000)
        seckill_id = v.get('id')
        #
        url = self.URLS.get('SEC_KILL') or ''
        # 
        params = {
            'vaccineIndex': '1', 
            'seckillId': seckill_id, 
            'linkmanId': self._user_id, 
            'idCardNo': self._user_card, 
            'startTimeUnx': start_time + 1
        }
        # 
        headers = self._headers
        _strings = '%s%s%s' % (seckill_id, self._user_id, start_time + 1)
        _ori_md5 = md5(_strings.encode('utf-8')).hexdigest()
        _strings = '%s%s' % (_ori_md5, self.ECC_HS_SALT)
        _md5_salt = md5(_strings.encode('utf-8'))
        headers['ecc-hs'] = _md5_salt.hexdigest()
        return dict(
            start_time=start_time,
            url=url,
            method='GET',
            headers=headers,
            params=params,
            data=None,
            json=None,
            ret=dict(
                http_code=200,
                json_key='code',
                json_value='0000'
            )
        )


    def iter(self):
        while self.running:
            for d in self._get_vaccine_list():
                if d:
                    if d.get('stock') and d.get("vaccineCode") == "8803":
                        yield self._build_skill_request(d)
                    else:
                        print(d, file=self.f) 
            s = 60
            print('sleep: %ss' % s)
            if not self.running:
                break
            sleep(s)
        
    


    




