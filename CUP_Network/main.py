from QuickProject.Commander import Commander
from QuickProject import QproDefaultConsole


app = Commander()


@app.command()
def login(username: str, password: str):
    """
    利用 selenium 自动登录校园网

    :param username: 校园网账号
    :param password: 校园网密码
    """
    from . import login
    with QproDefaultConsole.status('正在登录校园网...'):
        login(username, password)


@app.command()
def logout():
    """
    利用 selenium 自动登出校园网
    """
    from . import logout
    with QproDefaultConsole.status('正在登出校园网...'):
        logout()


@app.command()
def init():
    """
    在Ubuntu上自动安装 google-chrome 和 chromedriver
    """
    import os
    os.system('sudo apt-get install google-chrome-stable')
    os.system('sudo apt-get install chromium-chromedriver')


def main():
    """
    注册为全局命令时, 默认采用main函数作为命令入口, 请勿将此函数用作它途.
    When registering as a global command, default to main function as the command entry, do not use it as another way.
    """
    app()


if __name__ == '__main__':
    main()
