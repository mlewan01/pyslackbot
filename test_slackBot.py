import pytest
from slackBot import *

inpu = [{'type': 'message', 'user': 'UEVTGF2HY', 'text': 'hello python',
         'client_msg_id': '5fa911bf-90e4-4e74-a38f-9c070cc1ad2c', 'team': 'TEV5TN7MW', 'channel': 'DEX23LF2B',
         'event_ts': '1545102036.001000', 'ts': '1545102036.001000'}]
botID = 'UEVTGF2HY'


@pytest.fixture
def slackMsg():
    from slackBot import slackMsg
    return slackMsg()


@pytest.fixture
def mainFunc():
    from slackBot import mainFunc
    return mainFunc()


def test_slackConnect(slackMsg):
    print("connect")
    assert slackMsg.slackConnect() == True


@pytest.mark.skip(reason="not fully implemented")
def test_slackReadRTM(slackMsg):
    print("readRTM")


def test_parseSlackInputTrue(slackMsg):
    assert slackMsg.parseSlackInput(inpu, botID) == True


def test_parseSlackInput(slackMsg):
    assert slackMsg.parseSlackInput(inpu, botID) == ["UEVTGF2HY", "hello python2", "DEX23LF2B"]


def test_getBotID(slackMsg):
    assert slackMsg.getBotID("bot") == "UEVSWHSUT"


def test_writeToSlack(slackMsg):
    assert slackMsg.writeToSlack("DEX23LF2B", "testig writing to slack") == True


def test_actionOrnotMessage(mainFunc):
    inpu = ["UEVTGF2HY", "hello python2", "DEX23LF2B"]
    assert mainFunc.actionOrnot(inpu)


def test_actionOrnotNone(mainFunc):
    inpu = [None, None, None]
    assert mainFunc.actionOrnot(inpu)
