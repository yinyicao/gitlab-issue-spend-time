[English](README.md) | 简体中文 

# gitlab-issue-spend-time

------
[![MIT](https://img.shields.io/badge/license-MIT-000000.svg)](LICENSE) [![34782655](https://img.shields.io/badge/QQ-@34782655-red.svg)](http://wpa.qq.com/msgrd?v=3&uin=34782655&site=qq&menu=yes)

## 项目介绍

> 一个基于Python3+Flask的gitlab issues spend time统计项目。通过请求`gitlab API`，获取gitlab中issue notes数据并封装为自己需要的格式，最终提供数据接口。

:heavy_exclamation_mark::heavy_exclamation_mark: 目前只支持统计以`h`为单位的spend，如：`/spend 7h`。

## 安装

该项目使用Python3开发，在此之前你应该安装。

```shell
$ python -V
Python 3.9.1
```

使用命令 `git clone git@github.com:yinyicao/gitlab-issue-spend-time.git`或者 [点击这里](https://github.com/yinyicao/gitlab-issue-spend-time/archive/main.zip) 下载这个项目到本地。

```shell
$ git clone git@github.com:yinyicao/gitlab-issue-spend-time.git
```

根据项目中的`requirements.txt`文件安装依赖。

```shell
$ pip3 install -r requirements.txt
```

## 使用

根据 `main.py`来启动项目，这是该项目的入口文件.

```shell
$ python main.py
```

**:dart:请求：**

GET：`http://127.0.0.1:5000/getDatas` (返回以dict形式的json)or`/spendTimeDatas`(返回以list形式的json).

**:dart:响应：**

```json
{
  "2021-01-05": [
    {
      "name": "张三",
      "avatar_url": "https://avatar-stl.gitlab.com/email/zhangshan/avatar.png",
      "time": 7
    },
    {
      "name": "李四",
      "avatar_url": "https://avatar-stl.gitlab.com/email/lisi/avatar.png",
      "time": 7
    }
  ],
  "2021-01-06": [
      //more...
  ],
  //more....
}
```

## 贡献

随时欢迎你! [提交问题](https://github.com/yinyicao/gitlab-issue-spend-time/issues/new) 或者提交代码。


## 授权

这个项目遵循[MIT开源协议](https://opensource.org/licenses/MIT)-参见[LICENSE](https://github.com/yinyicao/gitlab-issue-spend-time/blob/main/LICENSE)文件以获取详细信息。

