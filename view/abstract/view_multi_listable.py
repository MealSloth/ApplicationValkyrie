from abc import ABCMeta


class MultiListableView:
    __metaclass__ = ABCMeta

    title = []
    header = []
    entry = []

    def __init__(self, **kwargs):
        if kwargs.get('title'):
            self.title = kwargs['title']
        if kwargs.get('header'):
            self.header = kwargs['header']
        if kwargs.get('entry'):
            self.entry = kwargs['entry']

    def get_elements(self):
        response = {}
        if self.title:
            response['title'] = self.title
        if self.header:
            response['header'] = self.header
        if self.entry:
            response['entry'] = self.entry
        return response
