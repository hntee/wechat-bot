from wxpy import *
from utils import *

bot = Bot(console_qr=2,cache_path=True)

@bot.register(None, TEXT)
def auto_reply(msg):
    # 回复消息内容和类型
    txt = msg.text
    print(msg.id, msg.text, msg.type, msg.raw['MsgType'])

    if ('浦发' in txt):
        total, num = 70, 5
        return genRandom(total,num)
    if ('华夏' in txt):
        total, num = 120, 2
        return genRandom(total,num)
    # 如果是群聊，但没有被 @，则不回复
    # if isinstance(msg.chat, Group) and not msg.is_at:
    #     return
    # else:


@bot.register(msg_types=NOTE)
def get_revoked(msg):
    print(msg.id, msg.text, msg.type, msg.raw['MsgType'])
    # 检查 NOTE 中是否有撤回信息
    revoked = ETree.fromstring(msg.raw['Content']).find('revokemsg')
    if revoked:
        # 根据找到的撤回消息 id 找到 bot.messages 中的原消息
        revoked_msg = bot.messages.search(id=int(revoked.find('msgid').text))[0]
        # 原发送者 (群聊时为群员)
        sender = msg.member or msg.sender
        # 把消息转发到文件传输助手
        revoked_msg.forward(
            bot.file_helper,
            prefix=msg
        )
        
embed()
