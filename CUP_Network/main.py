from QuickProject.Commander import Commander
from QuickProject import QproDefaultConsole

app = Commander()


@app.command()
def login():
    """
    利用 selenium 自动登录校园网
    """
    from . import login

    with QproDefaultConsole.status("正在登录校园网..."):
        login()


@app.command()
def logout():
    """
    利用 selenium 自动登出校园网
    """
    from . import logout

    with QproDefaultConsole.status("正在登出校园网..."):
        logout()


@app.command()
def reset():
    """
    重置校园网账号密码
    """
    from .__config__ import init_config

    init_config()


@app.command()
def config(key: str, value: str = None):
    """
    操作配置表
    """
    from . import config

    if value is None:
        QproDefaultConsole.print(key, config.select(key))
    else:
        config.update(key, value)


@app.command()
def doc():
    """
    文档
    """
    QproDefaultConsole.print(
        "[bold cyan][CUP_Network][/]", "CUP校园网命令工具", justify="center"
    )
    QproDefaultConsole.print("[bold]作者: RhythmLian[/]\n", justify="center")
    QproDefaultConsole.print(
        """\
在无桌面系统中，推荐使用docker部署selenuim，再使用此工具。大致步骤如下:

1. 安装docker
2. 运行命令: "docker run -d -p <某个端口号>:4444 --shm-size=2g selenium/standalone-chrome"
3. 初次运行 "cup-network" 会自动引导进行配置。
   1. 命令: "cup-network config <key> \[value]" 可以修改配置。
      对于 "value" 参数: 不填写表示查询, 设置为 [bold magenta]None[/] 表示删除此项。
   2. 命令: "cup-network config docker-url http://<IP或域名>:<某个端口号>/wd/hub" 可设置使用docker selenium 
      (1) 注意: <某个端口号> 为第二步中的端口号
      (2) 注意: <IP或域名> 为服务器的IP或域名
                服务器非本机的情况下，需要保证服务器与本机在同一局域网内。"""
    )


@app.command()
def status():
    """
    查看校园网状态
    """
    from . import status

    status()


def main():
    """
    注册为全局命令时, 默认采用main函数作为命令入口, 请勿将此函数用作它途.
    When registering as a global command, default to main function as the command entry, do not use it as another way.
    """
    app()


if __name__ == "__main__":
    main()
