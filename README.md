# CUP_Network

利用selenium自动登录和登出CUP的校园网

## 安装

```sh
pip3 install CUP_Network
```

## 使用

获取帮助: `cup-network --help`

### 子命令

| 子命令  | 样例                           | 描述        |
| -------- | ------------------------------ | ------------------ |
| login | `cup-network login <username> <password>` | 登录 |
| logout | `cup-network logout` | 登出 |
| init | `cup-network init` | 自动在Ubuntu上安装chrome driver |
