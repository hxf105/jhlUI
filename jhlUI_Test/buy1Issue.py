from jhlUI_Test.BasicFunction import *
role_b()
login_b1()

findXpath(xpath='/html/body/div/div/div[3]/div/div/div/div/div/div[1]/div[2]/a[2]').click() #单击“发布监管单”按钮，打开发布监管单-订单信息画面
wait2()
# findXpath(xpath='//*[@id="task-tab"]/div[2]/div[1]/div[2]/div').click() #单击“下一步”按钮，下不去
# wait1()
# self.driver.execute_script("arguments[0].click()",find_element_by_id('select-project-button'))
# targetElem=findID(id='select-project-button')
# driver.execute_script("arguments[0].scrollIntoView();",targetElem) #拖动到元素可见【失败】
findID(id='select-project-button').click() #单击“选择在建项目”按钮
wait2()
findID(id='search-project-text').send_keys('中交一公局集团10月份钢材招标采购评标结果公示') #查询这个项目
findID(id='select-project-search-button').click()  #单击查询按钮
wait2()
findXpath(xpath='//*[@id="select_project_list"]/tbody/tr/td[2]').click() #选中查询结果
findXpath(xpath='/html/body/div[2]/div[2]/div/div[3]/div').click() #单击确定按钮
wait2()
findID(id='title').send_keys('中交一公局钢材采购') #输入任务单名称
findID(id='plan_sn').send_keys('Plan_pyselenium') #输入计划编号
findID(id='assembly_sn').send_keys('LJ_pyselenium') #输入来件编号
findID(id='contract_type').find_element_by_xpath("//option[@value='2']").click() #单击合同类型下拉菜单,并选中一项
# 日期控件插件，选择日期，绕过这个，直接干掉栏位的readonly属性，input日期即可
# js = "document.getElementById('select-date-dom').removeAttribute('readonly')"  # 1.原生js，移除属性 【成功】
js = "$('input[id=select-date-dom]').removeAttr('readonly')"  # 2.jQuery，移除属性       【成功】
# js = "$('input[id=select-date-dom]').attr('readonly',false)"  # 3.jQuery，设置为false  【成功】
driver.execute_script(js)
findID(id='select-date-dom').send_keys('2018-11-30')  #输入日期
findXpath(xpath='//*[@id="order_info"]/tbody/tr[10]/td[2]/div[1]/label/input').send_keys('F:/测试执行资料库/文档/支持/pyselenium文件采购合同.docx')  #上传文件
findID(id='select-supply-company').click() #单击选择供应商
wait2()
findID(id='search-company-text').send_keys('柏嘉交科-供应商测试')
findID(id='select-company-search-button').click() #单击查询按钮
wait2()
findXpath(xpath='//*[@id="select_company_list"]/tbody/tr/td[1]').click() #单击选中按钮
wait1()
findXpath(xpath='/html/body/div[2]/div[2]/div/div[3]/div').click() #单击确定按钮
wait2()
findXpath(xpath='//*[@id="order_info"]/tbody/tr[12]/td[2]/div/div').click() #单击选择物流负责人
wait2()
findID(id='search-reciever-text').send_keys('侯小凤')
findID(id='select-reciever-search-button').click() #单击搜索按钮
wait2()
findXpath(xpath='//*[@id="select_reciever_emp_list"]/tbody/tr/td[2]').click() #单击查询结果选中
findXpath(xpath='/html/body/div[2]/div[2]/div/div[3]/div').click() #单击确定按钮
wait2()
findXpath(xpath='//*[@id="order_info"]/tbody/tr[13]/td[2]/div/div').click() #单击选择退税负责人
wait2()
findID(id='search-reciever-text').send_keys('侯小凤')  #查询
findID(id='select-reciever-search-button').click()  #单击搜索按钮
wait2()
findXpath(xpath='//*[@id="select_reciever_emp_list"]/tbody/tr/td[2]').click() #选中查询结果
findXpath(xpath='/html/body/div[2]/div[2]/div/div[3]/div').click() #单击确定按钮
wait2()
findID(id='remark').send_keys('pyselenium请务必尽快出库')  #输入备注
wait2()
findXpath(xpath='//*[@id="task-tab"]/div[2]/div[1]/div[2]/div').click() #单击下一步按钮
wait2()
# 下载产品模板
# options=webdriver.ChromeOptions()
# prefs={'profile.default_content_settings.popups':0,'download.default_directory':'F:/pyselenium下载文件'}
# options.add_experimental_option('prefs',prefs)
# driver=webdriver.Chrome(options=options)
findID(id='product-template-download').click() #单击下载产品模板
findID(id='excel-export').send_keys('F:/测试执行资料库/货物上传/0925马达加斯加货物表.xlsx') #上传产品模板
wait3()
findXpath(xpath='//*[@id="task-tab"]/div[2]/div[2]/div[3]/div[2]').click() #单击下一步按钮
wait2()
findXpath(xpath='//*[@id="company_buy_address"]/div[1]/div[1]').click() #单击选择地址
wait1()
findXpath(xpath='//*[@id="task-tab"]/div[2]/div[3]/div[3]/div[2]').click() #单击提交按钮，提交后，显示监管单详情画面
wait15()
findXpath(xpath='/html/body/div/div/div[3]/div/div/div/div/div/div[1]/div/a').click() #单击监管单详情画面的返回按钮，返回到进行中的订单列表页
wait3()







#
# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.quit()

