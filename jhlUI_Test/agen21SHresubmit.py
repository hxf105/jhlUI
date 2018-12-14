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
findXpath(xpath='//*[@id="order-table"]/tbody[1]/tr[3]/td[10]/a').click() #单击编辑按钮，打开港口收货编辑画面
wait1()
findClassName(name='uploader-button').send_keys('F://测试执行资料库/文档/支持/交货签收单.doc') #上传交货签收单
wait2()
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div[2]/div/div[4]/div[2]/div[2]/table/tbody/tr[2]/td/div/div[3]').click() #单击货物验收列表的第一个的编辑按钮
wait1()
findXpath(xpath='/html/body/div[3]/div[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[1]/div/div[1]').click() #单击全选按钮
findXpath(xpath='/html/body/div[3]/div[2]/div/div[1]/a/span[2]/span').click() #单击关闭弹窗按钮
wait1()
findXpath(xpath='/html/body/div[2]/div[2]/div/div[3]/div').click() #单击提交按钮，提交给采购商审核
wait3()
