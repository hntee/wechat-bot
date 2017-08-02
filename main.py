from wxpy import *
from utils import *
from xml.etree import ElementTree as ETree
from sendmail import sendmail
from th import forward
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
    txt = msg.text
    red_packet_group = find(u"x红包x")
    print(msg, msg.type, msg.raw['MsgType'])

    if ('收到红包' in txt) : # 红包
        forward(msg, red_packet_group)
        return
    if ('calc' in txt):
        return calc_msg(txt)
    if ('.浦发' in txt):
        total, num = 70, 5
        return genRandom(total,num)
    if ('.华夏' in txt):
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
@bot.register(find('th'), TEXT)
def auto_reply(msg):
    # 回复消息内容和类型
    global allow_reply_config
    txt = msg.text
    print(msg, msg.type, msg.raw['MsgType'])
    if ('eval' in txt):
        return eval_msg(txt)
    elif ('bash' in txt):
        return bash_msg(txt)
    elif ('calc' in txt):
        return calc_msg(txt)

    tuling.do_reply(msg)

@bot.register(msg_types=NOTE)
def note_handler(msg):
    msg_type = msg.raw['MsgType']
    msg_time = msg.create_time.strftime("%m-%d %H:%M:%S ")
    red_packet_group = find(u'x红包x')
    revoke_group = find(u"x撤回x")
    print(msg.id, msg.text, msg.type, msg_type)

    # 10000 红包
    # 10002 撤回
    # 49 转账

    if ('收到红包' in msg.text) or ('转账' in msg.text)  : # 红包
        forward(msg, red_packet_group)
        sendmail(str(msg))
    elif ('撤回' in msg.text): # 撤回
        revoked = ETree.fromstring(msg.raw['Content']).find('revokemsg')
        revoked_msg = bot.messages.search(id=int(revoked.find('msgid').text))[0]
        revoked_msg.forward(
                revoke_group,
                prefix=msg
            )
            
embed()
