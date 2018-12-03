from jhlUI_Test.BasicFunction import *
role_a()
login_a1()
findXpath(xpath='//*[@id="common-leftmenu"]/ul/li[2]/div[1]/a/span[2]').click() #单击任务菜单
wait1()
findXpath(xpath='//*[@id="common-leftmenu"]/ul/li[2]/div[2]/ul/li[1]/a').click() #单击待订舱菜单
wait1()
findID(id='title').send_keys('中交一公局钢材采购')
wait1()
findXpath(xpath='/html/body/div/div/div[3]/div/div/div/div/div/div[2]/div[7]/div').click() #单击查询按钮
wait2()
findXpath(xpath='//*[@id="order-table"]/tbody/tr[3]/td[2]/a').click() #单击任务单名称，查看任务单详细信息
wait1()
findID(id='showMore').click() #单击产品信息的查看更多按钮
wait1()
findXpath(xpath='/html/body/div[2]/div[2]/div/div[1]/a/span[2]/span').click() #单击产品信息弹窗的关闭按钮
findXpath(xpath='/html/body/div/div/div[3]/div/div/div/div/div/div[1]/div/a').click() #单击返回列表按钮
wait2()
findXpath(xpath='//*[@id="image-list-customs-declaration0"]/div/div/div/div/span[2]').click() #单击报关单下载按钮
wait1()
findXpath(xpath='//*[@id="order-table"]/tbody/tr[3]/td[9]/a').click() #单击物资件重尺下载按钮
wait1()
findXpath(xpath='//*[@id="order-table"]/tbody/tr[3]/td[10]/a').click() #单击查看详情按钮
wait1()
findXpath(xpath='/html/body/div[2]/div[2]/div/div[1]/a/span[2]/span').click() #单击关闭按钮
findXpath(xpath='//*[@id="order-table"]/tbody/tr[3]/td[1]/div/div').click() #单击该任务单的选中按钮
findXpath(xpath='/html/body/div/div/div[3]/div/div/div/div/div/div[3]/div/div[2]/a').click() #单击推送订舱信息按钮，打开订舱信息填写弹窗
wait1()
findID(id='booking_batch_destination_port_name').send_keys('布宜诺斯艾利斯') #输入目的港
findID(id='booking_shipment_port_name').send_keys('上海') #输入起运港
js="$('input[id=booking_ship_time_1]').attr('readonly',false)"
driver.execute_script(js)
findID(id='booking_ship_time_1').send_keys('2018-12-31') #开船时间
js="$('input[id=booking_ship_time_2]').attr('readonly',false)"
driver.execute_script(js)
findID(id='booking_ship_time_2').send_keys('2018-12-29') #截关时间
js="document.getElementById('booking_ship_time_3').removeAttribute('readonly')"
driver.execute_script(js)
findID(id='booking_ship_time_3').send_keys('2018-12-27') #截单时间
js="$('input[id=booking_ship_time_4]').removeAttr('readonly')"
driver.execute_script(js)
findID(id='booking_ship_time_4').send_keys('2018-12-25') #报关时间
js="$('input[id=booking_ship_time_5]').removeAttr('readonly')"
driver.execute_script(js)
findID(id='booking_ship_time_5').send_keys('2018-12-23') #领单时间
js="$('input[id=booking_ship_time_6]').removeAttr('readonly')"
driver.execute_script(js)
findID(id='booking_ship_time_6').send_keys('2018-12-21') #装箱时间
js="$('input[id=booking_ship_time_7]').removeAttr('readonly')"
driver.execute_script(js)
findID(id='booking_ship_time_7').send_keys('2018-12-19') #最晚到港时间
js="$('input[id=booking_ship_time_8]').removeAttr('readonly')"
driver.execute_script(js)
findID(id='booking_ship_time_8').send_keys('2018-12-18') #单据制作时间
js="$('input[id=booking_ship_time_9]').removeAttr('readonly')"
driver.execute_script(js)
findID(id='booking_ship_time_9').send_keys('2018-12-15') #订舱时间
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div[13]/div[2]/label/input').send_keys('F://测试执行资料库/文档/支持/进舱通知单.xlsx') #上传进舱通知单
wait2()
findID(id='booking_remark').send_keys('pyselenium货代提交订舱信息') #填写备注
wait1()
findXpath(xpath='/html/body/div[2]/div[2]/div/div[3]/div').click() #单击提交按钮
wait3()




