#Created by Hamilton Greene
#Contact me at hamilton.greene@gmail.com
#

#To run the program: Call pictureTheme(.jpg image) with a .jpg image in the same folder.
#The program will supply a list of available themes.  Type a theme name in the box and
#a transformed image will appear.  Choose whether or not you would like to save the file.
#If so, you will be prompted to enter a file name.

from Myro import *

#Insert the file name of the picture you wish to theme (must be in same folder
#as program).  The picture will be saved with a different name.
def pictureTheme(myPic):

    #Dictionary from which color values for each theme originate.
    picThemes = {'rasta':[(0,88,37),(157,8,12),(255,187,2)],'usa':[(215,26,33),(125,165,173),(253,229,169)],'grey scale':[(100,100,100),(151,151,151),(252,252,252)],'silhouette':[(0,0,0),(255,255,255),(255,255,255)],'negative':[(252,252,252),(151,151,151),(100,100,100)],
                    'negative silhouette': [(255,255,255),(255,255,255),(0,0,0)],'green lantern':[(0,0,0),(0,196,0),(255,255,255)], 'dirty birds':[(0,0,0),(234,46,45),(255,255,255)], 'cortana':[(7,24,140),(33,142,247),(215,243,246)], 'lamb chop':[(102,51,153),(0,160,0),(207,181,59)]}

    #Opens picture file.
    picture = makePicture(myPic)

    #Allows user to choose desired theme.
    chosenTheme = themeChoice(picThemes)

    #Takes color set of desired theme out of picThemes and puts theme in themeColors variable.
    themeColors = picThemes[chosenTheme]

    #Takes each color's RGB values out of themeColors and places them in smaller,
    #easier to access tuples: dC (dark color), mC (middle color), and lC (light color).
    dC = themeColors[0]
    mC = themeColors[1]
    lC = themeColors[2]

    #Goes through each pixel in the picture and determines what color to change it to,
    #based on the chosen theme.
    for pix in getPixels(picture):
        g = getGreen(pix)
        r = getRed(pix)
        b = getBlue(pix)

        #Light areas of the picture will be replaced with the theme's light color, medium
        #with medium, and dark with dark.
        if g >= 190 or r >= 190 or b >= 190:
            setRGB(pix,lC[0],lC[1],lC[2])
        elif g >= 130 or r >= 130 or b >= 130:
            setRGB(pix,mC[0],mC[1],mC[2])
        elif g >= 70 or r >= 70 or b >= 70:
            setRGB(pix,dC[0],dC[1],dC[2])
        else:
            setRGB(pix,0,0,0)

    #View picture and have time to determine whether you want to keep it.
    show(picture)
    wait(4)

    #Decide whether you want to save the resulting picture and what you would like to save
    #it as.
    keepPicture = input("Would you like to save? (y/n): ")
    if keepPicture == 'y' or keepPicture == 'yes':
        fileName = input("Enter a file name (.jpg included): ")
        savePicture(picture,fileName +".jpg")


#themeChoice() provides the user the ability to choose which theme he would like to apply.
def themeChoice(choices):

    #Prints available themes in alphabetical order.
    print("Here are a list of theme choices.  Please type a theme name.")
    for themes in sorted(choices.keys()):
        print(themes)

    #User enters desired theme.  Checks if theme is a possible choice.  If not,
    #themeChoice() is called again.
    chosen = input("Theme: ")
    if chosen in choices:
        return chosen
    else:
        return themeChoice(choices)