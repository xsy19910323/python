#登录界面相关的UI  login page
LOGIN_LINK="link text=登录"
LOGIN_USER="css selector=input.el-input__inner"
LOGIN_PWD="xpath=//input[@type='password']"
LOGIN_BTN="id=login"


#创建接口相关的UI
CREATE_API="xpath=//*[@title='新建接口']"
CREATE_API_NAME="css selector=div.el-form-item__content > div.el-input.el-input--small > input.el-input__inner"
SELECT_PORT="xpath=//*[@id='interfaceBasicInfo']/div[3]/div/div/div[1]/div[1]/input"
CREATE_API_PATH="css selector=div.row.el-row > div.el-form-item > div.el-form-item__content > div.el-input.el-input--small > input.el-input__inner"
CREATE_API_SAVEBTN="xpath=//*[@id='btnSave']/div/button/span/span[contains(text(), '保存')]"
CREATE_API_BODYRAW="id=bodyRaw"
CREATE_API_VALUEASSIGNMENT="xpath=(.//*[normalize-space(text()) and normalize-space(.)='JAVASCRIPT'])[1]/following::span[1]"
CREATE_API_RAWCONTENT="xpath=(.//*[normalize-space(text()) and normalize-space(.)='Raw文本内容'])[1]/following::textarea[1]"
CREATE_API_RAWCONTENT_SAVEBTN="xpath=(.//*[normalize-space(text()) and normalize-space(.)='Raw文本内容'])[1]/following::button[2]"
CREATE_API_RUNBTN="xpath=.//*[@id='interfaceContent']/div/div/div/button/span[contains(text(), '运行')]"
CREATE_API_RUN_URL="xpath=(//input[@type='text'])[5]"



