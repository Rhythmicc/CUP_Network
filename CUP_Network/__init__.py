import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.errorhandler import (
    ElementNotInteractableException,
    ElementClickInterceptedException,
)

from .__config__ import CUPNetworkConfig


config = CUPNetworkConfig()
sleep_time = 1


def _get_driver():
    if config.select("docker-url") != "无" and config.select("docker-url") != "":
        from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

        driver = webdriver.Remote(
            command_executor=config.select("docker-url"),
            desired_capabilities=DesiredCapabilities.CHROME,
        )
    else:
        from selenium.webdriver.chrome.options import Options

        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(chrome_options=chrome_options)
    return driver


def login(
    username: str = config.select("username"), password: str = config.select("password")
):
    """
    利用 selenium 自动登录校园网

    :param username: 校园网账号
    :param password: 校园网密码
    :return:
    """
    driver = _get_driver()
    driver.get("http://login.cup.edu.cn")
    time.sleep(sleep_time)
    try:
        driver.find_element(By.ID, "username").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        time.sleep(sleep_time)
        driver.find_element(By.ID, "login").click()
        time.sleep(sleep_time)
    except ElementNotInteractableException:
        from QuickProject import QproDefaultConsole, QproErrorString

        QproDefaultConsole.print(QproErrorString, "无法填入账号密码, 请检查是否已经登录。")
    except Exception as e:
        from QuickProject import QproDefaultConsole

        QproDefaultConsole.print_exception()
    finally:
        driver.close()
        driver.quit()


def logout():
    """
    利用 selenium 自动登出校园网

    :return:
    """
    driver = _get_driver()
    driver.get("http://login.cup.edu.cn/srun_portal_success?ac_id=1&theme=cup")
    time.sleep(sleep_time)
    try:
        driver.find_element(By.ID, "logout-dm").click()
        time.sleep(sleep_time)
    except ElementClickInterceptedException:
        from QuickProject import QproDefaultConsole, QproErrorString

        QproDefaultConsole.print(QproErrorString, "无法点击注销按钮，请检查是否已经登录。")
    except Exception as e:
        from QuickProject import QproDefaultConsole

        QproDefaultConsole.print_exception()
    finally:
        driver.close()
        driver.quit()


def status():
    """
    查看校园网状态

    :return:
    """
    from QuickProject import QproDefaultConsole, QproErrorString, QproInfoString

    driver = _get_driver()
    driver.get("http://login.cup.edu.cn/")
    time.sleep(sleep_time)
    try:
        status = driver.find_elements(By.CLASS_NAME, "info")[1].text
        QproDefaultConsole.print(QproInfoString, f"{status}")
    except Exception as e:
        QproDefaultConsole.print(QproErrorString, "未登录")
    finally:
        driver.close()
        driver.quit()
