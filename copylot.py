import os
import io
import time
import base64
import logging

import win32gui
import win32process

import cv2
import yaml
import psutil
import pynput
import requests
import psd_tools
import numpy as np
from pynput.keyboard import Key, Controller

from rimo_utils.计时 import 计时


设置文件 = 'p.yaml'
psd文件 = '1.psd'

默认设置 = {
    'cfg_scale': 7,
    'steps': 25,
    'seed': 1,
}

边长限制 = 640

API = 'http://localhost:7860/sdapi/v1/img2img'


def 当前窗口() -> str:
    hwnd = win32gui.GetForegroundWindow()
    threadid, pid = win32process.GetWindowThreadProcessId(hwnd)
    try:
        exe = psutil.Process(pid).exe()
    except Exception:
        exe = ''
    return exe

_上次修改时间 = 0

当前按键 = {}
pynput.keyboard.Listener(
    on_press=lambda x: 当前按键.setdefault(x, time.time()),
    on_release=lambda x: 当前按键.pop(x, None),
).start()
keyboard_controller = Controller()
上次保存时间 = 0
while True:
    try:
        上次修改时间 = max(os.path.getmtime(设置文件), os.path.getmtime(psd文件))
        if 上次修改时间 > _上次修改时间 + 0.00001:
            with 计时('预处理'):
                setting = yaml.safe_load(open(设置文件))
                p = psd_tools.PSDImage.open(psd文件)
                bo = io.BytesIO()
                p.topil().save(bo, format='WEBP')
                b = bo.getvalue()
                img_base64 = base64.b64encode(b).decode('utf-8')
            with 计时('调用'):
                设置 = 默认设置 | {'init_images': [img_base64]} | setting
                if not 设置.get('width'):
                    设置['width'] = p.width
                if not 设置.get('height'):
                    设置['height'] = p.height
                if max(设置['width'], 设置['height']) > 边长限制:
                    if 设置['width'] > 设置['height']:
                        设置['height'] = int(设置['height'] * 边长限制 / 设置['width'])
                        设置['width'] = 边长限制
                    else:
                        设置['width'] = int(设置['width'] * 边长限制 / 设置['height'])
                        设置['height'] = 边长限制
                r = requests.post(url=f'{API}', json=设置)
            with 计时('后处理'):
                图 = [base64.b64decode(b64) for b64 in r.json()['images']][0]
                img = cv2.imdecode(np.frombuffer(图, dtype=np.uint8), cv2.IMREAD_COLOR)
            _上次修改时间 = 上次修改时间
    except Exception:
        logging.exception('奇怪！')
        time.sleep(0.5)
    t = time.time()
    for k, v in [*当前按键.items()]:
        if not isinstance(k, Key) and (not k.char or k.char <= '\x1f'):   # 组合键有时候会多出奇怪的字符，我也不知道为什么
            当前按键.pop(k, None)
        if t - v > 10:
            当前按键.pop(k, None)
    if 当前窗口().lower().endswith('photoshop.exe') and not 当前按键:
        t = time.time()
        if t - 上次保存时间 > 0.5:
            上次保存时间 = t
            keyboard_controller.press(Key.ctrl_l.value)
            keyboard_controller.press('s')
            keyboard_controller.release('s')
            keyboard_controller.release(Key.ctrl_l.value)
    cv2.imshow('', img)
    cv2.waitKey(1)
