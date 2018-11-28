from jhlUI_Test.BasicFunction import *
findXpath(xpath='//*[@id="common-leftmenu"]/ul/li[2]/div[1]/a/span[2]').click() #单击订单菜单
wait3()
findXpath(xpath='//*[@id="common-leftmenu"]/ul/li[2]/div[2]/ul/li[1]/a').click() #单击进行中的订单菜单
wait3()
findID(id='title').send_keys('中交一公局钢材采购') #输入查询条件：任务单名称“中交一公局钢材采购”
findID(id='order_search').click() #单击搜索按钮
wait3()
findXpath(xpath='//*[@id="order-table"]/tbody/tr[3]/td[6]/div/div[1]/div/a').click() #单击查看详情按钮，进入物流流程画面
wait3()
findXpath(xpath='//*[@id="batch-flow-show"]/div/div/div[2]/div/ul/li[2]/div[3]/div[4]/span[3]').click() #单击去封箱按钮
wait3()
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div/div/div[1]/div/div').click() #单击封箱信息按钮
wait3()