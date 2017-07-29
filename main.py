from wxpy import *
from utils import genRandom

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
        
embed()
