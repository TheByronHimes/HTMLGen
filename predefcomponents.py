from htmlgen import Tag, StyleGroup, Component
import predefcss


class Subcontainer(Component):
    def __init__(self):
        super(Subcontainer, self).__init__(tag_name='div')
        self.addStyleGroup(predefcss.centerOnPage)
        self.classes='centerOnPage'


class RoundButton(Component):
    def __init__(self, text=''):
        super(RoundButton, self).__init__(tag_name='button')
        self.text=text
        self.addStyleGroup(predefcss.circleBorder)
        self.classes.add('circleBorder')
        
