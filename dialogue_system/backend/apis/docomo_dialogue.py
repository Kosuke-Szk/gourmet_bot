# -*- coding: utf-8 -*-
import os
import requests
import json
from datetime import datetime

KEY = os.environ.get('DOCOMO_DIALOGUE_API_KEY', None)

# リクエストクエリ
endpoint = 'https://api.apigw.smt.docomo.ne.jp/naturalChatting/v1/dialogue?APIKEY=REGISTER_KEY'
url = endpoint.replace('REGISTER_KEY', KEY)

class DocomoDialogAPI(object):
    # def __init__(self, api_key=None):
    #     api_key = os.environ.get('DOCOMO_DIALOGUE_API_KEY', api_key)
    #     self.__client = Client(apikey=api_key)

    # def reply(self, text):
    #     response = self.__client.send(utt=text, apiname='Dialogue')
    #     utt = response['utt']

    #     return utt

    def __init__(self):
      self.register()

    def register(self):
        r_endpoint = 'https://api.apigw.smt.docomo.ne.jp/naturalChatting/v1/registration?APIKEY=REGISTER_KEY'
        r_url = r_endpoint.replace('REGISTER_KEY', KEY)
        r_headers = {'Content-type': 'application/json'}
        pay = {
            "botId": "Chatting",
            "appKind": "Smart Phone"
        }
        r = requests.post(r_url, data=json.dumps(pay), headers=r_headers)
        self.appId = r.json()['appId']
        print('appId : ', self.appId)
        # return appId

    def reply(self, utt_content):
        headers = {'Content-type': 'application/json;charset=UTF-8'}
        payload = {
            "language": "ja-JP",
            "botId": "Chatting",
            "appId": self.appId,
            "voiceText": utt_content,
            "appRecvTime": "2018-06-11 22:44:22",  # 仮置き。これで動いてしまう。
            "appSendTime": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        # Transmission
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        data = r.json()
        # rec_time = data['serverSendTime']
        response = data['systemText']['expression']
        print("response: %s" % response)
        return response