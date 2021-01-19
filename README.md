# gitlab-issue-spend-time

------
[![MIT](https://img.shields.io/badge/license-MIT-000000.svg)](LICENSE) [![34782655](https://img.shields.io/badge/QQ-@34782655-red.svg)](http://wpa.qq.com/msgrd?v=3&uin=34782655&site=qq&menu=yes)

## **主要功能**

> 一个基于Python3+Flask的gitlab issues spend time统计项目。通过请求`gitlab API`，获取gitlab中issue notes数据并封装为自己需要的格式，最终提供数据接口。

:heavy_exclamation_mark::heavy_exclamation_mark: 目前只支持统计以`h`为单位的spend，如：`/spend 7h`。

**:dart:请求：**

GET：`http://127.0.0.1:5000/getDatas`

**:dart:响应：**

```json

{
  "2021-01-05": [
    {
      "name": "张三",
      "avatar_url": "https://avatar-stl.gitlab.com/email/zhangshan/avatar.png",
      "time": 7
    }，
    {
      "name": "李四",
      "avatar_url": "https://avatar-stl.gitlab.com/email/lisi/avatar.png",
      "time": 7
    }
  ],
  “2021-01-06”: [
      ...
  ],
  ....
}
```



## **License**

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT) - see the [`LICENSE`](https://github.com/yinyicao/gitlab-issue-spend-time/blob/main/LICENSE) file for details. 