'''
Here are some pre-defined styles to speed up common styling ops, like centering on a page
'''

from htmlgen import *

# center in parent
centerOnPage = StyleGroup('.centerOnPage')
centerOnPage.setProperty('margin', 'auto')

# center contents
flexCentered = StyleGroup('.flexCentered')
flexCentered.setProperty('display', 'flex')
flexCentered.setProperty('justify-content', 'center')
flexCentered.setProperty('align-items', 'center')


# max width and height, no margin
fillContainer = StyleGroup('.fillContainer')
fillContainer.setProperty('margin', '0px')
fillContainer.setProperty('height', '100%')
fillContainer.setProperty('width', '100%')
