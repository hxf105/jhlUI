from selenium import webdriver
driver=webdriver.Chrome()
driver.maximize_window()

# driver.set_window_size(1366,768)   #设置窗口大小
import time as t
def wait1():
    t.sleep(1)
def wait2():
    t.sleep(2)
def wait3():
    t.sleep(3)
def wait5():
    t.sleep(5)
def wait7():
    t.sleep(7)
def wait10():
    t.sleep(10)
def wait15():
    t.sleep(15)
def wait20():
    t.sleep(20)
# driver.implicitly_wait(10)

def role_b():
    global driver
    driver.get('http://buyer19.jiaohuilian.com/')
    wait3()
def role_s():
    global driver
    driver.get('http://front19.jiaohuilian.com/site/login')
    wait3()
def role_a():
    global driver
    driver.get('http://agent19.jiaohuilian.com/html/web-login.html')
    wait3()
# 问题记录：如何打开一个新的标签页？

def findID(id):
    global driver
    d=driver.find_element_by_id(id)
    return d
def findName(name):
    global driver
    d=driver.find_element_by_name(name)
    return d
def findClassName(name):
    global driver
    d=driver.find_element_by_class_name(name)
    return d
def findTagName(name):
    global driver
    d=driver.find_element_by_tag_name(name)
    return d
def findLinkText(text):
    global driver
    d=driver.find_element_by_link_text(text)
    return d
def findPLinkText(text):
    global driver
    d=driver.find_element_by_partial_link_text(text)
    return d
def findXpath(xpath):
    # global driver
    global driver
    d=driver.find_element_by_xpath(xpath)
    return d
def findCss(css):
    global driver
    d=driver.find_element_by_css_selector(css)
    return d

# 采购商登入
def login_b(username,password):
    findID(id='uname').clear()
    findID(id='uname').send_keys(username)
    findID('psd').clear()
    findID(id='psd').send_keys(password)
    wait1()
    findXpath(xpath='/html/body/div[1]/div/div/div[2]/div/div[2]/div[1]/div[1]/form/button').click()  # 单击登录按钮
    wait3()
def login_b1():
    return login_b(username='18292678346',password='123456')
def login_b2():
    return login_b(username='18189134680',password='123456')
def login_b3():
    return login_b(username='18629612156',password='123456')
def login_b4():
    return login_b(username='18576614172',password='123456')

# 供应商登入
def login_s(username,password):
    findID(id='loginform-username').clear()
    findID(id='loginform-username').send_keys(username)
    findID(id='loginform-password').clear()
    findID(id='loginform-password').send_keys(password)
    wait1()
    findXpath(xpath='//*[@id="login-form"]/div/div[4]/div/button').click()
    wait3()

def login_s1():
    return login_s(username='19945239622',password='123456')

# 货代登入
def login_a(username,password):
    findID(id='uname').clear()
    findID(id='uname').send_keys(username)
    findID(id='psd').clear()
    findID(id='psd').send_keys(password)
    wait1()
    findXpath(xpath='/html/body/div/div/div/div[2]/div/div[2]/div[1]/div[1]/form/button').click()
    wait3()
def login_a1():
    return login_a(username='17791615276',password='123456')

# 下拉菜单
def dropDownx(xpath,val):
    findXpath(xpath=xpath).find_element_by_xpath("//option[@value="+val+"]")
def dropDowni(id,val):
    findID(id=id).find_element_by_xpath("//option[@value="+val+"]")

# 删除readonly属性
def js():
    js = "$('input[id=select-date-dom]').removeAttr('readonly')"  # 2.jQuery，移除属性       【成功】
    driver.execute_script(js)

# 退出登入
def quit():
    return findXpath(xpath='//*[@id="menber-menu-list"]/div[2]/span[1]').click()
    wait3()
