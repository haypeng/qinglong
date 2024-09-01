import os.path
import notify


def start():
    with open('sys.info', 'r', encoding='utf-8') as f:
        info = f.read()
        print(info)
        # QLAPI.notify('服务器状态', info)


if __name__ == '__main__':
    if not os.path.exists('sys.info'):
        exit()
    start()
