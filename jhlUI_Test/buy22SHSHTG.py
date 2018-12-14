from jhlUI_Test.BasicFunction import *
role_b()
login_b1()
findID(id='title').send_keys('中交一公局钢材采购')  #查询该监管单
findID(id='order_search').click()
wait3()
findXpath(xpath='//*[@id="order-table"]/tbody/tr[3]/td[7]/div/div[1]/div/a').click() #单击查看详细按钮，进入物流流程页
wait3()
findXpath(xpath='//*[@id="batch-flow-show"]/div/div[2]/div[2]/div/ul/li[2]/div[7]/div[4]/span[3]').click() #单击港口交货的查看详细按钮
wait1()
findXpath(xpath='//*[@id="arrival_file_show_list"]/div/div/div/div/span[2]').click() #单击交货签收单的附件下载按钮
wait1()
findClassName(name='txtarea').send_keys('pyselenium港口交货审核通过') #输入备注信息
wait1()
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div[2]/div/table/tbody/tr[3]/td[2]/div').click() #单击提交按钮
wait2()
