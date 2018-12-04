from jhlUI_Test.BasicFunction import *
role_b()
login_b1()
findID(id='title').send_keys('中交一公局钢材采购')  #查询该监管单
findID(id='order_search').click()
wait3()
findXpath(xpath='//*[@id="order-table"]/tbody/tr[3]/td[7]/div/div[1]/div/a').click() #单击查看详细按钮，进入物流流程页
wait3()
findXpath(xpath='//*[@id="batch-flow-show"]/div/div[2]/div[2]/div/ul/li[2]/div[6]/div[3]/a[2]').click() #单击查看唛头按钮，打开唛头画面
wait1()
findID(id='export_word').click() #单击导出按钮，下载唛头
findXpath(xpath='/html/body/div/div/div[3]/div/div/div/div/div[1]/div/div[2]/a[1]').click() #单击返回按钮，返回物流流程画面
wait1()
findXpath(xpath='//*[@id="batch-flow-show"]/div/div[2]/div[2]/div/ul/li[2]/div[6]/div[4]/span[3]').click() #单击出库节点的查看详细按钮
wait1()
findClassName(name='txtarea').send_keys('pyselenium出库审核通过')
wait1()
findClassName(name='confirm-btn').click() #单击提交按钮
