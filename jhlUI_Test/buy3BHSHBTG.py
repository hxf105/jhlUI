from jhlUI_Test.BasicFunction import *
role_b()
login_b1()

# 备货信息审核不通过
findID(id='title').send_keys('中交一公局钢材采购')  #查询该监管单
findID(id='order_search').click()
wait3()
findXpath(xpath='//*[@id="order-table"]/tbody/tr[3]/td[7]/div/div[1]/div/a').click() #单击查看详细按钮
wait3()
findXpath(xpath='//*[@id="batch-flow-show"]/div/div[2]/div[2]/div/ul/li[2]/div[2]/div[4]/span[3]').click() #单击供应商备货的查看详细按钮
wait1()
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div[1]/div/div[5]/div[2]/div[1]/a').click() #单击查看更多产品按钮
wait1()
findXpath(xpath='/html/body/div[3]/div[2]/div/div[1]/a/span[2]').click() #单击关闭按钮，关闭产品弹窗
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div[2]/div[2]/div[2]/label[2]/input').click()
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div[2]/div[3]/div[2]/textarea').send_keys('审核不通过，pyselenium')
wait1()
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div[2]/div[4]/div[2]/div').click() #单击提交按钮
wait2()
