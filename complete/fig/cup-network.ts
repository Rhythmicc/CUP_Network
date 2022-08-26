const completionSpec: Fig.Spec = {
 "name": "cup-network",
 "description": "CUP校园网助手",
 "subcommands": [
  {
   "name": "--help",
   "description": "获取帮助"
  },
  {
   "name": "login",
   "description": "利用 selenium 自动登录校园网",
   "args": [
    {
     "name": "username",
     "description": "校园网账号"
    },
    {
     "name": "password",
     "description": "校园网密码"
    }
   ],
   "options": []
  },
  {
   "name": "logout",
   "description": "利用 selenium 自动登出校园网",
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
