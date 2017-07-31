from wxpy import *
from utils import *
from xml.etree import ElementTree as ETree
from sendmail import sendmail
import collections

def forward(msg, receiver):
    msg_time = msg.create_time.strftime("%m-%d %H:%M:%S ")
    receiver.send(msg_time + str(msg))


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
