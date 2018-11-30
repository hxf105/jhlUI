from jhlUI_Test.BasicFunction import *
role_b()
login_b1()
# 封箱信息审核不通过
findID(id='title').send_keys('中交一公局钢材采购')  #查询该监管单
wait1()
findID(id='order_search').click()
wait3()
findXpath(xpath='//*[@id="order-table"]/tbody/tr[3]/td[7]/div/div[1]/div/a').click() #单击查看详细按钮
wait2()
findXpath(xpath='//*[@id="order-table"]/tbody[1]/tr[3]/td[7]/div/div[1]/div/a').click() #单击查看详细按钮，进入物流流程页
wait1()
findXpath(xpath='//*[@id="batch-flow-show"]/div/div[2]/div[2]/div/ul/li[2]/div[3]/div[4]/span[3]').click() #单击封箱节点的查看详细按钮
wait1()
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div[2]/div[2]/div[2]/label[2]/input').click() #单击审核不通过按钮
findClassName(name='txtarea').send_keys('pyselenium封箱审核不通过')
wait1()
findClassName(name='confirm-btn').click() #单击提交按钮
# findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div[2]/div[4]/div[2]/div').click() #单击提交按钮
wait3()

