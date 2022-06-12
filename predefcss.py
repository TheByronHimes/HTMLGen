'''
Here are some pre-defined styles to speed up common styling ops, like centering on a page
'''

from htmlgen import *

# center in parent
centerOnPage = StyleGroup('.centerOnPage')
centerOnPage.setProperty('margin', 'auto')
centerOnPage.setProperty('max-width', '100%')
centerOnPage.setProperty('max-height', '100%')

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

# generic rounded borders with 8px radius
roundBorders = StyleGroup('.roundBorders')
roundBorders.setProperty('border-radius', '8px')

# fully rounded borders
circleBorder = StyleGroup('.circleBorder')
circleBorder.setProperty('border-radius', '50%')

# semi-transparent background white
seeThruLite = StyleGroup('.seeThruLite')
seeThruLite.setProperty('background-color', 'rgba(255, 255, 255, .5)')

# semi-transparent background black
seeThruDark = StyleGroup('.seeThruDark')
seeThruDark.setProperty('background-color', 'rgba(0, 0, 0, .5)')
