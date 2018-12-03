from jhlUI_Test.BasicFunction import *
role_b()
login_b1()
findXpath(xpath='//*[@id="common-leftmenu"]/ul/li[4]/div[1]/a/span[2]').click() #单击发运信息菜单
wait1()
findXpath(xpath='//*[@id="common-leftmenu"]/ul/li[4]/div[2]/ul/li[1]/a').click() #单击订舱信息菜单
wait2()
findXpath(xpath='//*[@id="order-table"]/tbody/tr[4]/td[8]/a').click() #单击查看详细按钮，打开订舱信息审核弹窗
wait1()
findClassName(name='txtarea').send_keys('pyselenium订舱审核通过')
wait1()
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div[3]/div[2]/div[3]/div[2]/div').click() #单击提交按钮
wait3()