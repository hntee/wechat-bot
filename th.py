from wxpy import *
from utils import *
from xml.etree import ElementTree as ETree
import collections

def forward(msg, receiver):
    msg_time = msg.create_time.strftime("%m-%d %H:%M:%S ")
    receiver.send(msg_time + str(msg))

@bot.register(find('坚决跟党走'))
def forward_chouma_message(msg):
    print(msg.id, msg.text, msg.type)
    receiver = find('假筹码群')
    forward(msg, receiver)

@bot.register(find('六个小号'))
def forward_chouma_message(msg):
    print(msg.id, msg.text, msg.type)
    receiver = find('另外一个心态')
    forward(msg, receiver)

@bot.register(msg_types=NOTE)
def note_handler(msg):
    msg_type = msg.raw['MsgType']
    forwarder = find('qwer')
    print(msg.id, msg.text, msg.type, msg_type)

    # 10000 红包
    # 10002 撤回
    # 49 转账

    if ('收到红包' in msg.text) or ('转账' in msg.text)  : # 红包
        forwarder.send(msg_time, msg)
    else:
        # 检查 NOTE 中是否有撤回信息
        revoked = ETree.fromstring(msg.raw['Content']).find('revokemsg')
        if revoked:
            # 根据找到的撤回消息 id 找到 bot.messages 中的原消息
            revoked_msg = bot.messages.search(id=int(revoked.find('msgid').text))[0]
            # 原发送者 (群聊时为群员)
            sender = msg.member or msg.sender
            # 把消息转发到文件传输助手
            revoked_msg.forward(
                forwarder,
                prefix=msg
            )
            
embed()
