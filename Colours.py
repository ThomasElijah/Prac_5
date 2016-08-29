COLOURS_HEXADECIMALS = {"aquamarine1": "#7fffd4", "chartreuse1": "#7fff00", "cyan1": "#00ffff", "cyan2": "#00eeee", "cyan3": "#00cdcd",
                       "cyan4": "#008b8b", "DarkGoldenrod": "#b8860b", "DarkGoldenrod1": "#ffb90f", "DarkGoldenrod2": "#eead0e", "DarkGoldenrod3": "#cd950c",
                        "DarkGoldenrod4": "#8b6508", "DarkGreen": "#006400"}

colour = input("Enter a colour to receive hexadecimal:")
while colour != "":
    if colour in COLOURS_HEXADECIMALS:
        print(colour, "is", COLOURS_HEXADECIMALS[colour])
    else:
        print("Invalid colour")
    colour = input("Enter a colour to receive a hexadecimal:")
