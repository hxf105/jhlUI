from jhlUI_Test.BasicFunction import *
role_s()
login_s1()
findXpath(xpath='//*[@id="common-leftmenu"]/ul/li[2]/div[1]/a/span[2]').click() #单击订单菜单
wait1()
findXpath(xpath='//*[@id="common-leftmenu"]/ul/li[2]/div[2]/ul/li[1]/a').click() #单击进行中的订单菜单
wait3()
findID(id='title').send_keys('中交一公局钢材采购') #输入查询条件：任务单名称“中交一公局钢材采购”
wait1()
findID(id='order_search').click() #单击搜索按钮
wait3()
# 查看唛头脚本未写
findXpath(xpath='//*[@id="order-table"]/tbody/tr[3]/td[6]/div/div[1]/div/a').click() #单击查看详情按钮，进入物流流程画面
wait3()
findXpath(xpath='//*[@id="batch-flow-show"]/div/div/div[2]/div/ul/li[2]/div[6]/div[3]/a[2]').click() #单击查看唛头按钮,打开唛头画面
wait1()
findID(id='export_word').click() #单击导出按钮，下载唛头
findXpath(xpath='/html/body/div/div/div[3]/div/div/div/div/div[1]/div/div[2]/a[1]').click() #单击返回按钮，返回物流流程画面
wait1()
findXpath(xpath='//*[@id="batch-flow-show"]/div/div/div[2]/div/ul/li[2]/div[6]/div[4]/span[3]').click() #单击去出库按钮
wait1()
findXpath(xpath='//*[@id="form-info"]/div/div/table[1]/tbody/tr[2]/td[2]/div[1]/label/input').send_keys('F://测试执行资料库/新图/tim0g.jpg')
wait2()
findClassName(name='txtarea').send_keys('pyselenium出库信息请审核')
wait1()
findID(id='pub_deliver_transport_company').send_keys('pyselenium货运公司名称')
findID(id='pub_deliver_ship_driver_name').send_keys('pyselenium货运公司联系人')
findID(id='pub_deliver_ship_driver_phone').send_keys('18292678346')
findID(id='id="pub_deliver_waybill_sn"').send_keys('pyselenium货运单号')
findID(id='pub_deliver_address').send_keys('pyselenium地址')
js="$('input[id=pub_deliver_start_time]').removeAttr('readonly')"
driver.execute_script(js)
findID(id='pub_deliver_start_time').send_keys('F://测试执行资料库/新图/tim0g.jpg')
wait2()
findXpath(xpath='/html/body/div[2]/div[2]/div/div[3]/div').click() #单击提交按钮
wait3()