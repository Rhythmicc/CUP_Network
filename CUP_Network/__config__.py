import os
import json
import base64
from QuickProject import user_root, _ask, QproDefaultConsole, QproInfoString

config_path = os.path.join(user_root, '.cup-network')

problems = {
    'username': {
        'type': 'input',
        'name': 'username',
        'message': '请输入校园网账号',
    },
    'password': {
        'type': 'password',
        'name': 'password',
        'message': '请输入校园网密码',
    }
}


def encode_password(password):
    return base64.b64encode(password.encode('utf-8')).decode('utf-8')


def decode_password(password):
    return base64.b64decode(password.encode('utf-8')).decode('utf-8')


def init_config():
    with open(config_path, 'w') as f:
        json.dump(
            {
                'username': encode_password(_ask(problems['username'])),
                'password': encode_password(_ask(problems['password'])),
            }, f, indent=4, ensure_ascii=False
        )
    QproDefaultConsole.print(QproInfoString, f'您的校园网账号和密码已加密保存在 "{config_path} 中!"')


class CUPNetworkConfig:
    def __init__(self):
        if not os.path.exists(config_path):
            init_config()
        with open(config_path, 'r') as f:
            self.config = json.load(f)

    def select(self, item):
        if item not in self.config and item in problems:
            self.update(item, encode_password(_ask(problems[item])))
        return decode_password(self.config[item])

    def update(self, key, value):
        self.config[key] = value
        with open(self.config_path, 'w') as f:
            json.dump(self.config, f, indent=4, ensure_ascii=False)
