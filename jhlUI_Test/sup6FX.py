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
findXpath(xpath='//*[@id="order-table"]/tbody/tr[3]/td[6]/div/div[1]/div/a').click() #单击查看详情按钮，进入物流流程画面
wait3()
findXpath(xpath='//*[@id="batch-flow-show"]/div/div/div[2]/div/ul/li[2]/div[3]/div[4]/span[3]').click() #单击去封箱按钮
wait1()
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div/div/div[1]/div/div').click() #单击封箱信息按钮
wait2()
# 封第一个箱子
findXpath(xpath='//*[@id="add_package_items"]/thead/tr/th[1]/div[1]/input').click() #单击全选按钮
findXpath(xpath='//*[@id="add_package_items"]/tbody/tr[2]/td[6]/div/input').clear()
findXpath(xpath='//*[@id="add_package_items"]/tbody/tr[2]/td[6]/div/input').send_keys('5') #修改封箱数量
wait1()
findXpath(xpath='/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div[2]/div[1]/div[2]/div[4]/div[2]/ul/li[4]/a').clcik() #单击下一页按钮
wait1()
findXpath(xpath='//*[@id="add_package_items"]/thead/tr/th[1]/div[1]/input').click() #单击全选按钮
wait1()
findID(id='package-add-num').send_keys('1') #输入箱号
wait1()
findXpath(xpath='/html/body/div[3]/div[2]/div/div[3]/div[2]').click() #单击提交按钮
wait1()
# 封第二个箱子
findXpath(xpath='//*[@id="add_package_items"]/thead/tr/th[1]/div[1]/input').click() #单击全选按钮
wait1()
findXpath(xpath='//*[@id="add_package_items"]/tbody/tr[2]/td[6]/div/input').clear()
findXpath(xpath='//*[@id="add_package_items"]/tbody/tr[2]/td[6]/div/input').send_keys('5') #修改封箱数量
wait1()
findXpath(xpath='/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div[2]/div[1]/div[2]/div[4]/div[2]/ul/li[4]/a').clcik() #单击下一页按钮
wait1()
findXpath(xpath='//*[@id="add_package_items"]/thead/tr/th[1]/div[1]/input').click() #单击全选按钮
wait1()
findID(id='package-add-num').send_keys('2') #输入箱号
wait1()
findXpath(xpath='/html/body/div[3]/div[2]/div/div[3]/div[2]').click() #单击提交按钮
wait2()
# findXpath(xpath='/html/body/div[3]/div[2]/div/div[1]/a/span[2]').click() #单击关闭按钮
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/a[1]').click() #单击包装待添加按钮
wait1()
findID(id='package_type_num').clear() #清除箱号
findID(id="package_type_num").send_keys('2-1') #输入新箱号
wait1()
findID(id='package_item_note').send_keys('配件') #输入货物说明
wait1()
findID(id='package_type_code').find_element_by_xpath("//option[@value='1']").click() #选择包装方式
wait1()
findID(id='package_type_id').find_element_by_xpath("//option[@value='A7AD3545-AD83-544B-8F36-22CC1E5FFE1B']") #选择包装尺寸
wait1()
findXpath(xpath='/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[3]/div[2]/div[2]/div').click() #单击新增尺寸按钮
wait1()
findID(id='package-type-length').send_keys('1000') #输入长
findID(id='package-type-width').send_keys('800') #输入宽
findID(id='package-type-height').send_keys('500') #输入高
findID(id='add-package-type').click() #单击确定按钮
wait1()
findID(id='package_suttle_weight').send_keys('100') #输入净重
findID(id='package_rough_weight').send_keys('105') #输入毛重
wait1()
findXpath(xpath='/html/body/div[3]/div[2]/div/div[3]/div').click() #单击保存按钮
wait1()
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/a[1]/span').click() #单击包装待添加按钮
wait1()
findID(id='package_type_num').clear() #清除箱号
findID(id="package_type_num").send_keys('1-1') #输入新箱号
findID(id='package_item_note').send_keys('配件') #输入货物说明
findID(id='package_type_code').find_element_by_xpath("//option[@value='1']").click() #选择包装方式
wait1()
findID(id='package_type_id').find_element_by_xpath("//option[@value='A7AD3545-AD83-544B-8F36-22CC1E5FFE1B']") #选择包装尺寸
wait1()
findXpath(xpath='/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[3]/div[2]/div[2]/div').click() #单击新增尺寸按钮
wait1()
findID(id='package-type-length').send_keys('1000') #输入长
findID(id='package-type-width').send_keys('800') #输入宽
findID(id='package-type-height').send_keys('500') #输入高
wait1()
findID(id='add-package-type').click() #单击确定按钮
wait1()
findID(id='package_suttle_weight').send_keys('100') #输入净重
findID(id='package_rough_weight').send_keys('105') #输入毛重
wait1()
findXpath(xpath='/html/body/div[3]/div[2]/div/div[3]/div').click() #单击保存按钮
wait1()
findXpath(xpath='/html/body/div[2]/div[2]/div/div[3]/div').click() #单击提交按钮
wait3()
