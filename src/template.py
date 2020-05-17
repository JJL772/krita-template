
from krita import Extension

class TemplateExtension(Extension):

    def __init__(self, parent): 
        super(TemplateExtension, self).__init__(parent)

    def setup(self):
        pass

    def createActions(self, window):
        pass


