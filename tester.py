import webbrowser
from htmlgen import *
import predefcss


class Tester:
    def __init__(self):
        pass

    def viewDocument(self, doc):
        ''' opens document in browswer '''
        doc.writeToFile(file_name='test.html')
        i = 0
        for ss in doc.stylesheets:
            ss[0].writeToFile()
            
        webbrowser.open_new_tab(doc.getOutputLocation() + 'test.html')
        

## some basic test code
tester = Tester()

s = Stylesheet()
s.setProperty('.class1', 'background-color', 'salmon')
s.setProperty('.class1', 'font-size', '50px')
s.addStyleGroup(predefcss.fillContainer)
s.addStyleGroup(predefcss.flexCentered)



# todo, add easy way to apply stylegroups to tags
div1 = Tag('div', text='div1', classes='fillContainer flexCentered')
div2 = Tag('div', text='div2', classes='class1')
div1.addChild(div2)

d = Document()
d.body.addChild(div1)
d.linkStylesheet(s)
tester.viewDocument(d)
