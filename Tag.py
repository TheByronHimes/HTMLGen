import re


class Tag:

    class Classes:
        def __init__(self, *args):
            self.classes = list()
            if len(args) > 0:
                for arg in args:
                    self.add(arg)

        def __len__(self):
            return len(self.classes)

        def __str__(self):
            if len(self.classes) == 0:
                return ""
            else:
                return ' '.join(self.classes)

        def add(self, *args):
            starting_length = len(self.classes)
            # TODO: DRY this out
            for a in args:
                if type(a) != str:
                    raise Exception("Classes must be added as strings, not %s" % str(type(a)))
                if a.count(' ') > 0:
                    # can pass in muliple classes as a string separated by spaces
                    a = a.split()
                    for name in a:
                        if self.isValidClassName(self, name):
                            self.classes.append(name)
                        else:
                            raise Exception("Class name %s is not in the correct format" % name)
                else:
                    if self.isValidClassName(self, a):
                        self.classes.append(a)

            if len(self.classes) > starting_length:
                self.classes.sort()

        def remove(self, *args):
            # TODO: DRY this out
            for a in args:
                if type(a) != str:
                    raise Exception("Classes must be added as strings, not %s" % str(type(a)))
                if a.count(' ') > 0:
                    # can pass in muliple classes as a string separated by spaces
                    a = a.split()
                    for name in a:
                        if self.isValidClassName(self, name) and name in self.classes:
                            self.classes.remove(name)
                        else:
                            raise Exception("Class name %s is not in the correct format" % name)
                else:
                    if self.isValidClassName(self, a) and name in self.classes:
                        self.classes.add(a)

        def removeAll(self):
            self.classes = list()

        def toHtml(self):
            output = ''
            if len(self.classes) > 0:
                output = 'class="%s"' % ' '.join(self.classes)
            return output
            
            
        @staticmethod
        def isValidClassName(self, c):
            ''' returns True if c is a valid CSS class name '''
            return re.search('^[_a-zA-Z]+[_a-zA-Z0-9-]*', c)

        #################################
        ######END OF ClassList CLASS#####
        #################################


    class Styles:
        def __init__(self, styles=''):
            self.styles = dict()
            
            if len(styles) > 0:
                if style.count(':') in (0, 1):
                    self.set(self.parseStyle(style))
                elif style.count(':') > 1:
                    try:
                        style = style.split(';')
                        for s in style:
                            self.set(self.parseStyle(s))
                    except:
                        raise Exception('Multiple styles must be passed in with format "styleName:styleValue; styleName:styleValue"')
            

        @staticmethod
        def parseStyle(self, s):
            ''' tries to get key val from string formatted like "key: val" '''
            try:
                key = s[:s.index(':')].strip()
                val = s[s.index(':')+1:].strip()
                return key, val
            except:
                raise Exception('Style not in expected format. Format expected to be "styleName:styleValue"')

        def remove(self, name):
            if name in self.styles:
                self.styles.pop(name)

        def set(self, name, value=''):
            self.styles[name] = value

        def toHtml(self):
            output = ''
            if len(self.styles) > 0:
                output = 'style="%s"' % ' '.join([name + ': ' + self.styles[name] + ';' for name in self.styles])
            return output

        #################################
        ######  END OF Styles CLASS #####
        #################################


    class Attributes:
        def __init__(self, attributes=''):
            self.attributes = dict()
            if len(attributes) > 0:
                if attributes.count('=') in (0, 1):
                    k,v = self.parseValue(attributes, '=')
                    self.set(k,v)
                elif attributes.count('=') > 1:
                    try:
                        if attributes.count(';') > 0:
                            attributes = attributes.split(';')
                        else:
                            attributes = attributes.split(' ')
                        for s in attributes:
                            k,v = self.parseValue(s, '=')
                            self.set(k,v)
                    except:
                        raise Exception('Multiple attributes must be passed in with format "attName=attValue; attName=attValue"')                

        @staticmethod
        # TODO: add base class and abstract this logic out 
        def parseValue(s, sep):
            ''' tries to get key val from string formatted like "key[sep]val" '''
            try:
                key = s[:s.index(sep)].strip()
                val = s[s.index(sep)+1:].strip()
                return key, val
            except:
                raise Exception('Style or Attribute not in expected format. Format expected to be "styleName%sstyleValue"' % sep)
            
        def set(self, name, value=''):
            self.attributes[name] = value
            
        def toHtml(self):
            output = ''
            if len(self.attributes) > 0:
                output = ' '.join([name + '="' + self.attributes[name] + '"' for name in self.attributes])
            return output            
        
        #################################
        #### END OF Attributes CLASS ####
        #################################
    
    def __init__(
        self, 
        tag_name, 
        text='', 
        children=list(), 
        classes='', 
        tag_id='', 
        styles='',
        attributes=''
    ):
        self.tag_name = tag_name
        self.text = text

        self.children = list()
        if type(children) == Tag:
            self.addChildren(children)
        elif type(children) == list:
            for child in children:
                self.addChild(child)
            
        if classes == '':
            self.classes = self.Classes()
        else:
            self.classes = self.Classes(classes)
        
        self.tag_id = tag_id

        if styles == '':
            self.styles = self.Styles()
        else:
            self.styles = self.Styles(styles)

        if attributes == '':
            self.attributes = self.Attributes()
        else:
            self.attributes = self.Attributes(attributes)
        
        self.outer_tabs = 0
        self.inner_tabs = 1
        
    def addChild(self, child):
        child.indent(self.outer_tabs)
        self.children.append(child)

    def addScript(self, src=''):
        script = Tag('script', attributes='src=%s'%src)
        self.addChild(script)
        
    def dedent(self):
        self.outer_tabs -= 1
        self.inner_tabs -= 1
        for child in self.children:
            child.dedent()
        
    def getId(self):
        output = ""
        if self.tag_id != output:
            output = 'id="%s"' % self.tag_id
        return output
    
    def getIndentedText(self):
        if self.text == '':
            return ''
        return (self.inner_tabs * "\t") + self.text + '\n'    

    def getPrintedChildren(self):
        return '\n'.join([str(c) for c in self.children])

    def getTagExtras(self):
        extras = {
            'classes': self.classes,
            'styles': self.styles,
            'attributes': self.attributes
        }
        return extras

    def indent(self, parent=0):
        if parent==0:
            self.outer_tabs += 1
        else:
            self.outer_tabs = parent + 1

        self.inner_tabs = self.outer_tabs + 1
        for child in self.children:
            child.indent(self.outer_tabs)         
    
    def removeAllChildren(self):
        for i in reversed(range(len(self.children))):
            del self.children[i]
        
    def removeChildByIndex(self, index):
        ''' remove child based on index '''
        self.removeChild(self.children[index])
        
    def removeChild(self, obj):
        self.children.remove(obj)
        
    def tagExtrasToHtml(self):
        extras = self.getTagExtras()
        return ' '.join([extras[key].toHtml() for key in extras if len(extras[key].toHtml()) > 0])
        
    def __str__(self):
        if len(self.children) == 0:
            return "%s<%s %s>%s</%s>" % (
                "\t" * self.outer_tabs, 
                self.tag_name, 
                self.tagExtrasToHtml(), 
                self.text,
                self.tag_name
            )
        else:
            return "%s<%s %s>\n%s\n%s</%s>" % (
                    "\t" * self.outer_tabs, 
                    self.tag_name, 
                    self.tagExtrasToHtml(), 
                    #'\t' * self.inner_tabs + self.text, 
                    self.getPrintedChildren(), 
                    "\t" * self.outer_tabs, 
                    self.tag_name
                )


        
                
##########################################
##t = Tag('div', text="inner text", class_list="class1", attributes="width=250 height=500")
##t2 = Tag('div', children=t)
##t2.classes.add('bat')
##print(t2)


