from slackclient import SlackClient
import time


class slackMsg(object):

    def __init__(self):
        self.sl = SlackClient('xoxb-505197755744-505914604979-WLDuicOTjymw3FTUA3s7f3oB')
        self.inpu = [{'type': 'message', 'user': 'UEVTGF2HY', 'text': 'hello python',
                      'client_msg_id': '5fa911bf-90e4-4e74-a38f-9c070cc1ad2c', 'team': 'TEV5TN7MW',
                      'channel': 'DEX23LF2B',
                      'event_ts': '1545102036.001000', 'ts': '1545102036.001000'}]
        self.botID = 'UEVTGF2HY'  # more like an app ID
        self.bot_id_real_confirmed_twice = 'BEXCCNHNJ'
        self.appName = 'botApp'
        self.botName = 'bot'
        self.myName = 'le.wy'
        self.myID = 'UEVTGF2HY'

    def slackConnect(self):
        return self.sl.rtm_connect()

    def slackReadRTM(self):
        return self.sl.rtm_read()

    def parseSlackInputTrue(self, inpu, botID):
        if inpu and len(inpu) > 0:
            inpu = inpu[0]
            if 'text' in inpu and 'user' in inpu:
                msg = inpu['text']
                usr = inpu['user']
                cha = inpu['channel']
                if botID == usr:
                    print("user in input string ! " + usr)
                    print("text in input string ! " + msg)
                    print("channel in input string ! " + cha)
                    return True
                else:
                    print('botID not found...')
                    return False

            else:
                print('botID not found...')
                return False

    def parseSlackInput(self, inpu, botID):
        if inpu and len(inpu) > 0:
            inpu = inpu[0]
            # print(inpu)
            if 'text' in inpu and 'user' in inpu:
                msg = inpu['text']
                usr = inpu['user']
                cha = inpu['channel']
                if botID == usr:
                    # print("user in input string ! " + usr)
                    # print("text in input string ! " + msg)
                    # print("channel in input string ! " + cha)
                    # print("msg: " + msg)
                    return [str(usr), str(msg), str(cha)]
                else:
                    # print('botID not found...')
                    return [None, None, None]
            else:
                # print('parse: text or user not in...')
                return [None, None, None]
        else:
            # print('parse: input Not > 0...')
            return [None, None, None]

    def getBotID(self, botusername):  # bots slack ID
        apicall = self.sl.api_call("users.list")
        users = apicall["members"]
        # print(users)
        for user in users:
            if 'name' in user and botusername == user.get('name') and not user.get('deleted'):
                return user.get('id')

    def writeToSlack(self, channel, msg):
        return self.sl.api_call("chat.postMessage", channel=channel, text=msg, as_user=True)

    def getChannelList(self):
        # return sl.api_call("channels.list")
        cl = self.sl.api_call("channels.list")['channels']

        for c in cl:
            print(c['name'] + " : " + c['id'])
            # print('c')


class mainFunc(slackMsg):
    def __int__(self):
        super(mainFunc, self).__int__()

    def actionOrnot(self, inpu):
        if inpu[1] != None:
            user, message, channel = inpu
            message = self.mat(message)
            # print("mat msg processed: " + str(message))
            return self.writeToSlack(channel, str(message))['ok']
        else:
            # print("inpu is None")
            return False

    def run(self):
        self.slackConnect()
        MYID = self.getBotID(self.myName)
        # print(MYID)
        int = 1
        while True:
            slackInput = self.parseSlackInput(self.slackReadRTM(), MYID)
            # print("slack input: ")
            # print(slackInput)
            if self.actionOrnot(slackInput):
                print(str(int) + " msg: " + slackInput[1])
                int += 1
            try:
                time.sleep(1)
            except KeyboardInterrupt:
                exit(1)

    def mat(self, inp):
        if "+" in inp:
            inp = str(inp).split("+")
            ii = inp[0].strip(' ')
            iii = inp[1].strip(' ')
            ret = "yes, I do math: " + str(float(ii) + float(iii))
            print(ret)
            return ret
        elif "-" in inp:
            inp = str(inp).split("-")
            ii = inp[0].strip(' ')
            iii = inp[1].strip(' ')
            ret = "yes, I do math: " + str(float(ii) - float(iii))
            print(ret)
            return ret
        elif "*" in inp:
            inp = str(inp).split("*")
            ii = inp[0].strip(' ')
            iii = inp[1].strip(' ')
            ret = "yes, I do math: " + str(float(ii) * float(iii))
            print(ret)
            return ret
        elif "/" in inp:
            inp = str(inp).split("/")
            ii = inp[0].strip(' ')
            iii = inp[1].strip(' ')
            ret = "yes, I do math: " + str(float(ii) / float(iii))
            print(ret)
            return ret
        else:
            return inp

if __name__ == "__main__":
    instance = mainFunc()
    instance.run()

# sm = slackMsg()
# print(slackConnect())
# slackReadRTM()
# sm.parseSlackInput(sm.inpu, sm.botID)
# print(sm.getBotID('bot'))
# getBotID('bot')
# print(writeToSlack("DEX23LF2B", "testig writing to slack"))

# print(slackMsg().writeToSlack("CEW3YFUMB", "BOT is testig writing to slack"))
# getChannelList()
