English | [简体中文](README.zh-CN.md) 

# gitlab-issue-spend-time

------
[![MIT](https://img.shields.io/badge/license-MIT-000000.svg)](LICENSE) [![34782655](https://img.shields.io/badge/QQ-@34782655-red.svg)](http://wpa.qq.com/msgrd?v=3&uin=34782655&site=qq&menu=yes)

## Introductions

> A gitlab issues spend time statistical project based on Python3+Flask. By requesting the `gitlab API`, obtain the issue notes data in gitlab and encapsulate it in the format you need, and finally provide a data interface.

:heavy_exclamation_mark::heavy_exclamation_mark: Currently only supports statistics of spend with `h` as the unit, such as：`/spend 7h`。

## Install

This project use python3. Go check them out if you don't have them locally installed.

```shell
$ python -V
Python 3.9.1
```

Then, use the `git clone git@github.com:yinyicao/gitlab-issue-spend-time.git` command or [click here](https://github.com/yinyicao/gitlab-issue-spend-time/archive/main.zip) to download the project.

```shell
$ git clone git@github.com:yinyicao/gitlab-issue-spend-time.git
```

Install dependencies.

```shell
$ pip3 install -r requirements.txt
```

## Usage

Now! You can start the project with `main.py`.

```shell
$ python main.py
```


**:dart:Request：**

GET：`http://127.0.0.1:5000/getDatas` (return json of dict)or`/spendTimeDatas`(return json of list).

**:dart:Response：**

```json
{
  "2021-01-05": [
    {
      "name": "zs",
      "avatar_url": "https://avatar-stl.gitlab.com/email/zhangshan/avatar.png",
      "time": 7
    },
    {
      "name": "ls",
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

## Contributing

Feel free to dive in! [Open an issue](https://github.com/yinyicao/gitlab-issue-spend-time/issues/new) or submit PRs.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT) - see the [`LICENSE`](https://github.com/yinyicao/gitlab-issue-spend-time/blob/main/LICENSE) file for details. 
