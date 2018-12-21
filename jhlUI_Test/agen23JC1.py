from jhlUI_Test.BasicFunction import *
role_a()
login_a1()
findXpath(xpath='//*[@id="common-leftmenu"]/ul/li[2]/div[1]/a/span[2]').click() #单击任务菜单
wait1()
findXpath(xpath='//*[@id="common-leftmenu"]/ul/li[2]/div[2]/ul/li[4]/a').click() #单击进舱按钮
wait1()
findID(id='title').send_keys('中交一公局钢材采购') #输入查询条件任务单名称
wait1()
findXpath(xpath='/html/body/div/div/div[3]/div/div/div/div/div/div[2]/div[8]/div').click() #单击搜索按钮
wait2()
findXpath(xpath='/html/body/div/div/div[3]/div/div/div/div/div/div[3]/div/div[1]/div/div[1]').click() #单击全选按钮选中
findXpath(xpath='/html/body/div/div/div[3]/div/div/div/div/div/div[3]/div/div[1]/div/div[1]').click() #单击全选按钮取消选中
findXpath(xpath='//*[@id="order-table"]/tbody[1]/tr[3]/td[1]/div').click() #单击查询结果的选中按钮
findXpath(xpath='/html/body/div/div/div[3]/div/div/div/div/div/div[3]/div/div[2]/a').click() #单击货物进舱按钮
wait1()
findID(id='batch_incoming_voyage_number').send_keys('HMHC-001') #输入航名航次
wait1()
findID(id='batch_incoming_address').send_keys('西安') #输入当前地址
wait1()
findID(id='batch_incoming_remark').send_keys('pyselenium进舱集装箱备注') #输入备注
wait1()
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div[3]/div[2]/div[1]/div').click() #单击新增集装箱按钮
wait1()
dropDowni(id='incoming_container_type',val='1')
findID(id='incoming_container_number').send_keys('GH001') #输入柜号
findID(id='incoming_container_seal_number').send_keys('QFH001') #输入铅封号
findXpath(xpath='/html/body/div[3]/div[2]/div/div[2]/div/div/div/div[3]/table/tbody/tr[2]/td/div/div/div').click() #单击第一个批次的选中按钮
# 上传进舱图片
findXpath(xpath='/html/body/div[3]/div[2]/div/div[2]/div/div/div/div[3]/table/tbody/tr[2]/td/div/div/div').click() #单击第一个批次的选中按钮
