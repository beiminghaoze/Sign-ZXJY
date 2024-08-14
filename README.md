# 职校家园实习汇报自动填写

## 项目来源
本项目基于 [zycn0910/Sign-ZXJY](https://github.com/zycn0910/Sign-ZXJY) 进行修改。

## 修改内容
针对原项目，我们进行了以下修改：

1. **手动填写坐标**：在运行 `AddUser.py` 前，请在文件的第26行和第29行修改坐标。注意使用 `@` 符号。如果运行后出现错误，属于正常现象。只需检查 `all-users.json` 是否有内容，并且结构与原项目的 `user.json` 说明一致即可。
2. **取消打卡功能**：本项目移除了打卡调用，仅保留了提交汇报的功能。
3. **配置文件更新**：`config.yml` 中的 `gpturl` 已更新为 `https://api.xeduapi.com/v1` 如需获取key，请访问 [注册页面](https://xeduapi.com/register?aff=2fbE)。
4. **月报功能**：目前月报功能尚未测试，因此在 `config.yml` 中 `month_report` 设置为 `False`。
5. **日期优化**：每周周一到周五提交日报、周六提交本周的周报，每月月底最后一天提交月报。


## 项目说明

1. **开源协议**：本项目遵循 [GPL3.0开源协议](https://www.gnu.org/licenses/gpl-3.0.zh-cn.html)。
2. **使用限制**：本项目仅供学习使用，请在下载后24小时内删除所有项目内容。
3. **反对违规使用**：我们不鼓励、不赞成、不支持使用任何违规方式完成实习和打卡任务。鉴于项目特殊性，开发者可能随时停止更新或删除项目。
4. **风险声明**：使用本项目可能导致职校家园账号被封禁或其他后果，与作者无关。使用即表示同意。
5. **责任自负**：使用本项目可能产生的后果由使用者本人承担，与项目作者无关。使用即表示同意。
6. **二次开发声明**：若基于或参考此项目进行二次开发，请注明原作者并遵循 GPL3.0 许可证。

## 使用教程

1.**更新**
```pip install -i https://mirrors.aliyun.com/pypi/simple --upgrade pip```

2.**安装所需依赖**
```pip install -i https://mirrors.aliyun.com/pypi/simple -r requirements.txt ```

3.**添加用户**
`python AddUser.py`

4.**主程序运行**
`python Main.py`


更多使用教程请参考原项目 [zycn0910/Sign-ZXJY](https://github.com/zycn0910/Sign-ZXJY)