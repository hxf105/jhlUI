from jhlUI_Test.BasicFunction import *
role_a()
login_a1()
findXpath(xpath='//*[@id="common-leftmenu"]/ul/li[2]/div[1]/a/span[2]').click() #单击任务菜单
wait1()
findXpath(xpath='//*[@id="common-leftmenu"]/ul/li[2]/div[2]/ul/li[2]/a').click() #单击已订舱菜单
wait2()
findXpath(xpath='//*[@id="order-table"]/tbody[1]/tr[3]/td[8]/a[1]').click() #单击编辑按钮
wait1()
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div[1]/div[2]/ul/li[2]/a').click() #单击编辑批次按钮
wait1()
findXpath(xpath='/html/body/div[3]/div[2]/div/div[2]/div/div/div[1]/table/tbody/tr[3]/td[9]/a').click() #单击物资件重尺按钮
wait1()
findXpath(xpath='/html/body/div[3]/div[2]/div/div[3]/div').click() #单击确定按钮
wait1()
findXpath(xpath='/html/body/div[2]/div[2]/div/div[3]/div').click() #单击提交按钮，提交订舱信息给采购商审核
wait3()