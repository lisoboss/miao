#!/usr/bin/env python
# -*- coding: utf-8 -*-


user_name = ''

miaomiao_tk = ''
miaomiao_cookie = '_xzkj_=' + miaomiao_tk

region_codes = [
    5101,  # 成都
]


_region_codes = [
    110101,  # 北京市 东城区
    110102,  # 北京市 西城区
    110105,  # 北京市 朝阳区
    110106,  # 北京市 丰台区
    110107,  # 北京市 石景山区
    110108,  # 北京市 海淀区
    110109,  # 北京市 门头沟区
    110111,  # 北京市 房山区
    110112,  # 北京市 通州区
    110113,  # 北京市 顺义区
    110114,  # 北京市 昌平区
    110115,  # 北京市 大兴区
    110116,  # 北京市 怀柔区
    110117,  # 北京市 平谷区
    110118,  # 北京市 密云区
    110119,  # 北京市 延庆区
    120101,  # 天津市 和平区
    120102,  # 天津市 河东区
    120103,  # 天津市 河西区
    120104,  # 天津市 南开区
    120105,  # 天津市 河北区
    120106,  # 天津市 红桥区
    120110,  # 天津市 东丽区
    120111,  # 天津市 西青区
    120112,  # 天津市 津南区
    120113,  # 天津市 北辰区
    120114,  # 天津市 武清区
    120115,  # 天津市 宝坻区
    120116,  # 天津市 滨海新区
    120117,  # 天津市 宁河区
    120118,  # 天津市 静海区
    120225,  # 天津市 蓟州区
    1301,  # 河北省 石家庄市
    1302,  # 河北省 唐山市
    1303,  # 河北省 秦皇岛市
    1304,  # 河北省 邯郸市
    1305,  # 河北省 邢台市
    1306,  # 河北省 保定市
    1307,  # 河北省 张家口市
    1308,  # 河北省 承德市
    1309,  # 河北省 沧州市
    1310,  # 河北省 廊坊市
    1311,  # 河北省 衡水市
    1390,  # 河北省 省直辖县级行政区划
    1401,  # 山西省 太原市
    1402,  # 山西省 大同市
    1403,  # 山西省 阳泉市
    1404,  # 山西省 长治市
    1405,  # 山西省 晋城市
    1406,  # 山西省 朔州市
    1407,  # 山西省 晋中市
    1408,  # 山西省 运城市
    1409,  # 山西省 忻州市
    1410,  # 山西省 临汾市
    1411,  # 山西省 吕梁市
    1501,  # 内蒙古自治区 呼和浩特市
    1502,  # 内蒙古自治区 包头市
    1503,  # 内蒙古自治区 乌海市
    1504,  # 内蒙古自治区 赤峰市
    1505,  # 内蒙古自治区 通辽市
    1506,  # 内蒙古自治区 鄂尔多斯市
    1507,  # 内蒙古自治区 呼伦贝尔市
    1508,  # 内蒙古自治区 巴彦淖尔市
    1509,  # 内蒙古自治区 乌兰察布市
    1522,  # 内蒙古自治区 兴安盟
    1525,  # 内蒙古自治区 锡林郭勒盟
    1529,  # 内蒙古自治区 阿拉善盟
    2101,  # 辽宁省 沈阳市
    2102,  # 辽宁省 大连市
    2103,  # 辽宁省 鞍山市
    2104,  # 辽宁省 抚顺市
    2105,  # 辽宁省 本溪市
    2106,  # 辽宁省 丹东市
    2107,  # 辽宁省 锦州市
    2108,  # 辽宁省 营口市
    2109,  # 辽宁省 阜新市
    2110,  # 辽宁省 辽阳市
    2111,  # 辽宁省 盘锦市
    2112,  # 辽宁省 铁岭市
    2113,  # 辽宁省 朝阳市
    2114,  # 辽宁省 葫芦岛市
    2201,  # 吉林省 长春市
    2202,  # 吉林省 吉林市
    2203,  # 吉林省 四平市
    2204,  # 吉林省 辽源市
    2205,  # 吉林省 通化市
    2206,  # 吉林省 白山市
    2207,  # 吉林省 松原市
    2208,  # 吉林省 白城市
    2224,  # 吉林省 延边朝鲜族自治州
    2301,  # 黑龙江省 哈尔滨市
    2302,  # 黑龙江省 齐齐哈尔市
    2303,  # 黑龙江省 鸡西市
    2304,  # 黑龙江省 鹤岗市
    2305,  # 黑龙江省 双鸭山市
    2306,  # 黑龙江省 大庆市
    2307,  # 黑龙江省 伊春市
    2308,  # 黑龙江省 佳木斯市
    2309,  # 黑龙江省 七台河市
    2310,  # 黑龙江省 牡丹江市
    2311,  # 黑龙江省 黑河市
    2312,  # 黑龙江省 绥化市
    2327,  # 黑龙江省 大兴安岭地区
    310101,  # 上海市 黄浦区
    310104,  # 上海市 徐汇区
    310105,  # 上海市 长宁区
    310106,  # 上海市 静安区
    310107,  # 上海市 普陀区
    310108,  # 上海市 闸北区
    310109,  # 上海市 虹口区
    310110,  # 上海市 杨浦区
    310112,  # 上海市 闵行区
    310113,  # 上海市 宝山区
    310114,  # 上海市 嘉定区
    310115,  # 上海市 浦东新区
    310116,  # 上海市 金山区
    310117,  # 上海市 松江区
    310118,  # 上海市 青浦区
    310120,  # 上海市 奉贤区
    310151,  # 上海市 崇明区
    3201,  # 江苏省 南京市
    3202,  # 江苏省 无锡市
    3203,  # 江苏省 徐州市
    3204,  # 江苏省 常州市
    3205,  # 江苏省 苏州市
    3206,  # 江苏省 南通市
    3207,  # 江苏省 连云港市
    3208,  # 江苏省 淮安市
    3209,  # 江苏省 盐城市
    3210,  # 江苏省 扬州市
    3211,  # 江苏省 镇江市
    3212,  # 江苏省 泰州市
    3213,  # 江苏省 宿迁市
    3301,  # 浙江省 杭州市
    3302,  # 浙江省 宁波市
    3303,  # 浙江省 温州市
    3304,  # 浙江省 嘉兴市
    3305,  # 浙江省 湖州市
    3306,  # 浙江省 绍兴市
    3307,  # 浙江省 金华市
    3308,  # 浙江省 衢州市
    3309,  # 浙江省 舟山市
    3310,  # 浙江省 台州市
    3311,  # 浙江省 丽水市
    3401,  # 安徽省 合肥市
    3402,  # 安徽省 芜湖市
    3403,  # 安徽省 蚌埠市
    3404,  # 安徽省 淮南市
    3405,  # 安徽省 马鞍山市
    3406,  # 安徽省 淮北市
    3407,  # 安徽省 铜陵市
    3408,  # 安徽省 安庆市
    3410,  # 安徽省 黄山市
    3411,  # 安徽省 滁州市
    3412,  # 安徽省 阜阳市
    3413,  # 安徽省 宿州市
    3415,  # 安徽省 六安市
    3416,  # 安徽省 亳州市
    3417,  # 安徽省 池州市
    3418,  # 安徽省 宣城市
    3501,  # 福建省 福州市
    3502,  # 福建省 厦门市
    3503,  # 福建省 莆田市
    3504,  # 福建省 三明市
    3505,  # 福建省 泉州市
    3506,  # 福建省 漳州市
    3507,  # 福建省 南平市
    3508,  # 福建省 龙岩市
    3509,  # 福建省 宁德市
    3601,  # 江西省 南昌市
    3602,  # 江西省 景德镇市
    3603,  # 江西省 萍乡市
    3604,  # 江西省 九江市
    3605,  # 江西省 新余市
    3606,  # 江西省 鹰潭市
    3607,  # 江西省 赣州市
    3608,  # 江西省 吉安市
    3609,  # 江西省 宜春市
    3610,  # 江西省 抚州市
    3611,  # 江西省 上饶市
    3701,  # 山东省 济南市
    3702,  # 山东省 青岛市
    3703,  # 山东省 淄博市
    3704,  # 山东省 枣庄市
    3705,  # 山东省 东营市
    3706,  # 山东省 烟台市
    3707,  # 山东省 潍坊市
    3708,  # 山东省 济宁市
    3709,  # 山东省 泰安市
    3710,  # 山东省 威海市
    3711,  # 山东省 日照市
    3713,  # 山东省 临沂市
    3714,  # 山东省 德州市
    3715,  # 山东省 聊城市
    3716,  # 山东省 滨州市
    3717,  # 山东省 菏泽市
    4101,  # 河南省 郑州市
    4102,  # 河南省 开封市
    4103,  # 河南省 洛阳市
    4104,  # 河南省 平顶山市
    4105,  # 河南省 安阳市
    4106,  # 河南省 鹤壁市
    4107,  # 河南省 新乡市
    4108,  # 河南省 焦作市
    4109,  # 河南省 濮阳市
    4110,  # 河南省 许昌市
    4111,  # 河南省 漯河市
    4112,  # 河南省 三门峡市
    4113,  # 河南省 南阳市
    4114,  # 河南省 商丘市
    4115,  # 河南省 信阳市
    4116,  # 河南省 周口市
    4117,  # 河南省 驻马店市
    4190,  # 河南省 济源市
    4201,  # 湖北省 武汉市
    4202,  # 湖北省 黄石市
    4203,  # 湖北省 十堰市
    4205,  # 湖北省 宜昌市
    4206,  # 湖北省 襄阳市
    4207,  # 湖北省 鄂州市
    4208,  # 湖北省 荆门市
    4209,  # 湖北省 孝感市
    4210,  # 湖北省 荆州市
    4211,  # 湖北省 黄冈市
    4212,  # 湖北省 咸宁市
    4213,  # 湖北省 随州市
    4228,  # 湖北省 恩施土家族苗族自治州
    4290,  # 湖北省 省直辖县级行政区划
    4301,  # 湖南省 长沙市
    4302,  # 湖南省 株洲市
    4303,  # 湖南省 湘潭市
    4304,  # 湖南省 衡阳市
    4305,  # 湖南省 邵阳市
    4306,  # 湖南省 岳阳市
    4307,  # 湖南省 常德市
    4308,  # 湖南省 张家界市
    4309,  # 湖南省 益阳市
    4310,  # 湖南省 郴州市
    4311,  # 湖南省 永州市
    4312,  # 湖南省 怀化市
    4313,  # 湖南省 娄底市
    4331,  # 湖南省 湘西土家族苗族自治州
    4401,  # 广东省 广州市
    4402,  # 广东省 韶关市
    4403,  # 广东省 深圳市
    4404,  # 广东省 珠海市
    4405,  # 广东省 汕头市
    4406,  # 广东省 佛山市
    4407,  # 广东省 江门市
    4408,  # 广东省 湛江市
    4409,  # 广东省 茂名市
    4412,  # 广东省 肇庆市
    4413,  # 广东省 惠州市
    4414,  # 广东省 梅州市
    4415,  # 广东省 汕尾市
    4416,  # 广东省 河源市
    4417,  # 广东省 阳江市
    4418,  # 广东省 清远市
    4419,  # 广东省 东莞市
    4420,  # 广东省 中山市
    4451,  # 广东省 潮州市
    4452,  # 广东省 揭阳市
    4453,  # 广东省 云浮市
    4501,  # 广西壮族自治区 南宁市
    4502,  # 广西壮族自治区 柳州市
    4503,  # 广西壮族自治区 桂林市
    4504,  # 广西壮族自治区 梧州市
    4505,  # 广西壮族自治区 北海市
    4506,  # 广西壮族自治区 防城港市
    4507,  # 广西壮族自治区 钦州市
    4508,  # 广西壮族自治区 贵港市
    4509,  # 广西壮族自治区 玉林市
    4510,  # 广西壮族自治区 百色市
    4511,  # 广西壮族自治区 贺州市
    4512,  # 广西壮族自治区 河池市
    4513,  # 广西壮族自治区 来宾市
    4514,  # 广西壮族自治区 崇左市
    4601,  # 海南省 海口市
    4602,  # 海南省 三亚市
    4603,  # 海南省 三沙市
    4690,  # 海南省 省直辖县级行政区划
    500101,  # 重庆市 万州区
    500102,  # 重庆市 涪陵区
    500103,  # 重庆市 渝中区
    500104,  # 重庆市 大渡口区
    500105,  # 重庆市 江北区
    500106,  # 重庆市 沙坪坝区
    500107,  # 重庆市 九龙坡区
    500108,  # 重庆市 南岸区
    500109,  # 重庆市 北碚区
    500110,  # 重庆市 綦江区
    500111,  # 重庆市 大足区
    500112,  # 重庆市 渝北区
    500113,  # 重庆市 巴南区
    500114,  # 重庆市 黔江区
    500115,  # 重庆市 长寿区
    500116,  # 重庆市 江津区
    500117,  # 重庆市 合川区
    500118,  # 重庆市 永川区
    500119,  # 重庆市 南川区
    500120,  # 重庆市 璧山区
    500151,  # 重庆市 铜梁区
    500152,  # 重庆市 潼南区
    500153,  # 重庆市 荣昌区
    500154,  # 重庆市 开州区
    500155,  # 重庆市 梁平区
    500229,  # 重庆市 城口县
    500230,  # 重庆市 丰都县
    500231,  # 重庆市 垫江县
    500232,  # 重庆市 武隆区
    500233,  # 重庆市 忠县
    500234,  # 重庆市 开县
    500235,  # 重庆市 云阳县
    500236,  # 重庆市 奉节县
    500237,  # 重庆市 巫山县
    500238,  # 重庆市 巫溪县
    500240,  # 重庆市 石柱土家族自治县
    500241,  # 重庆市 秀山土家族苗族自治县
    500242,  # 重庆市 酉阳土家族苗族自治县
    500243,  # 重庆市 彭水苗族土家族自治县
    5101,  # 四川省 成都市
    5103,  # 四川省 自贡市
    5104,  # 四川省 攀枝花市
    5105,  # 四川省 泸州市
    5106,  # 四川省 德阳市
    5107,  # 四川省 绵阳市
    5108,  # 四川省 广元市
    5109,  # 四川省 遂宁市
    5110,  # 四川省 内江市
    5111,  # 四川省 乐山市
    5113,  # 四川省 南充市
    5114,  # 四川省 眉山市
    5115,  # 四川省 宜宾市
    5116,  # 四川省 广安市
    5117,  # 四川省 达州市
    5118,  # 四川省 雅安市
    5119,  # 四川省 巴中市
    5120,  # 四川省 资阳市
    5132,  # 四川省 阿坝藏族羌族自治州
    5133,  # 四川省 甘孜藏族自治州
    5134,  # 四川省 凉山彝族自治州
    5201,  # 贵州省 贵阳市
    5202,  # 贵州省 六盘水市
    5203,  # 贵州省 遵义市
    5204,  # 贵州省 安顺市
    5205,  # 贵州省 毕节市
    5206,  # 贵州省 铜仁市
    5223,  # 贵州省 黔西南布依族苗族自治州
    5226,  # 贵州省 黔东南苗族侗族自治州
    5227,  # 贵州省 黔南布依族苗族自治州
    5301,  # 云南省 昆明市
    5303,  # 云南省 曲靖市
    5304,  # 云南省 玉溪市
    5305,  # 云南省 保山市
    5306,  # 云南省 昭通市
    5307,  # 云南省 丽江市
    5308,  # 云南省 普洱市
    5309,  # 云南省 临沧市
    5323,  # 云南省 楚雄彝族自治州
    5325,  # 云南省 红河哈尼族彝族自治州
    5326,  # 云南省 文山壮族苗族自治州
    5328,  # 云南省 西双版纳傣族自治州
    5329,  # 云南省 大理白族自治州
    5331,  # 云南省 德宏傣族景颇族自治州
    5333,  # 云南省 怒江傈僳族自治州
    5334,  # 云南省 迪庆藏族自治州
    5401,  # 西藏自治区 拉萨市
    5402,  # 西藏自治区 日喀则市
    5403,  # 西藏自治区 昌都市
    5404,  # 西藏自治区 林芝市
    5422,  # 西藏自治区 山南地区
    5424,  # 西藏自治区 那曲地区
    5425,  # 西藏自治区 阿里地区
    6101,  # 陕西省 西安市
    6102,  # 陕西省 铜川市
    6103,  # 陕西省 宝鸡市
    6104,  # 陕西省 咸阳市
    6105,  # 陕西省 渭南市
    6106,  # 陕西省 延安市
    6107,  # 陕西省 汉中市
    6108,  # 陕西省 榆林市
    6109,  # 陕西省 安康市
    6110,  # 陕西省 商洛市
    6201,  # 甘肃省 兰州市
    6202,  # 甘肃省 嘉峪关市
    6203,  # 甘肃省 金昌市
    6204,  # 甘肃省 白银市
    6205,  # 甘肃省 天水市
    6206,  # 甘肃省 武威市
    6207,  # 甘肃省 张掖市
    6208,  # 甘肃省 平凉市
    6209,  # 甘肃省 酒泉市
    6210,  # 甘肃省 庆阳市
    6211,  # 甘肃省 定西市
    6212,  # 甘肃省 陇南市
    6229,  # 甘肃省 临夏回族自治州
    6230,  # 甘肃省 甘南藏族自治州
    6301,  # 青海省 西宁市
    6302,  # 青海省 海东市
    6322,  # 青海省 海北藏族自治州
    6323,  # 青海省 黄南藏族自治州
    6325,  # 青海省 海南藏族自治州
    6326,  # 青海省 果洛藏族自治州
    6327,  # 青海省 玉树藏族自治州
    6328,  # 青海省 海西蒙古族藏族自治州
    6401,  # 宁夏回族自治区 银川市
    6402,  # 宁夏回族自治区 石嘴山市
    6403,  # 宁夏回族自治区 吴忠市
    6404,  # 宁夏回族自治区 固原市
    6405,  # 宁夏回族自治区 中卫市
    6501,  # 新疆维吾尔自治区 乌鲁木齐市
    6502,  # 新疆维吾尔自治区 克拉玛依市
    6504,  # 新疆维吾尔自治区 吐鲁番市
    6522,  # 新疆维吾尔自治区 哈密地区
    6523,  # 新疆维吾尔自治区 昌吉回族自治州
    6527,  # 新疆维吾尔自治区 博尔塔拉蒙古自治州
    6528,  # 新疆维吾尔自治区 巴音郭楞蒙古自治州
    6529,  # 新疆维吾尔自治区 阿克苏地区
    6530,  # 新疆维吾尔自治区 克孜勒苏柯尔克孜自治州
    6531,  # 新疆维吾尔自治区 喀什地区
    6532,  # 新疆维吾尔自治区 和田地区
    6540,  # 新疆维吾尔自治区 伊犁哈萨克自治州
    6542,  # 新疆维吾尔自治区 塔城地区
    6543,  # 新疆维吾尔自治区 阿勒泰地区
    6590,  # 新疆维吾尔自治区 自治区直辖县级行政区划
    8101,  # 香港 香港
]
