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
            "name": "config",
            "description": "操作配置表",
            "args": [
                {
                    "name": "key",
                    "description": "<key>"
                },
                {
                    "name": "value",
                    "description": "<value>"
                }
            ],
            "options": []
        },
        {
            "name": "doc",
            "description": "文档",
            "args": [],
            "options": []
        },
        {
            "name": "status",
            "description": "查看校园网状态",
            "args": [],
            "options": []
        }
    ]
};
export default completionSpec;
