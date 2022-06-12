from htmlgen import Tag, StyleGroup

class Component:

    def __init__(self, name=''):
        self.name = name
        self.content = list()
        self.styles = list()
        # ^ styles doesn't apply any styling directly
        # rather, it makes sure that the styles
        # get included in the stylesheet

    def __str__(self):
        return str(self.content)

    def addStyleGroup(self, sg):
        if type(sg) != StyleGroup:
            raise Exception('parameter for Stylesheet.addStyleGroup() must be of type StyleGroup')
        if sg not in self.styles:
            self.styles.append(sg)

    def removeStyleGroup(self, sg):
        if type(sg) != StyleGroup:
            raise Exception('parameter for Stylesheet.removeStyleGroup() must be of type StyleGroup')
        if sg in self.styles:
            self.styles.remove(sg)
