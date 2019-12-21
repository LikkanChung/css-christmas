import random, os

width = 100
height = 50

foreground = []
background = []
mask = []
output = []

css_title_x_offset = 21
css_title_y_offset = 19
css_title = ["                                                         ",
             "    _=[]+{}+{}[        {}]+![]+!![        ];$=_[5]+_[    ",
             "   1]+_[16]+_[1+      26]+_[6]+_[1+      29]+_[15]+_[5   ",
             " ]+_[6       ]+_[1  ]+_[1      +29];(  []+[]      )[$][$ ",
             " ](_[5       +4+6+  3+7+5              ]+_[4             ",
             " ]+_[6               ]+_[3+             5+7]+_           ",
             " [7+4+                 6+1+3+9]+          _[8+2+3+3      ",
             " ]+_[7                  ]+_[5]+_[          1]+_[4+4+     ",
             " 4+4]+                       _[3+4+             7+6+5+   ",
             " 2]+_[       1]+_[             26]+_              [4])(  ",
             " )[_[1       +25]+  _[1]+      ([]+_   [$])[      14]](  ",
             "   _[5]+_[4+7+6+      3+5+2]+_[1+26      ]+_[7]+_[25]+   ",
             "    _[6]+_[7]+[        ]+_[8+3+4]         +_[1]+_[2])    ",
             "                                                         "]

css_title_mask = ["   #############      #############      #############   ",
                  "  ##_=[]+{}+{}[#     ##{}]+![]+!![#     ##];$=_[5]+_[#   ",
                  "###1]+_[16]+_[1+######26]+_[6]+_[1+######29]+_[15]+_[5###",
                  "#]+_[6#~#####]+_[1##]+_[1######+29];(##[]+[]######)[$][$#",
                  "#](_[5#     #+4+6+##3+7+5###  #########]+_[4###  ########",
                  "#]+_[6#     #########]+_[3+######     ##5+7]+_######     ",
                  "#[7+4+#             ###6+1+3+9]+##     ###_[8+2+3+3##    ",
                  "#]+_[7#               ##]+_[5]+_[###     ##1]+_[4+4+###  ",
                  "#4+4]+#     #######    ######_[3+4+ #     ######7+6+5+## ",
                  "#2]+_[#     #1]+_[########  ###26]+_# #######  ###[4])(# ",
                  "#)[_[1#######+25]+##_[1]+######([]+_# #[$])[######14]](# ",
                  "###_[5]+_[4+7+6+## ###3+5+2]+_[1+26## ###]+_[7]+_[25]+## ",
                  "  ##_[6]+_[7]+[##    ##]+_[8+3+4]###    ##+_[1]+_[2])##  ",
                  "   #############      ############       #############   "]

title_x_offset = 10
title_y_offset = 5
title = ["  __  __                         _____ _          _     _                        ",
         " |  \/  |                       / ____| |        (_)   | |                       ",
         " | \  / | ___ _ __ _ __ _   _  | |    | |__  _ __ _ ___| |_ _ __ ___   __ _ ___  ",
         " | |\/| |/ _ \ '__| '__| | | | | |    | '_ \| '__| / __| __| '_ ` _ \ / _` / __| ",
         " | |  | |  __/ |  | |  | |_| | | |____| | | | |  | \__ \ |_| | | | | | (_| \__ \ ",
         " |_|  |_|\___|_|  |_|   \__, |  \_____|_| |_|_|  |_|___/\__|_| |_| |_|\__,_|___/ ",
         "                         __/ |                                                   ",
         "                 __     |___/                   _ _         _                    ",
         "                / _|                           | | |       | |                   ",
         "               | |_ _ __ ___  _ __ ___     __ _| | |   __ _| |_                  ",
         "               |  _| '__/ _ \| '_ ` _ \   / _` | | |  / _` | __|                 ",
         "               | | | | | (_) | | | | | | | (_| | | | | (_| | |_                  ",
         "               |_| |_|  \___/|_| |_| |_|  \__,_|_|_|  \__,_|\__|                 ",
         "                                                                                 "]

title_mask = ["##__##__##                     ##_____#_##      ##_## ##_##                      ",
              "#|##\/##|#                    ##/#____|#|#      #(_)###| |#                      ",
              "#|#\##/#|#___#_#__#_#__#_###_##|#|####|#|__##_#__#_#___| |_#_#__#___###__#_#___##",
              "#|#|\/|#|/#_#\#'__|#'__|#|#|#|#|#|####|#'_#\|#'__|#/#__|#__|#'_#`#_#\#/#_`#/#__|#",
              "#|#|##|#|##__/#|##|#|##|#|_|#|#|#|____|#|#|#|#|##|#\__#\#|_|#|#|#|#|#|#(_|#\__#\#",
              "#|_|##|_|\___|_|##|_|###\__,#|##\_____|_|#|_|_|##|_|___/\__|_|#|_|#|_|\__,_|___/#",
              "#########################__/#|###################################################",
              "               ##__##  #|___/##               ##_#_##     ##_##                  ",
              "              ##/#_|#  #######                #|#|#|#     #|#|##                 ",
              "              #|#|_#_#__#___##_#__#___#####__#_|#|#|###__#_|#|_##                ",
              "              #|##_|#'__/#_#\|#'_#`#_#\###/#_`#|#|#|##/#_`#|#__|#                ",
              "              #|#|#|#|#|#(_)#|#|#|#|#|#|#|#(_|#|#|#|#|#(_|#|#|_##                ",
              "              #|_|#|#|##\___/|_|#|_|#|_|##\__,_|_|_|##\__,_|\__|#                ",
              "              ###################################################                "]

# Initialise foreground and background arrays
for y in range(height):
    line = []
    foreground.append(line)
    background.append(line)
    output.append(line)
    for x in range(width):
            line.append(' ')

# Initialise Mask
for y in range(height):
    line = []
    mask.append(line)
    for x in range(width):
        line.append(False)

# Draw TITLE
j = title_y_offset
for line in title:
    i = title_x_offset
    for c in line:
        foreground[j][i] = c
        i += 1
    j += 1

# Mask TITLE
j = title_y_offset
for line in title_mask:
    i = title_x_offset
    for c in line:
        if c != ' ':
            mask[j][i] = True
        else:
            mask[j][i] = False
        i += 1
    j += 1

# Draw CSS logo
j = css_title_y_offset
for line in css_title:
    i = css_title_x_offset
    for c in line:
        foreground[j][i] = c
        i += 1
    j += 1

# Mask CSS logo
j = css_title_y_offset
for line in css_title_mask:
    i = css_title_x_offset
    for c in line:
        if c != ' ':
            mask[j][i] = True
        else:
            mask[j][i] = False
        i += 1
    j += 1

# Draw borders
for y in range(height):
    for x in range(width):
        if y == 0 or x == 0 or y == height - 1 or x == width - 1 \
        or y == 1 or x == 1 or y == height - 2 or x == width - 2:
            foreground[y][x] = '#'
            mask[y][x] = True

# Use Mask
# for y in range(height):
#     for x in range(width):
#         if not (mask[y][x]):
#             background[y][x] = '+'
for i in range(300):
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)
    if not mask[y][x]:
        background[y][x] = '*'

# Layers
for y in range(height):
    for x in range(width):
        output[y][x] = background[y][x]
        if foreground[y][x] != ' ':
            output[y][x] = foreground[y][x]

# Print
def print_image():
    for y in range(height):
        for x in range(width):
            print(output[y][x], end = '')
        print("")

def clear():
     _ = lambda: os.system('clear') #on Linux System

for i in range(1000):
    clear()
    print(str(i))
    print_image()