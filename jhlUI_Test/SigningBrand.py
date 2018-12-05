from jhlUI_Test.BasicFunction import *
role_b()
login_b(username='18802922082',password='922082')
wait10()
findXpath(xpath='//*[@id="common-leftmenu"]/ul/li[6]/div[1]/a/span[2]').click() #单击系统设置菜单
wait2()
driver.get(url='http://buyer.jiaohuilian.com/html/basic-base-manage.html')
wait1()
# 开始
findID(id='brand-add').click() #单击新增签约品牌按钮
wait1()
findID(id='brand_name').send_keys('中国铁路工程集团有限公司') #输入品牌全称
findID(id='brand_short_name').send_keys('中铁工') #输入品牌简称
findID(id='tax_id').send_keys('91110000102016548J') #输入税号
findID(id='company_addr').send_keys('北京市丰台区南四环西路128号院1号楼920') #输入公司地址
findID(id='company_phone').send_keys('010-51845225') #输入联系电话
wait2()
findXpath(xpath='/html/body/div[2]/div[2]/div/div[3]/div').click() #单击确定按钮
wait2()
# 结束
# 开始
findID(id='brand-add').click() #单击新增签约品牌按钮
wait1()
findID(id='brand_name').send_keys('中交第二公路工程局有限公司') #输入品牌全称
findID(id='brand_short_name').send_keys('二公局）') #输入品牌简称
findID(id='tax_id').send_keys('91610000220521254B') #输入税号
findID(id='company_addr').send_keys('中国西安市科技六路33号') #输入公司地址
findID(id='company_phone').send_keys('029-89560113') #输入联系电话
wait2()
findXpath(xpath='/html/body/div[2]/div[2]/div/div[3]/div').click() #单击确定按钮
wait2()
# 结束
# 开始
findID(id='brand-add').click() #单击新增签约品牌按钮
wait1()
findID(id='brand_name').send_keys('西安达刚路面机械股份有限公司') #输入品牌全称
findID(id='brand_short_name').send_keys('西安达刚') #输入品牌简称
findID(id='tax_id').send_keys('91610131735085973C') #输入税号
findID(id='company_addr').send_keys('西安市高新区科技三路60号') #输入公司地址
findID(id='company_phone').send_keys('029-88328410') #输入联系电话
wait2()
findXpath(xpath='/html/body/div[2]/div[2]/div/div[3]/div').click() #单击确定按钮
wait2()
# 结束
# 开始
findID(id='brand-add').click() #单击新增签约品牌按钮
wait1()
findID(id='brand_name').send_keys('中国水利水电第四工程局有限公司') #输入品牌全称
findID(id='brand_short_name').send_keys('中水四局') #输入品牌简称
findID(id='tax_id').send_keys('9163000022658124XK') #输入税号
findID(id='company_addr').send_keys('西宁市东川工业园区金桥路38号') #输入公司地址
findID(id='company_phone').send_keys('0971-8088078') #输入联系电话
wait2()
findXpath(xpath='/html/body/div[2]/div[2]/div/div[3]/div').click() #单击确定按钮
wait2()
# 结束