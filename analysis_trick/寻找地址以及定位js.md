### 寻找登录的post地址

- 在form表单中寻找action对应的url地址

  - post的数据是input标签中name的值作为键，真正的填写的表单信息作为值得字典，post的url地址就是action对应的url地址

- 抓包，寻找登录的url地址

  - 勾选perserve log选框，防止页面跳转后之前的url地址消失
  - 寻找post数据，确定参数

    - 参数不会变，直接用，比如密码不是动态加密的情况下
    - 参数会变

        - 参数在当前的响应中
        - 通过js生成

### 定位相应的js

- 选择会触发的js事件按钮，选择event listener,找到js的位置
- 通过chrome中的search all file来全局搜索url中的关键字
- 添加断点的方式来查看js的操作，通过python来模拟相同的操作