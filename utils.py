import random
import threading
import time
import os
import subprocess
from wxpy import *

bot = Bot(console_qr=2,cache_path=True)

tuling = Tuling(os.environ['TULING'])

def genRandom(total, num, result=None):
  if (result == None):
    return genRandom(total*100, num, [])
  if (num == 1):
    result.append(total)
    result = [x/100 for x in result]
    return str(result) + " , 共 " + str(sum(result))
  else:
    part = int(total / num)
    rand = random.randint(-220,299)
    current = part+rand
    result.append(current)
    return genRandom(total-current, num-1, result)


def send_online_notification(name):
    global bot
    my_friend = ensure_one(bot.search(name))
    while True:
        my_friend.send('Hello!') # 你想发送的消息
        time.sleep(10) # 一小时后在进行发送

def find(name, content=None):
    global bot
    if (content == None):
        return ensure_one(bot.search(name))
    return find(name, None).send(content)
# positiveSendingThread = threading.Thread(target=send_online_notification, args=('th',)) 
# positiveSendingThread.setDaemon(True)
# positiveSendingThread.start()

def eval_msg(msg):
    code = msg.split('eval')[1].lstrip()
    with open('temp_code.py','w') as f:
        f.write(code)
    cmd = 'python ./temp_code.py'
    x = subprocess.check_output(['bash','-c', cmd])
    return x.lstrip().rstrip().decode('UTF-8')

def bash_msg(msg):
    code = msg.split('bash')[1].lstrip()
    x = subprocess.check_output(['bash','-c', code])
    return x.lstrip().rstrip().decode('UTF-8')

def calc_msg(msg):
    code = msg.split('calc')[1].lstrip()
    return eval(code)


