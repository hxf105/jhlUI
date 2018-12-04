from jhlUI_Test.BasicFunction import *
role_a()
login_a1()
findXpath(xpath='//*[@id="common-leftmenu"]/ul/li[2]/div[1]/a/span[2]').click() #单击任务菜单
wait1()
findXpath(xpath='//*[@id="common-leftmenu"]/ul/li[2]/div[2]/ul/li[3]/a').click() #单击港口收货菜单
wait2()
findID(id='title').send_keys('中交一公局钢材采购') #输入查询条件
wait1()
findXpath(xpath='/html/body/div/div/div[3]/div/div/div/div/div/div[2]/div[8]/div').click() #单击搜索按钮
wait2()
findXpath(xpath='//*[@id="order-table"]/tbody[1]/tr[2]/td/div/div[2]/div/a').click() #单击查看详情按钮，查看基本信息和物流信息详情
wait1()
findXpath(xpath='/html/body/div[2]/div[2]/div/div[1]/a/span[2]').click() #单击关闭按钮，关闭弹窗
wait1()
findXpath(xpath='//*[@id="order-table"]/tbody[1]/tr[3]/td[10]/a').click() #单击港口收货按钮，打开港口收货填写画面
wait1()
findClassName(name='uploader-button').send_keys('F://测试执行资料库/文档/支持/交货签收单.doc') #上传交货签收单
wait2()
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div[3]/div[2]/div[1]/div').click() #单击添加货物按钮
wait1()
findXpath(xpath='/html/body/div[3]/div[2]/div/div[2]/div/div/div/div[3]/table/tbody/tr[3]/td[7]/a').click() #单击查看详情按钮，查看箱子的详细信息
wait1()
findXpath(xpath='/html/body/div[4]/div[2]/div/div[1]/a/span[2]/span').click() #单击关闭按钮，关闭箱子箱子信息画面
wait1()
dropDowni(id='arrival_check_status',val=2) #选择下拉菜单value=2货物损坏
findXpath(xpath='/html/body/div[3]/div[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[1]/div/div[1]').click() #单击全选按钮
findXpath(xpath='/html/body/div[3]/div[2]/div/div[2]/div/div/div/div[4]/div/div[2]/div[1]/label/input').send_keys('F://测试执行资料库/新图/tim0g.jpg')
wait2()
findID(id='batch_arrival_remark').send_keys('pyselenium货物损坏')
wait1()
findXpath(xpath='/html/body/div[3]/div[2]/div/div[3]/div').click() #单击确定按钮
wait1()
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div[3]/div[2]/div[2]/table/tbody/tr[2]/td/div/div[3]').click() #单击编辑按钮，编辑已添加的货物
wait1()
findXpath(xpath='/html/body/div[3]/div[2]/div/div[1]/a/span[2]/span').click() #单击关闭按钮，关闭编辑画面
wait1()
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div[3]/div[2]/div[2]/table/tbody/tr[2]/td/div/div[2]').click() #单击删除按钮，删除已添加的货物
wait1()
# 重新把货物添加回来
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div[3]/div[2]/div[1]/div').click() #单击添加货物按钮
wait1()
findXpath(xpath='/html/body/div[3]/div[2]/div/div[2]/div/div/div/div[3]/table/tbody/tr[3]/td[7]/a').click() #单击查看详情按钮，查看箱子的详细信息
wait1()
findXpath(xpath='/html/body/div[4]/div[2]/div/div[1]/a/span[2]/span').click() #单击关闭按钮，关闭箱子箱子信息画面
wait1()
findXpath(xpath='/html/body/div[3]/div[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[1]/div/div[1]').click() #单击全选按钮
findXpath(xpath='/html/body/div[3]/div[2]/div/div[2]/div/div/div/div[4]/div/div[2]/div[1]/label/input').send_keys('F://测试执行资料库/新图/tim0g.jpg')
wait2()
findID(id='batch_arrival_remark').send_keys('pyselenium货物完好')
wait1()
findXpath(xpath='/html/body/div[3]/div[2]/div/div[3]/div').click() #单击确定按钮
wait1()
findXpath(xpath='/html/body/div[2]/div[2]/div/div[3]/div').click() #单击提交按钮，提交给采购商审核
wait3()
