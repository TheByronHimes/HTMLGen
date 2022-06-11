class Stylesheet:
    def __init__(self, name='style.css'):
        self.name = name
        self.output_location = ''
        self.styles = dict() #[property][value] = [class names]

    def cleanClassFromProperty(self, className, propertyName):
        if propertyName in self.styles:
            for val in self.styles[propertyName]:
                if className in self.styles[propertyName][val]:
                    self.styles[propertyName][val].remove(className)

    def __str__(self):
        groups = dict()
        for pn in self.styles:
            for pv in self.styles[pn]:
                namesAsKey = tuple(sorted(self.styles[pn][pv]))
                if namesAsKey not in groups:
                    groups[namesAsKey] = list()
                groups[namesAsKey].append('%s: %s;' % (pn, pv))

        # TODO: perform smart consolidation here
        
        output = ''
        for group in groups:
            c = ',\n'.join(group)
            c += ' {\n\t'
            c += '\n\t'.join(groups[group])
            c += '\n}'
            output += c + '\n\n'
        return output
        

    def setProperty(self, className, propertyName, propertyValue):
        if propertyName not in self.styles:
            self.styles[propertyName] = dict()
        if propertyValue not in self.styles[propertyName]:
            self.styles[propertyName][propertyValue] = list()

        # search through values for this property and remove class name
        self.cleanClassFromProperty(className, propertyName)

        # set property
        self.styles[propertyName][propertyValue].append(className)

    def removeProperty(self, className, propertyName):
        cleanClassFromProperty(className, propertyName)

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
s = Stylesheet()
s.setProperty('.banana', 'width', '250px')
s.setProperty('.mohawk', 'width', '250px')
s.setProperty('.banana', 'height', '300px')
s.setProperty('.mohawk', 'height', '750px')
print(s)
