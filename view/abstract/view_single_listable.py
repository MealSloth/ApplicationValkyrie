from abc import ABCMeta


class SingleListableView:
    __metaclass__ = ABCMeta

    image = []
    id = []
    info = []
    id_pool = []
    widget = []
    listable = []
    blobs = []

    def __init__(self, **kwargs):
        if kwargs.get('image'):
            self.image = kwargs['image']
        if kwargs.get('id'):
            self.id = kwargs['id']
        if kwargs.get('info'):
            self.info = kwargs['info']
        if kwargs.get('id_pool'):
            self.id_pool = kwargs['id_pool']
        if kwargs.get('widget'):
            self.widget = kwargs['widget']
        if kwargs.get('listable'):
            self.listable = kwargs['listable']
        if kwargs.get('blobs'):
            self.blobs = kwargs['blobs']

    def get_elements(self):
        response = {}
        if self.image:
            response['image'] = self.image
        if self.id:
            response['id'] = self.id
        if self.info:
            response['info'] = self.info
        if self.id_pool:
            response['id_pool'] = self.id_pool
        if self.widget:
            response['widget'] = self.widget
        if self.listable:
            response['listable'] = self.listable
        if self.blobs:
            response['blobs'] = self.blobs
        return response
