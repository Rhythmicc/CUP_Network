const completionSpec: Fig.Spec = {
    "name": "CUP_Network",
    "description": "CUP_Network",
    "subcommands": [
        {
            "name": "--help",
            "description": "获取帮助"
        },
        {
            "name": "login",
            "description": "利用 selenium 自动登录校园网",
            "args": [],
            "options": []
        },
        {
            "name": "logout",
            "description": "利用 selenium 自动登出校园网",
            "args": [],
            "options": []
        },
        {
            "name": "reset",
            "description": "重置校园网账号密码",
            "args": [],
            "options": []
        },
        {
            "name": "init",
            "description": "在Ubuntu上自动安装 google-chrome 和 chromedriver",
            "args": [],
            "options": []
        }
    ]
};
export default completionSpec;
