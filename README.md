# SoftwareTest

[![Build Status](https://travis-ci.com/ljw9609/SoftwareTest.svg?token=rZsycNAAqukSyU9AujYH&branch=master)](https://travis-ci.com/ljw9609/SoftwareTest)
[![codecov](https://codecov.io/gh/ljw9609/SoftwareTest/branch/master/graph/badge.svg?token=O8Yc1DrOUw)](https://codecov.io/gh/ljw9609/SoftwareTest)

上海交通大学软件学院*SE213软件测试*课程作业

## 目录
+ 作业一：黑盒测试
+ 作业二：白盒测试(branch master)
+ 作业三：GUI测试(brance guitest)

### 作业二
测试原程序为Python简单日历，输入年份，打印出该年份的日历。使用UnitTest进行单元测试，总体测试覆盖率为87%。项目在[Travis](https://travis.ci.com)持续集成和测试，测试覆盖率工具使用[Codecov](https://github.com/codecov)。

### 作业三
maven项目自动安装依赖，不过需要下载自己浏览器对应版本的驱动。测试代码在test目录下，只要修改自己的参数就能跑，TestNG作为整体测试框架，Selenium作为GUI测试框架。测试网站为[Elearning-Platform](http://elearning.se.sjtu.edu.cn/)中的个人资料页面，测试了超链接、文本框、单选按钮、选择器、多选框、文件上传、alert弹窗验证。