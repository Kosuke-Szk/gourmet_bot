# -*- coding: utf-8 -*-
from modules.DialogueManagement.state import DialogueState
from modules.BackEnd.APIs.hotpepper import HotPepperGourmetAPI

# from dialogue_system.backend.apis.docomo_dialogue import DocomoDialogAPI


class DialogueManager(object):

    def __init__(self):
        self.dialogue_state = DialogueState()
        # self.dialogue_api = DocomoDialogAPI()

    def update_dialogue_state(self, dialogue_act):
        self.dialogue_state.update(dialogue_act)

    def select_action(self, dialogue_act):
        from copy import deepcopy
        sys_act = deepcopy(dialogue_act)
        # if dialogue_act['user_act_type'] == 'OTHER':
        #     reply = self.dialogue_api.reply(dialogue_act['utt'])
        #     sys_act['sys_act_type'] = 'CHAT'
        #     sys_act['utt'] = reply
        # el
        if not self.dialogue_state.has('LOCATION'):
            print('setting LOCATION')
            sys_act['sys_act_type'] = 'REQUEST_LOCATION'
        elif not self.dialogue_state.has('GENRE'):
            print('setting GENRE')
            sys_act['sys_act_type'] = 'REQUEST_GENRE'
        else:
            self.gourmet_api = HotPepperGourmetAPI()
            area = self.dialogue_state.get_area()
            food = self.dialogue_state.get_food()
            restaurant = self.gourmet_api.search_restaurant(area=area, food=food)
            sys_act['sys_act_type'] = 'INFORM_RESTAURANT'
            sys_act['restaurant'] = restaurant
            # self.dialogue_state.clear()

        return sys_act