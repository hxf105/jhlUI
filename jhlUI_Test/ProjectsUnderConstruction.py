#coding=gbk
from jhlUI_Test.BasicFunction import *
role_b()
login_b(username='18802922082',password='922082')
wait5()
findXpath(xpath='//*[@id="common-leftmenu"]/ul/li[3]/div[1]/a/span[2]').click() #单击项目管理菜单
wait1()
driver.get(url='http://buyer.jiaohuilian.com/html/bid-project-list.html') #打开在建项目页
wait1()
def pro(name,country,address,bcompany,scompany,des):
    findXpath(xpath='/html/body/div/div/div[3]/div/div/div/div/div/div[1]/div[2]/a').click() #单击发布在建项目
    wait3()
    findID(id='project_name').send_keys(name) #输入项目名称
    findXpath(xpath='//*[@id="city-picker-search"]/div[1]/a').click() #单击选择国家
    # 国外国家，选择国家后，省市区隐藏，不需要选择
    findXpath(xpath='//*[@id="city-picker-search"]/div[1]/div/div/input').send_keys(country) #输入国家名称
    wait1()
    findXpath(xpath='//*[@id="city-picker-search"]/div[1]/div/ul/li').click() #选择匹配出来的国家
    findID(id='area').send_keys(address) #输入具体地址
    # 选择参建公司
    findID(id='select_builing').click() #单击选择参建公司按钮
    wait1()
    findID(id='search-bulid-text').send_keys(bcompany) #输入查询条件
    wait1()
    findID(id='select-bulid-search-button').click() #单击查询按钮
    wait1()
    findXpath(xpath='//*[@id="select_bulid_company_list"]/tbody/tr/td[1]/input').click() #单击选中框选中参建公司
    findXpath(xpath='/html/body/div[2]/div[2]/div/div[3]/div').click() #单击确定按钮
    wait2()
    # 选择签约品牌
    findID(id='select_brand').click() #单击选择签约品牌按钮
    wait1()
    findID(id='search-brand-text').send_keys(scompany) #输入查询条件
    wait1()
    findID(id='select-brand-search-button').click() #单击查询按钮
    wait1()
    findXpath(xpath='//*[@id="select_brand_company_list"]/tbody/tr/td[1]/input').click() #单击选中框选中签约品牌
    wait1()
    findXpath(xpath='/html/body/div[2]/div[2]/div/div[3]/div').click() #单击确定按钮
    wait2()
    findID(id='desc').send_keys(des) #输入项目描述
    wait3()
    findID(id='publish_bid_project').click() #单击提交按钮
    wait2()
pro(name='巴基斯坦KKH-2期项目3标段',country='巴基斯坦',address='曼赛赫拉',bcompany='中交二公局第四工程有限公司',scompany='中国路桥',des='')
pro(name='马来西亚吉隆坡地铁二号线项目（MRT2）',country='马来西亚',address='吉隆坡',bcompany='中交二公局铁路工程有限公司',scompany='中国交建',des='项目位于马来西亚吉隆坡，从既有地铁一号线(MRT1)起点双溪毛糯车站开始，经过吉隆坡城市中心，终点站为马来西亚行政中心布城，全长52.2公里，标准轨距，采用750V导电轨供电。全线共37个车站，其中11个地下车站，26个高架车站（含一个预留车站），双溪毛糯车站和沙登（Serdang）车站附近各设一个车辆段。')
pro(name='马来西亚东部沿海铁路项目站前工程ECRLZQ-5标',country='马来西亚',address='东部沿海铁路',bcompany='中交二公局第六工程有限公司',scompany='中国交建',des='')
# pro(name='马来西亚金新铁路',country='',address='',bcompany='',scompany='',des='')
pro(name='马来西亚东海岸铁路项目6标',country='马来西亚',address='吉兰丹州',bcompany='中交二公局铁路工程有限公司',scompany='中国港湾',des='马来西亚东海岸铁路项目由中国交建承建，是迄今为止中马两国最大的经贸合作项目，该铁路规划长度为688公里，投资金额550亿林吉特，约合860亿人民币，工期为7年，客运设计时速为160公里，货运设计时速为80公里，建成通车后，东海岸铁路将成为马来西亚最快的一条铁路干线，将惠及440万人口。')
pro(name='印度尼西亚巨港LRT铺轨项目',country='印度尼西亚',address='巨港',bcompany='中交二公局铁路工程有限公司',scompany='中国港湾',des='印尼巨港轻轨项目合同工期为2017年2月28日至2018年4月30日，是印尼为2018年亚运会修建的，也是公司在印尼修建的第一条轻轨线路。该项目线路总长45公里，起点和终点分别为巨港国际机场和巨港札卡巴林体育中心，沿线共设高架车站13个。项目铺轨工期14个月，今年4月30日完工并进行试车运行，7月23日至7月30日对外免费开放。')
pro(name='斯里兰卡CDB三期C13道路项目',country='斯里兰卡',address='普特拉姆',bcompany='中交二公局海外事业部',scompany='西安达刚',des='帕拉维---凯皮提亚公路改扩建项目全长40公里，总投资约2260万美元')
pro(name='缅甸EINDU至KAWKAREIK道路LOT1',country='缅甸',address='克伦邦',bcompany='中交二公局海外事业部',scompany='中国路桥',des='')
pro(name='缅甸EINDU至KAWKAREIK道路LOT2项目',country='缅甸',address='克伦邦',bcompany='中交二公局海外事业部',scompany='中国路桥',des='')
# pro(name='阿联酋MENDER油田开发工程一期项目',country='',address='',bcompany='',scompany='',des='')
# pro(name='卡塔尔2号供水管线工程',country='',address='',bcompany='',scompany='',des='')
pro(name='刚果(布)布拉柴维尔NDOUO与SADELMI军营进场路',country='刚果',address='布拉柴维尔',bcompany='中交二公局第一工程有限公司',scompany='中国路桥',des='')
pro(name='莫桑比克马普托大桥项目',country='莫桑比克',address='马普托',bcompany='中交二公局第二工程有限公司',scompany='中国路桥',des='马普托大桥横跨马普托湾，连接莫桑比克首都马普托市和马普托湾南岸的卡腾贝镇。大桥桥面全长600米，由57片钢箱梁组成，总重量约8000吨。大桥总长3公里多，主跨680米，是目前非洲主跨径最大的悬索桥。大桥由中国进出口银行提供融资支持，这是中国资金、中国建设、中国标准“走出去”的又一成功案例。')
pro(name='莫桑比克SAVE河大桥及旧桥加固项目',country='莫桑比克',address='伊尼扬巴内与索法拉省交界',bcompany='中交二公局第二工程有限公司',scompany='中国路桥',des='该项目由中国路桥签约，公司负责施工，合同额39809688.09美元, 合同总工期为36个月。SAVE河大桥位于莫桑比克南北大通道EN1干线公路伊尼扬巴内与索法拉省交界处，距离莫桑比克首都马普托市819公里，距离莫桑比克第二大城市贝拉393公里。目前桥位处有一座120+210*3+120m四塔三跨自锚式悬索桥，建造时间为1969 年至1972 年。由于该桥已临近设计寿命，所以拟新建桥梁。SAVE河大桥设计为主桥120m 预应力混凝土连续梁桥，引桥为45m 预应力混凝土T 梁，桥跨布置为（2×45）+（3×45）+（65+3×120+65）+ （3×45）+（3×45）m，桥梁全桥长985m。')
pro(name='莫桑比克马普托环城路Tchumene互通项目',country='莫桑比克',address='马普托',bcompany='中交二公局东萌工程有限公司',scompany='中国路桥',des='马普托市环城路项目由中国进出口银行提高优买贷款、中国路桥工程有限公司承建。项目总额达3.15亿美元，采用设计、施工、监理总承包模式（EPC），拟建公路总长约74公里，双向4车道，计划工期两年半。该项目将成为马普托市标志性工程，连接马普托市区至阳光海岸区，并与国家1号公路衔接。')
pro(name='莫桑比克N13公路Muita-Massangulo段道路修复和和升级项目(84KM)',country='莫桑比克',address='尼亚萨省',bcompany='中交二公局东萌工程有限公司',scompany='中交集团',des='莫桑比克MM公路升级改造项目位于莫桑比克尼亚萨省境内，为Nacala 经济走廊的一部分，是连接Nacala港东海岸和尼亚萨省内陆重要通道，也是连接邻国马拉维和赞比亚的国际商业走廊的关键一段。该项目共有六段组成，总长84km，建设周期为2.5年，由非洲发展银行出资建设。该项目采用南部非洲规范（SATCC）设计与施工，设计时速正常段为80km/h，城镇与村落段为40km/h；为双向两车道，宽度10m。该项目建成后将极大方便沿线居民的出行，并带动周边经济的发展，达到消贫、减贫的目标。')
pro(name='马达加斯加连接IVATO国际机场和欧洲大道的快速路项目',country='马达加斯加',address='塔那那利佛',bcompany='中交二公局东萌工程有限公司',scompany='中国路桥',des='该项目系马总统埃里本人提出，亲自划线，并在中非合作论坛约堡峰会期间当面向习主席提出的希中方帮助实施的道路基础设施项目。项目全长18.67公里，其中第一期通车部分为4.759公里，项目投资额约1.43亿美元，实施单位为中国路桥工程有限责任公司。')
pro(name='安哥拉以路桥名义中标项目',country='安哥拉',address='罗安达',bcompany='中交二公局东萌工程有限公司',scompany='中国路桥',des='中国路桥工程有限责任公司与安哥拉GRINER公司和葡萄牙NORAFRICA公司组成的联合体中标安哥拉新宽扎河大桥建设项目。项目合同总额约合1.1亿美元，工期为24个月。新桥设计全长622米,采用A型双塔斜拉桥结构，主跨长126米+300米+126米，南北引桥各35米， 桥面宽度27.7米，下部结构为桩基础，梁体为悬浇箱梁，建成后将取代1975年建成、因年久失修已成危桥的旧宽扎河大桥，成为安哥拉境内该类型桥梁跨径第一，所有类型桥梁中跨径第三的标杆性工程。')
pro(name='安哥拉恩泽托和库因巴7条市政道路项目',country='安哥拉',address='恩泽托和库因巴',bcompany='中交二公局东萌工程有限公司',scompany='中国路桥',des='')
pro(name='安哥拉恩泽托-索约96.06公里高速公路建设项目05标',country='安哥拉',address='恩泽托-索约',bcompany='中交二公局东萌工程有限公司',scompany='中水四局',des='')
pro(name='肯尼亚内马铁路一期工程120公里线上7标段',country='肯尼亚',address='内马',bcompany='中交二公局铁路工程有限公司',scompany='中国路桥',des='')
pro(name='肯尼亚内马铁路一期工程120公里线下1标段',country='肯尼亚',address='内马',bcompany='中交二公局海外事业部',scompany='中国路桥',des='')
pro(name='肯尼亚内罗毕集装箱内陆港扩建项目（ICD）',country='肯尼亚',address='内罗毕',bcompany='中交二公局海外事业部',scompany='中国路桥',des='')
pro(name='尼日利亚凯菲至马库尔迪公路改扩建一期项目第3标段',country='尼日利亚',address='凯菲至马库尔迪',bcompany='中交二公局第六工程有限公司',scompany='中国港湾',des='')
pro(name='尼日利亚凯菲至马库尔迪公路改扩建工程项目总经理部主营地建设工程项目',country='尼日利亚',address='凯菲至马库尔迪',bcompany='中交二公局第六工程有限公司',scompany='中国港湾',des='')
pro(name='科特迪瓦铁比苏－布瓦凯高速公路项目1标段',country='科特迪瓦',address='铁比苏－布瓦凯',bcompany='中交二公局第六工程有限公司',scompany='中国路桥',des='')
pro(name='牙买加主要基础设施发展项目Mandela公路改造工程道路',country='牙买加',address='金士顿',bcompany='中交二公局第三工程有限公司',scompany='中国港湾',des='该项目由中国港湾签约，公司负责施工。合同价22，695，838美元，约合人民币1.5亿元，合同工期600天。Mandela公路改造工程位于牙买加首都金士顿西部，工程与正在施工的Marcus Garvey Drive项目一样，为牙买加主要基础设施发展项目（MIDP）的子项目。主线长度3.5千米，是典型的公路拓宽扩建工程，公司承担了路基、路面、涵洞、交安和部分照明工程。项目含2处互通，Six Miles互通主要工程为原有道路重新铺设路面，有局部需要加宽。Diamond互通为新建互通区。')
pro(name='哥斯达黎加32号公路Siquirres营地建设和安装项目',country='哥斯达黎加',address='瓜匹莱斯、瓜西莫、锡基莱斯',bcompany='中交二公局第三工程有限公司',scompany='中国港湾',des='项目合同总金额1.53亿美元（约10.2亿人民币,其中一标合同金额84723813.92美元，二标合同金额68276186.08美元）。项目全长61.2km，经过Guapiles（瓜匹莱斯）、Guacimo（瓜西莫）及Siquirres（锡基莱斯）三个市，合同工期34个月。主要工程量包括砼11.4万m?，钢筋0.9万t，钢绞线509.9t，砂砾、水稳及级配碎石104.5万m?，沥青料15万m?，桩基288个（1.2m桩径180根、1.5m桩径108根），承台及系梁66个，墩柱94个（圆柱径1.3m72根，主线桥薄壁墩11根，互通及PSV桥薄壁墩11根），台帽及盖梁125个，预制梁板476片（箱梁232片，板梁134片、梯道梁及槽型梁110片），浆砌1.9万m?。')
pro(name='牙买加主要基础设施发展项目Ferris Cross to Mackfield Road公路改造工程项目',country='牙买加',address='Savanna La Mar',bcompany='中交二公局第三工程有限公司',scompany='中国港湾',des='牙买加Ferris To Mackfield Road项目位于牙买加Savanna La Mar城市中部，是Savanna La Mar市重要的道路走廊之一。项目总长约12.581公里。全线起点和终点处地势较为平坦；中间为山区，高低起伏较大，多为挖方，存在大量高填和深挖段落，最大挖方深度约有40米。项目起点至K4+300段为南北走向，地势比较平缓开阔；K4+300-K11+900段为山岭重丘区，原有道路沿着山腰布设，此区域加宽多为向山岭侧加宽，多为挖石方，局部为半填半挖区域。')
pro(name='黑山南北高速项目第2标段',country='黑山',address='BAR港至北部城市BOLJARE主干道',bcompany='中交二公局第六工程有限公司',scompany='中国路桥',des='黑山南北高速公路项目第2标段，工程起讫桩号K11+487.51--K22+744.87，共11.257Km。主要工程内容包括：路基工程、路面工程、隧道工程、桥梁工程、涵洞工程、排水工程、防护工程、机电配套土建等工程内容，合同造价约1.43亿欧元，工期36个月')
pro(name='克罗地亚佩列沙茨大桥项目',country='克罗地亚',address='佩列沙茨',bcompany='中交二公局第一工程有限公司',scompany='中国路桥',des='')
# pro(name='',country='',address='',bcompany='',scompany='',des='')
