from wxpy import *
from utils import *
from xml.etree import ElementTree as ETree
import collections

tuling_on = True

stop_words = ['shutup','别吵','闭嘴', 'exit', '886', '88']
start_words = ['出来吧']
allow_reply_config = collections.defaultdict(bool)

farewell = "886"

def contains(txt, words):
    for w in words:
        if w in txt:
            return True
    return False

@bot.register(None, TEXT)
def auto_reply(msg):
    # 回复消息内容和类型
    global allow_reply_config
    print(msg, msg.type, msg.raw['MsgType'])
    if ('浦发' in txt):
        total, num = 70, 5
        return genRandom(total,num)
    if ('华夏' in txt):
        total, num = 120, 2
        return genRandom(total,num)
    if isinstance(msg.chat, Group) and msg.is_at:
        tuling.do_reply(msg)
        return 
    if isinstance(msg.chat, Group) and not msg.is_at:
        return

    tuling.do_reply(msg)
        
    # 如果是群聊，但没有被 @，则不回复
    # if isinstance(msg.chat, Group) and not msg.is_at:
    #     return
    # else:


@bot.register(msg_types=NOTE)
def note_handler(msg):
    msg_type = msg.raw['MsgType']
    forwarder = find('qwer')
    print(msg.id, msg.text, msg.type, msg_type)

    # 10000 红包
    # 10002 撤回
    # 49 转账

    if msg_type == 10000: # 红包
        forwarder.send(msg)
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
