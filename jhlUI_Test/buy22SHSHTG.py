from jhlUI_Test.BasicFunction import *
role_b()
login_b1()
findID(id='title').send_keys('中交一公局钢材采购')  #查询该监管单
findID(id='order_search').click()
wait3()
findXpath(xpath='//*[@id="order-table"]/tbody/tr[3]/td[7]/div/div[1]/div/a').click() #单击查看详细按钮，进入物流流程页
wait3()