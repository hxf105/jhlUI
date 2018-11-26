from jhlUI_Test.BasicFunction import *
#供应商登录，进行备货操作
role_s()
login_s1()
findXpath(xpath='//*[@id="common-leftmenu"]/ul/li[2]/div[1]/a/span[2]').click() #单击订单菜单
wait3()
findXpath(xpath='//*[@id="common-leftmenu"]/ul/li[2]/div[2]/ul/li[1]/a').click() #单击进行中的订单菜单
wait3()
findID(id='title').send_keys('中交一公局钢材采购') #输入查询条件：任务单名称“中交一公局钢材采购”
findID(id='order_search').click() #单击搜索按钮
wait3()
findXpath(xpath='//*[@id="order-table"]/tbody/tr[2]/td/div/span').click() #单击新增备货信息按钮
wait3()
# 上传产品授权书
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[2]/div[1]/label/input').send_keys('F:/测试执行资料库/文档/支持/河北廊坊新机场北线高速公路廊坊段项目物资采购合同.docx')
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[2]/div[1]/label/input').send_keys('F:/测试执行资料库/文档/支持/供应商管理.doc')
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[2]/div[1]/label/input').send_keys('F:/测试执行资料库/文档/支持/product-introduction-template.xls')
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[2]/div[1]/label/input').send_keys('F:/测试执行资料库/文档/支持/大型泵体采购任务一期货物信息表.xlsx')
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[2]/div[1]/label/input').send_keys('F:/测试执行资料库/文档/支持/yrdy.wps')
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[2]/div[1]/label/input').send_keys('F:/测试执行资料库/文档/支持/萌兴工程有限公司三亚大桥支座伸缩缝招标采购.pdf')
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[2]/div[1]/label/input').send_keys('F:/测试执行资料库/新图/tim0g.jpg')
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[2]/div[1]/label/input').send_keys('F:/测试执行资料库/新图/timg (1).jpeg')
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[2]/div[1]/label/input').send_keys('F:/测试执行资料库/新图/timg (3).png')
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[2]/div[1]/label/input').send_keys('F:/测试执行资料库/新图/timg (16).jpg')
wait5()
# 上传原厂出库单
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/div[3]/div[2]/div[1]/label/input').send_keys('F:/测试执行资料库/新图/tim0g.jpg')
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/div[3]/div[2]/div[1]/label/input').send_keys('F:/测试执行资料库/新图/timg (1).jpeg')
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/div[3]/div[2]/div[1]/label/input').send_keys('F:/测试执行资料库/新图/timg (3).png')
wait5()
# 上传产品图片
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/div[4]/div[2]/div[1]/label/input').send_keys('F:/测试执行资料库/新图/tim0g.jpg')
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/div[4]/div[2]/div[1]/label/input').send_keys('F:/测试执行资料库/新图/timg (1).jpeg')
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/div[4]/div[2]/div[1]/label/input').send_keys('F:/测试执行资料库/新图/timg (3).png')
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/div[4]/div[2]/div[1]/label/input').send_keys('F:/测试执行资料库/新图/timg (10).jpg')
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/div[4]/div[2]/div[1]/label/input').send_keys('F:/测试执行资料库/新图/timg (11).jpg')
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/div[4]/div[2]/div[1]/label/input').send_keys('F:/测试执行资料库/新图/timg (13).jpg')
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/div[4]/div[2]/div[1]/label/input').send_keys('F:/测试执行资料库/新图/timg (14).jpg')
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/div[4]/div[2]/div[1]/label/input').send_keys('F:/测试执行资料库/新图/timg (15).jpg')
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/div[4]/div[2]/div[1]/label/input').send_keys('F:/测试执行资料库/新图/timg (16).jpg')
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/div[4]/div[2]/div[1]/label/input').send_keys('F:/测试执行资料库/新图/timg (17).jpg')
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/div[4]/div[2]/div[1]/label/input').send_keys('F:/测试执行资料库/新图/timg (18).jpg')
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/div[4]/div[2]/div[1]/label/input').send_keys('F:/测试执行资料库/新图/timg (19).jpg')
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/div[4]/div[2]/div[1]/label/input').send_keys('F:/测试执行资料库/新图/timg (20).jpg')
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/div[4]/div[2]/div[1]/label/input').send_keys('F:/测试执行资料库/新图/timg (21).jpg')
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/div[4]/div[2]/div[1]/label/input').send_keys('F:/测试执行资料库/新图/timg (22).jpg')
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/div[4]/div[2]/div[1]/label/input').send_keys('F:/测试执行资料库/新图/timg (23).jpg')
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/div[4]/div[2]/div[1]/label/input').send_keys('F:/测试执行资料库/新图/timg (24).jpg')
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/div[4]/div[2]/div[1]/label/input').send_keys('F:/测试执行资料库/新图/timg (26).jpg')
wait15()
findID(id='remark').send_keys('备货信息，请审核，pyselenium') #输入备注
wait3()
findXpath(xpath='//*[@id="show_item_list"]/thead/tr/th[1]/div[1]/input').click() #点击货物全选按钮
findXpath(xpath='//*[@id="show_item_list"]/tbody/tr[2]/td[6]/div/input').clear()
findXpath(xpath='//*[@id="show_item_list"]/tbody/tr[2]/td[6]/div/input').send_keys('10')
wait3()
findXpath(xpath='/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[2]/div[2]/div[1]/div[2]/div[4]/div[2]/ul/li[9]/a').click()
wait3()
findXpath(xpath='//*[@id="show_item_list"]/thead/tr/th[1]/div[1]/input').click() #点击货物全选按钮
wait3()
findXpath(xpath='/html/body/div[2]/div[2]/div/div[3]/div[2]').click() #单击提交按钮,提交备货信息
wait3()
findID(id='title').send_keys('中交一公局钢材采购') #输入查询条件：任务单名称“中交一公局钢材采购”
wait3()
findID(id='order_search').click() #单击搜索按钮
wait3()




