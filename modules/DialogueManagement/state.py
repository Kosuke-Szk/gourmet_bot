# -*- coding: utf-8 -*-


class DialogueState(object):

    def __init__(self):
        self.__state = {'GENRE': None, 'LOCATION': None}

    def update(self, dialogue_act):
        self.__state['GENRE'] = dialogue_act.get('GENRE', self.__state['GENRE'])
        self.__state['LOCATION'] = dialogue_act.get('LOCATION', self.__state['LOCATION'])

    def has(self, name):
        return self.__state[name] != None

    def get_area(self):
        return self.__state['LOCATION']

    def get_food(self):
        return self.__state['GENRE']

    def __str__(self):
        import pprint
        return pprint.pformat(self.__state)