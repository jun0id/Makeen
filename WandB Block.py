x = 0
fullWidth = int(input("Enter width?  "))

WidthPercolor = fullWidth / 2

blockWidth = 5

widthBlack = (WidthPercolor / blockWidth)
widthWhite = WidthPercolor / blockWidth - 1

gap = (WidthPercolor - widthWhite * blockWidth )  

print(" The Black Block width is:", round(widthBlack),'\n', "The White Block width is:", round(widthWhite),'\n', "The Gab width is:", gap)