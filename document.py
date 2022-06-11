''' Document represents the whole HTML page '''
from tag import Tag

class Document(Tag):            
    
    def __init__(self, lang='en'):
        self.doctype = ''
        self.name = 'index.html'
        self.tag_name = 'html'
        self.text = ''
        self.children = list()
        self.classes = self.Classes()
        self.tag_id = ''
        self.styles = self.Styles()
        self.attributes=self.Attributes('lang=en')
        self.output_location = ''
        self.outer_tabs = 0
        self.inner_tabs = 1


        self.head = Tag('head')
        self.head.addChild(Tag('title', text='Test'))
        self.body = Tag('body')
        self.addChild(self.head)
        self.addChild(self.body)

    def writeToFile(self, file_name=''):
        if file_name == '':
            file_name = self.name
        path = self.output_location
        if len(path) > 0:
            path += '/'
        path += file_name
        f = open(path, 'w')
        print(self, file=f)
        f.close()


######################
# TEST
######################

d = Document()
div1 = Tag('div', classes='class1')
div2 = Tag('div', classes='class2')
div1.addChild(div2)
d.body.addChild(div1)
print(d)
d.writeToFile()
