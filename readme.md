# actually very very simple

### 使用说明

直接 bash setup.sh

端口号为5000（可以 "局域网ip:5000"访问）

用户登陆界面输入新账户就是注册，没有反应就说明该账户已存在并且密码不对

查看提交记录只支持查看自己的最后一发提交，其他提交记录需要自己输入提交id来获取

如果修改已经存在的题目，只能修改自己上传的题

上传题目只能使用zip，zip里需要有以下内容：

- titile：一行文本

- stat：题面描述，html格式
（没错，换行要用&lt;br&gt;，没事不要用小于号）

- in：输入数据

- ans：答案文件

- tl：一个实数，时间限制（单位：s）

我也给出了两道题目样例，a_plus_b.zip 和 challenge.zip

不难发现，由于配置文件咕咕咕，现只支持一组测试数据

为了服务器性能，每次题目修改都有一定时间的延时，不要反复提交
