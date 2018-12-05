from jhlUI_Test.BasicFunction import *
role_b()
login_b(username='18802922082',password='922082')
findXpath(xpath='//*[@id="common-leftmenu"]/ul/li[6]/div[1]/a/span[2]').click() #单击系统设置菜单
wait2()
driver.get(url='http://buyer.jiaohuilian.com/html/basic-base-manage.html')
# findXpath(xpath='//*[@id="common-leftmenu"]/ul/li[6]/div[2]/ul/li[7]/a').click() #单击基础数据管理菜单
wait1()
findID(id='company-add').click() #单击新建参建公司按钮
wait1()
findID(id='builing_company_name').send_keys('中交二公局第四工程有限公司') #输入公司全称
findID(id='builing_short_name').send_keys('四公司') #输入公司简称
wait1()
findXpath(xpath='/html/body/div[2]/div[2]/div/div[3]/div').click() #单击确定按钮
wait3()
findID(id='company-add').click() #单击新建参建公司按钮
wait1()
findID(id='builing_company_name').send_keys('中交二公局铁路工程有限公司') #输入公司全称
findID(id='builing_short_name').send_keys('铁路公司') #输入公司简称
wait1()
findXpath(xpath='/html/body/div[2]/div[2]/div/div[3]/div').click() #单击确定按钮
wait3()
findID(id='company-add').click() #单击新建参建公司按钮
wait1()
findID(id='builing_company_name').send_keys('中交二公局电务工程有限公司') #输入公司全称
findID(id='builing_short_name').send_keys('电务公司') #输入公司简称
wait1()
findXpath(xpath='/html/body/div[2]/div[2]/div/div[3]/div').click() #单击确定按钮
wait3()
findID(id='company-add').click() #单击新建参建公司按钮
wait1()
findID(id='builing_company_name').send_keys('中交二公局海外事业部') #输入公司全称
findID(id='builing_short_name').send_keys('海外事业部') #输入公司简称
wait1()
findXpath(xpath='/html/body/div[2]/div[2]/div/div[3]/div').click() #单击确定按钮
wait3()
findID(id='company-add').click() #单击新建参建公司按钮
wait1()
findID(id='builing_company_name').send_keys('中交二公局第一工程有限公司') #输入公司全称
findID(id='builing_short_name').send_keys('一公司') #输入公司简称
findXpath(xpath='/html/body/div[2]/div[2]/div/div[3]/div').click() #单击确定按钮
wait3()
findID(id='company-add').click() #单击新建参建公司按钮
wait1()
findID(id='builing_company_name').send_keys('中交二公局第二工程有限公司') #输入公司全称
findID(id='builing_short_name').send_keys('二公司') #输入公司简称
wait1()
findXpath(xpath='/html/body/div[2]/div[2]/div/div[3]/div').click() #单击确定按钮
wait3()