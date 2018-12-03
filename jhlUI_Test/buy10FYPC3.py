from jhlUI_Test.BasicFunction import *
role_b()
login_b1()
# 推送发运批次-滚装船
findID(id='title').send_keys('中交一公局钢材采购')  #查询该监管单
wait1()
findID(id='order_search').click()
wait3()
findXpath(xpath='//*[@id="order-table"]/tbody/tr[3]/td[7]/div/div[1]/div/a').click() #单击查看详细按钮
wait2()
findXpath(xpath='//*[@id="order-table"]/tbody[1]/tr[3]/td[7]/div/div[1]/div/a').click() #单击查看详细按钮，进入物流流程页
wait2()
# 件重尺下载，脚本未写
findXpath(xpath='//*[@id="batch-flow-show"]/div/div[2]/div[2]/div/ul/li[2]/div[4]/div[4]/span[2]').click() #单击物流流程页内的推送发运批次按钮
wait1()
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div').click() #单击选择国内货代按钮
wait1()
findID(id='search-company-text').send_keys('柏嘉交科-货代商测试') #输入查询条件
wait1()
findID(id='select-company-search-button').click() #单击查询按钮
wait1()
findXpath(xpath='//*[@id="select_company_list"]/tbody/tr/td[1]/input').click() #单击单选选中按钮，选中货代
findXpath(xpath='/html/body/div[3]/div[2]/div/div[3]/div').click() #单击确定按钮
wait1()
findID(id='push_batch_shipment_port_name').send_keys('上海') #输入你送港口
findID(id='push_batch_tran_type').find_element_by_xpath("//option[@value='3']").click() #选择发运方式3滚装船
wait1()
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[4]/div[2]/label/input').send_keys('F://测试执行资料库/文档/支持/报关单中交柏嘉大型泵体采购计划实施一期产品信息表.xlsx') #上传报关单
findClassName(name='auv-file-control').send_keys('F://测试执行资料库/新图/timg (5).jpg') #上传报关单
wait3()
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[5]/div[2]/div/table/tbody/tr/td[6]/a').click() #单击件重尺下载按钮
findID(id='push_batch_remark').send_keys('pyselenium推送发运批次') #输入备注
wait2()
findXpath(xpath='/html/body/div[2]/div[2]/div/div[3]/div').click() #单击提交按钮
wait2()
findXpath(xpath='//*[@id="batch-flow-show"]/div/div[2]/div[2]/div/ul/li[2]/div[4]/div[4]/span[2]').click() #单击推送发运批次的查看详细按钮
wait1()
findClassName(name='link edit').click() #单击编辑按钮
wait1()
# findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/a[1]').click() #单击编辑按钮
findXpath(xpath='/html/body/div[2]/div[2]/div/div[3]/div') #单击编辑画面的提交按钮
wait2()
findXpath(xpath='//*[@id="batch-flow-show"]/div/div[2]/div[2]/div/ul/li[2]/div[4]/div[4]/span[2]').click() #单击推送发运批次的查看详细按钮
wait1()
findClassName(name='link preview-history').click() #单击查看历史按钮
wait1()
# findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/a[2]').click() #单击查看历史按钮
findXpath(xpath='/html/body/div[2]/div[2]/div/div[1]/a/span[2]/span').click() #单击关闭按钮
wait2()