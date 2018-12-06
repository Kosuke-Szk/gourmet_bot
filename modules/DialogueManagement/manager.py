# -*- coding: utf-8 -*-
from modules.DialogueManagement.state import DialogueState
from modules.BackEnd.APIs.hotpepper import HotPepperGourmetAPI

class DialogueManager(object):

    def __init__(self):
        self.dialogue_state = DialogueState()

    def update_dialogue_state(self, dialogue_act):
        self.dialogue_state.update(dialogue_act)

    def select_action(self, dialogue_act):
