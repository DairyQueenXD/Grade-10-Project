from graphics import *
import random

win = GraphWin("Escape the Mastermind",500,650)

"""
Game States
GS 0  - Start Screen
- Start Button : (110,400) (390,490)
- Rules Button (110,520) (390,610)

GS 1 - Intro to Game Screen
- Continue Button: (110,520) (390,600)

GS 2 - InGame State

GS 3 - Rules Screen

GS 4 - Winning Screen

GS 5 - Losing Screen
"""

## Game Stats
victory = 0 # 1 when win, 2 when lose
gamestate = 0
generate = 0
times_played = 0
## Image Importation
start = Image(Point(250,325),"start.png")
intro = Image(Point(250,325),"intro.png")
ingame = Image(Point(250,325),"ingame.png")
rules = Image(Point(250,325),"rules.png")
winning = Image(Point(250,325),"winning.png")
losing = Image(Point(250,325),"losing.png")

## Secret Code
reveal = 2 # 0 when not revealed, 1 when revealed, 2 when guessing colors,
# 3 when neutral
code = []
bigRadius = 30
smallRadius = 10
spacing = 10
total = 70
code_color_list = []

for i in range(0,3*total+1,total):
    code.append(Circle(Point(40+i,610),bigRadius))
a = 0
number = 5
code_list = ["red","green","yellow","blue","pink","orange"]
while a < 4:
    code_num = random.randint(0,number)
    code[a].setFill(code_list[code_num])
    code_color_list.append(code_list[code_num])
    code_list = code_list[0:code_num]+code_list[code_num+1:]
    a += 1
    number -= 1
print(code_color_list) ## This line is not necessary;
## I only put it for my demo to be faster

## Guessing Circles

# Big Circles
initial = 0 # 0 when initial (without colors),1 when otherwise

guess1 = []
for i in range(0,3*total+1,total):
        guess1.append(Circle(Point(40+i,40+total*0),bigRadius))
guess2 = []
for i in range(0,3*total+1,total):
        guess2.append(Circle(Point(40+i,40+total*1),bigRadius))
guess3 = []
for i in range(0,3*total+1,total):
        guess3.append(Circle(Point(40+i,40+total*2),bigRadius))
guess4 = []
for i in range(0,3*total+1,total):
        guess4.append(Circle(Point(40+i,40+total*3),bigRadius))
guess5 = []
for i in range(0,3*total+1,total):
        guess5.append(Circle(Point(40+i,40+total*4),bigRadius))
guess6 = []
for i in range(0,3*total+1,total):
        guess6.append(Circle(Point(40+i,40+total*5),bigRadius))
guess7 = []
for i in range(0,3*total+1,total):
        guess7.append(Circle(Point(40+i,40+total*6),bigRadius))
guess8 = []
for i in range(0,3*total+1,total):
        guess8.append(Circle(Point(40+i,40+total*7),bigRadius))
width = 2
for i in range(4):
    guess1[i].setWidth(width)
    guess2[i].setWidth(width)
    guess3[i].setWidth(width)
    guess4[i].setWidth(width)
    guess5[i].setWidth(width)
    guess6[i].setWidth(width)
    guess7[i].setWidth(width)
    guess8[i].setWidth(width)

# Small Circles
smallRadius = 10
total2 = 1*bigRadius + spacing
x = 325
result1 = []
for i in range(0,3*total2+1,total2):
        result1.append(Circle(Point(x+i,40+total*0),smallRadius))
result2 = []
for i in range(0,3*total2+1,total2):
        result2.append(Circle(Point(x+i,40+total*1),smallRadius))
result3 = []
for i in range(0,3*total2+1,total2):
        result3.append(Circle(Point(x+i,40+total*2),smallRadius))
result4 = []
for i in range(0,3*total2+1,total2):
        result4.append(Circle(Point(x+i,40+total*3),smallRadius))
result5 = []
for i in range(0,3*total2+1,total2):
        result5.append(Circle(Point(x+i,40+total*4),smallRadius))
result6 = []
for i in range(0,3*total2+1,total2):
        result6.append(Circle(Point(x+i,40+total*5),smallRadius))
result7 = []
for i in range(0,3*total2+1,total2):
        result7.append(Circle(Point(x+i,40+total*6),smallRadius))
result8 = []
for i in range(0,3*total2+1,total2):
        result8.append(Circle(Point(x+i,40+total*7),smallRadius))
width = 2
for i in range(4):
    result1[i].setWidth(width)
    result2[i].setWidth(width)
    result3[i].setWidth(width)
    result4[i].setWidth(width)
    result5[i].setWidth(width)
    result6[i].setWidth(width)
    result7[i].setWidth(width)
    result8[i].setWidth(width)
         
## "Secret Code" Text Box
codeText = Text(Point(6*total-30,610),"<- Secret Code !")
codeText.setFace("courier")
codeText.setSize(14)
codeText.setStyle("bold")

## Rectangle to hide the code
rect = Rectangle(Point(0,610-spacing-bigRadius),Point(3*total+40+bigRadius+spacing,650))
rect.setFill("black")


## Choosing Colors
choose_color = ["red","orange","yellow","green","blue","pink"]
choose_color_rect = []
choose_rect_yPos = 610-spacing-bigRadius+20
xPos = int(500/6)
for i in range (6):
    choose_color_rect.append(Rectangle(Point(i*xPos,choose_rect_yPos),Point((i+1)*xPos,650)))
for i in range(6):
    choose_color_rect[i].setFill(choose_color[i])
choose_text = Text(Point(250,610-spacing-bigRadius+7),"Choose a color!")
choose_text.setFace("courier")
choose_text.setSize(14)
choose_text.setStyle("bold")

## Rules Page
draw = 0
size = 15
x = 50
txt1 = Text(Point(250,120),"A red ball at the right means that there is a ball of the")
txt2 = Text(Point(250,142),"right color placed in the right place")
txt1.setSize(size)
txt2.setSize(size)
txt3 = Text(Point(250,120+x),"A white ball at the right means that there is a ball of the")
txt4 = Text(Point(250,142+x),"right color placed in the wrong place")
txt3.setSize(size)
txt4.setSize(size)
txt5 = Text(Point(250,120+2*x),"A black ball at the right means that there is a ball of")
txt6 = Text(Point(250,142+2*x),"the wrong color")
txt5.setSize(size)
txt6.setSize(size)
txt7 = Text(Point(113,220+2*x),"Suppose the secret code is: ")
txt7.setStyle("bold")
txt7.setSize(size-3)
txt8 = Text(Point(193,272+2*x),"Then the results for the following guesses will be: ")
txt8.setStyle("bold")
## Starting the game
start.draw(win)
row = 0
column = 0
which_row = []
guess_list = []
result_row = []
while True:
    
    time.sleep(0.02)
    k = win.checkKey()
    m = win.checkMouse()
        
    if gamestate == 0: ## Start screen
        if m != None and 110 <= m.getX() <= 390:
            if 400 <= m.getY() <= 490:
                gamestate = 1
                start.undraw()
                intro.draw(win)
            if 520 <= m.getY() <= 610:
                gamestate = 3
                start.undraw()
                rules.draw(win)
    if gamestate == 1: ## Intro Screen
        if m != None and 110 <= m.getX() <= 390 and 520 <= m.getY() <= 600:
            gamestate = 2
            intro.undraw()
            ingame.draw(win)
    if gamestate == 2:
        if initial == 0:
            for i in range(4):
                guess1[i].draw(win)
                guess2[i].draw(win)
                guess3[i].draw(win)
                guess4[i].draw(win)
                guess5[i].draw(win)
                guess6[i].draw(win)
                guess7[i].draw(win)
                guess8[i].draw(win)
            for i in range(4):
                result1[i].draw(win)
                result2[i].draw(win)
                result3[i].draw(win)
                result4[i].draw(win)
                result5[i].draw(win)
                result6[i].draw(win)
                result7[i].draw(win)
                result8[i].draw(win)
            initial = 1
        if reveal == 2: # Drawing the choose color buttons
            for i in range(6):
                choose_color_rect[i].draw(win)
            choose_text.draw(win)
            reveal = 3
        if reveal == 3: # Choosing colors
            
            if row == 0:
                which_row = guess1
                result_row = result1
                which_row[column].setOutline("red")
            if row == 1:
                which_row = guess2
                result_row = result2
                which_row[column].setOutline("red")
            if row == 2:
                which_row = guess3
                result_row = result3
                which_row[column].setOutline("red")
            if row == 3 :
                which_row = guess4
                result_row = result4
                which_row[column].setOutline("red")
            if row == 4:
                which_row = guess5
                result_row = result5
                which_row[column].setOutline("red")
            if row == 5 :
                which_row = guess6
                result_row = result6
                which_row[column].setOutline("red")
            if row == 6 :
                which_row = guess7
                result_row = result7
                which_row[column].setOutline("red")
            if row == 7:
                which_row = guess8
                result_row = result8
                which_row[column].setOutline("red")
        
            if m != None and m.getY() >= choose_rect_yPos:
                if m.getX() <= 82:
                    which_row[column].setFill("red")
                    guess_list.append("red")
                    which_row[column].undraw()
                    which_row[column].draw(win)
                if 84 <= m.getX() < 166:
                    which_row[column].setFill("orange")
                    guess_list.append("orange")
                    which_row[column].undraw()
                    which_row[column].draw(win)
                if 166 < m.getX() < 249:
                    which_row[column].setFill("yellow")
                    guess_list.append("yellow")
                    which_row[column].undraw()
                    which_row[column].draw(win)
                if 249 < m.getX() < 332:
                    which_row[column].setFill("green")
                    guess_list.append("green")
                    which_row[column].undraw()
                    which_row[column].draw(win)
                if 332 < m.getX() < 415:
                    which_row[column].setFill("blue")
                    guess_list.append("blue")
                    which_row[column].undraw()
                    which_row[column].draw(win)
                if 415 < m.getX():
                    which_row[column].setFill("pink")
                    guess_list.append("pink")
                    which_row[column].undraw()
                    which_row[column].draw(win)
                which_row[column].setOutline("black")
                which_row[column].undraw()
                which_row[column].draw(win)
                column += 1
    
                
                
                if column > 3:
                    red = 0
                    white = 0
                    black = 0
                    total_num = 0
                    column = 0
                    counter = 0
                     ## The commented block below is what I tried to fix when the user inputs 2
                    ## balls of the same color, but it doesn't work.
                    """
                    counted = True
                    repeat_num = 0 
                    continue_or_not = True
                    repeat = ""
                    repeated = False
                    repeated_2 = False
                    counter_repeat = 0
                   
                    
                    if str(guess_list).find("red") != str(guess_list).rfind("red"):
                        continue_or_not = False
                        repeat = "red"
                        repeat_num += 1
                    if str(guess_list).find("orange") != str(guess_list).rfind("orange"):
                        continue_or_not = False
                        repeat = "orange"
                        repeat_num += 1
                    if str(guess_list).find("yellow") != str(guess_list).rfind("yellow"):
                        continue_or_not = False
                        repeat = "yellow"
                        repeat_num += 1
                    if str(guess_list).find("green") != str(guess_list).rfind("green"):
                        continue_or_not = False
                        repeat = "green"
                        repeat_num += 1
                    if str(guess_list).find("blue") != str(guess_list).rfind("blue"):
                        continue_or_not = False
                        repeat = "blue"
                        repeat_num += 1
                    if str(guess_list).find("pink") != str(guess_list).rfind("pink"):
                        continue_or_not = False
                        repeat = "pink"
                        repeat_num += 1
                    print(continue_or_not)
                    print(repeat)
                    for i in range(0,4,1):
                        if guess_list[i] == repeat:
                            counter_repeat += 1
                    for i in range(4):
                        if code_color_list[i] == guess_list[i]:
                            if guess_list[i] == repeat:
                                repeated = True
                    for i in range(4):
                        if guess_list[i] == code_color_list:
                            repeated_2 = True
                    for i in range(4):
                        if repeat_num != 2: ## No 2 repeat colors
                            if continue_or_not: ## No repeat colors
                                if str(code_color_list).find(guess_list[i]) == -1:
                                    black += 1
                                elif code_color_list[i] == guess_list[i]:
                                    red += 1
                                elif str(code_color_list).find(guess_list[i]) != -1:
                                    white += 1
                            else: ## Repeat colors
                                if guess_list[i] == repeat: # Repeat color
                                    if repeated:
                                        ## Correct position correct color
                                        black += (counter_repeat - 1)
                                        red += 1
                                        repeated = False
                                    ## If already one red, then the others are all black
                                    else: 
                                        if str(code_color_list).find(repeat) != -1 and counted: # Found
                                            white += 1
                                            black += (counter_repeat - 1)
                                            counted = False
                                        ## No red, so if you can find the color, then there is 1 white and the rest black 
                                        else: # if there is no red nor white then all are black
                                            black += counter_repeat
                                else: ## Not the repeated color
                                    if str(code_color_list).find(guess_list[i]) == -1:
                                        black += 1
                                    elif code_color_list[i] == guess_list[i]:
                                        red += 1
                                    elif str(code_color_list).find(guess_list[i]) != -1:
                                        white += 1"""
                    for i in range(4):
                        if str(code_color_list).find(guess_list[i]) == -1:
                            black += 1
                        elif code_color_list[i] == guess_list[i]:
                            red += 1
                        elif str(code_color_list).find(guess_list[i]) != -1:
                            white += 1

                    
                    for i in range(red):
                        result_row[i].setFill("red")
                        counter += 1
                    for i in range(white):
                        result_row[counter].setFill("white")
                        counter += 1
                    for i in range(black):
                        result_row[counter].setFill("black")
                        counter += 1
                    if red == 4:
                        victory = 1
                    guess_list = []
                    row += 1
                    if row == 8:
                        victory = 2
                        row = 0
                    
                   
                    
        if reveal == 0: # Secret code hided
            rect.draw(win)
            codeText.draw(win)
            
        if reveal == 1: # Secret code revealed
            rect.undraw()
            for i in range(4):
                code[i].draw(win)
            reveal = 4
        if victory == 1:
            time.sleep(2)
            gamestate = 4
            ingame.undraw()
            winning.draw(win)
        if victory == 2: # lose
            time.sleep(2)
            gamestate = 5
            ingame.undraw()
            losing.draw(win)
    if gamestate == 3: # Rules page
        if draw == 0:
            txt1.draw(win)
            txt2.draw(win)
            txt3.draw(win)
            txt4.draw(win)
            txt5.draw(win)
            txt6.draw(win)
            txt7.draw(win)
            txt8.draw(win)
            rules1 = []
            for i in range(0,3*total+1,total):
                rules1.append(Circle(Point(40+i+210,40+total*4),bigRadius-3))
            width = 2
            rules1[0].setFill("red")
            rules1[1].setFill("orange")
            rules1[2].setFill("yellow")
            rules1[3].setFill("green")
            rules2 = []
            rules3 = []
            rules4 = []
            rules5 = []
            rules6 = []
            rules7 = []
            x = 325
            smallRadius = 10
            for i in range(0,3*total+1,total):
                rules2.append(Circle(Point(40+i,40+total*6-45),bigRadius-3))
            for i in range(0,3*total2+1,total2):
                rules3.append(Circle(Point(x+i,40+total*6-45),smallRadius))
            for i in range(0,3*total+1,total):
                rules4.append(Circle(Point(40+i,40+total*6+17),bigRadius-3))
            for i in range(0,3*total2+1,total2):
                rules5.append(Circle(Point(x+i,40+total*6+17),smallRadius))
            for i in range(0,3*total+1,total):
                rules6.append(Circle(Point(40+i,40+total*6+78),bigRadius-3))
            for i in range(0,3*total2+1,total2):
                rules7.append(Circle(Point(x+i,40+total*6+78),smallRadius))
            rules2[0].setFill("blue")
            rules2[1].setFill("orange")
            rules2[2].setFill("green")
            rules2[3].setFill("yellow")
            rules3[0].setFill("red")
            rules3[1].setFill("white")
            rules3[2].setFill("white")
            rules3[3].setFill("black")
            rules4[0].setFill("red")
            rules4[1].setFill("red")
            rules4[2].setFill("red")
            rules4[3].setFill("red")
            rules5[0].setFill("red")
            rules5[1].setFill("black")
            rules5[2].setFill("black")
            rules5[3].setFill("black")
            rules6[0].setFill("pink")
            rules6[1].setFill("yellow")
            rules6[2].setFill("blue")
            rules6[3].setFill("orange")
            rules7[0].setFill("white")
            rules7[1].setFill("white")
            rules7[2].setFill("black")
            rules7[3].setFill("black")
            for i in range(4):
                rules1[i].setWidth(width)
                rules2[i].setWidth(width)
                rules3[i].setWidth(width)
                rules4[i].setWidth(width)
                rules5[i].setWidth(width)
                rules6[i].setWidth(width)
                rules7[i].setWidth(width)
                rules4[i].draw(win)
                rules5[i].draw(win)
                rules1[i].draw(win)
                rules3[i].draw(win)
                rules2[i].draw(win)
                rules6[i].draw(win)
                rules7[i].draw(win)
            draw = 1
        if k != "" and k == 'space':
            gamestate = 0
            rules.undraw()
            txt1.undraw()
            txt2.undraw()
            txt3.undraw()
            txt4.undraw()
            txt5.undraw()
            txt6.undraw()
            txt7.undraw()
            txt8.undraw()
            for i in range(4):
                rules1[i].undraw()
                rules2[i].undraw()
                rules3[i].undraw()
                rules4[i].undraw()
                rules5[i].undraw()
                rules6[i].undraw()
                rules7[i].undraw()
            start.draw(win)
    if gamestate == 4:
        red = 0
        victory = 0
        #setUp()
        for i in range(4):
            guess1[i].undraw()
            guess2[i].undraw()
            guess3[i].undraw()
            guess4[i].undraw()
            guess5[i].undraw()
            guess6[i].undraw()
            guess7[i].undraw()
            guess8[i].undraw()
            result1[i].undraw()
            result2[i].undraw()
            result3[i].undraw()
            result4[i].undraw()
            result5[i].undraw()
            result6[i].undraw()
            result7[i].undraw()
            result8[i].undraw()
                ## Guessing Circles

        # Big Circles
        initial = 0 # 0 when initial (without colors),1 when otherwise
        reveal = 2
        row = 0
        guess1 = []
        for i in range(0,3*total+1,total):
                guess1.append(Circle(Point(40+i,40+total*0),bigRadius))
        guess2 = []
        for i in range(0,3*total+1,total):
                guess2.append(Circle(Point(40+i,40+total*1),bigRadius))
        guess3 = []
        for i in range(0,3*total+1,total):
                guess3.append(Circle(Point(40+i,40+total*2),bigRadius))
        guess4 = []
        for i in range(0,3*total+1,total):
                guess4.append(Circle(Point(40+i,40+total*3),bigRadius))
        guess5 = []
        for i in range(0,3*total+1,total):
                guess5.append(Circle(Point(40+i,40+total*4),bigRadius))
        guess6 = []
        for i in range(0,3*total+1,total):
                guess6.append(Circle(Point(40+i,40+total*5),bigRadius))
        guess7 = []
        for i in range(0,3*total+1,total):
                guess7.append(Circle(Point(40+i,40+total*6),bigRadius))
        guess8 = []
        for i in range(0,3*total+1,total):
                guess8.append(Circle(Point(40+i,40+total*7),bigRadius))
        width = 2
        for i in range(4):
            guess1[i].setWidth(width)
            guess2[i].setWidth(width)
            guess3[i].setWidth(width)
            guess4[i].setWidth(width)
            guess5[i].setWidth(width)
            guess6[i].setWidth(width)
            guess7[i].setWidth(width)
            guess8[i].setWidth(width)

        # Small Circles
        smallRadius = 10
        total2 = 1*bigRadius + spacing
        x = 325
        result1 = []
        for i in range(0,3*total2+1,total2):
                result1.append(Circle(Point(x+i,40+total*0),smallRadius))
        result2 = []
        for i in range(0,3*total2+1,total2):
                result2.append(Circle(Point(x+i,40+total*1),smallRadius))
        result3 = []
        for i in range(0,3*total2+1,total2):
                result3.append(Circle(Point(x+i,40+total*2),smallRadius))
        result4 = []
        for i in range(0,3*total2+1,total2):
                result4.append(Circle(Point(x+i,40+total*3),smallRadius))
        result5 = []
        for i in range(0,3*total2+1,total2):
                result5.append(Circle(Point(x+i,40+total*4),smallRadius))
        result6 = []
        for i in range(0,3*total2+1,total2):
                result6.append(Circle(Point(x+i,40+total*5),smallRadius))
        result7 = []
        for i in range(0,3*total2+1,total2):
                result7.append(Circle(Point(x+i,40+total*6),smallRadius))
        result8 = []
        for i in range(0,3*total2+1,total2):
                result8.append(Circle(Point(x+i,40+total*7),smallRadius))
        width = 2
        for i in range(4):
            result1[i].setWidth(width)
            result2[i].setWidth(width)
            result3[i].setWidth(width)
            result4[i].setWidth(width)
            result5[i].setWidth(width)
            result6[i].setWidth(width)
            result7[i].setWidth(width)
            result8[i].setWidth(width)
                 
        ## "Secret Code" Text Box
        codeText = Text(Point(6*total-30,610),"<- Secret Code !")
        codeText.setFace("courier")
        codeText.setSize(14)
        codeText.setStyle("bold")

        ## Rectangle to hide the code
        rect = Rectangle(Point(0,610-spacing-bigRadius),Point(3*total+40+bigRadius+spacing,650))
        rect.setFill("black")


        ## Choosing Colors
        
        choose_color = ["red","orange","yellow","green","blue","pink"]
        choose_color_rect = []
        choose_rect_yPos = 610-spacing-bigRadius+20
        xPos = int(500/6)
        for i in range (6):
            choose_color_rect.append(Rectangle(Point(i*xPos,choose_rect_yPos),Point((i+1)*xPos,650)))
        for i in range(6):
            choose_color_rect[i].setFill(choose_color[i])
        choose_text = Text(Point(250,610-spacing-bigRadius+7),"Choose a color!")
        choose_text.setFace("courier")
        choose_text.setSize(14)
        choose_text.setStyle("bold")
        if generate == times_played:
            code_color_list = []
            a = 0
            number = 5
            code_list = ["red","green","yellow","blue","pink","orange"]
            while a < 4:
                code_num = random.randint(0,number)
                code[a].setFill(code_list[code_num])
                code_color_list.append(code_list[code_num])
                code_list = code_list[0:code_num]+code_list[code_num+1:]
                a += 1
                number -= 1
            print(code_color_list)
            generate += 1
        if k != "" and k == 'Return':
            gamestate = 0
            winning.undraw()
            start.draw(win)
            times_played += 1
    if gamestate == 5:
        red = 0
        victory = 0
        #setUp()
        for i in range(4):
            guess1[i].undraw()
            guess2[i].undraw()
            guess3[i].undraw()
            guess4[i].undraw()
            guess5[i].undraw()
            guess6[i].undraw()
            guess7[i].undraw()
            guess8[i].undraw()
            result1[i].undraw()
            result2[i].undraw()
            result3[i].undraw()
            result4[i].undraw()
            result5[i].undraw()
            result6[i].undraw()
            result7[i].undraw()
            result8[i].undraw()
                ## Guessing Circles

        # Big Circles
        initial = 0 # 0 when initial (without colors),1 when otherwise
        reveal = 2
        row = 0
        guess1 = []
        for i in range(0,3*total+1,total):
                guess1.append(Circle(Point(40+i,40+total*0),bigRadius))
        guess2 = []
        for i in range(0,3*total+1,total):
                guess2.append(Circle(Point(40+i,40+total*1),bigRadius))
        guess3 = []
        for i in range(0,3*total+1,total):
                guess3.append(Circle(Point(40+i,40+total*2),bigRadius))
        guess4 = []
        for i in range(0,3*total+1,total):
                guess4.append(Circle(Point(40+i,40+total*3),bigRadius))
        guess5 = []
        for i in range(0,3*total+1,total):
                guess5.append(Circle(Point(40+i,40+total*4),bigRadius))
        guess6 = []
        for i in range(0,3*total+1,total):
                guess6.append(Circle(Point(40+i,40+total*5),bigRadius))
        guess7 = []
        for i in range(0,3*total+1,total):
                guess7.append(Circle(Point(40+i,40+total*6),bigRadius))
        guess8 = []
        for i in range(0,3*total+1,total):
                guess8.append(Circle(Point(40+i,40+total*7),bigRadius))
        width = 2
        for i in range(4):
            guess1[i].setWidth(width)
            guess2[i].setWidth(width)
            guess3[i].setWidth(width)
            guess4[i].setWidth(width)
            guess5[i].setWidth(width)
            guess6[i].setWidth(width)
            guess7[i].setWidth(width)
            guess8[i].setWidth(width)

        # Small Circles
        smallRadius = 10
        total2 = 1*bigRadius + spacing
        x = 325
        result1 = []
        for i in range(0,3*total2+1,total2):
                result1.append(Circle(Point(x+i,40+total*0),smallRadius))
        result2 = []
        for i in range(0,3*total2+1,total2):
                result2.append(Circle(Point(x+i,40+total*1),smallRadius))
        result3 = []
        for i in range(0,3*total2+1,total2):
                result3.append(Circle(Point(x+i,40+total*2),smallRadius))
        result4 = []
        for i in range(0,3*total2+1,total2):
                result4.append(Circle(Point(x+i,40+total*3),smallRadius))
        result5 = []
        for i in range(0,3*total2+1,total2):
                result5.append(Circle(Point(x+i,40+total*4),smallRadius))
        result6 = []
        for i in range(0,3*total2+1,total2):
                result6.append(Circle(Point(x+i,40+total*5),smallRadius))
        result7 = []
        for i in range(0,3*total2+1,total2):
                result7.append(Circle(Point(x+i,40+total*6),smallRadius))
        result8 = []
        for i in range(0,3*total2+1,total2):
                result8.append(Circle(Point(x+i,40+total*7),smallRadius))
        width = 2
        for i in range(4):
            result1[i].setWidth(width)
            result2[i].setWidth(width)
            result3[i].setWidth(width)
            result4[i].setWidth(width)
            result5[i].setWidth(width)
            result6[i].setWidth(width)
            result7[i].setWidth(width)
            result8[i].setWidth(width)
                 
        ## "Secret Code" Text Box
        codeText = Text(Point(6*total-30,610),"<- Secret Code !")
        codeText.setFace("courier")
        codeText.setSize(14)
        codeText.setStyle("bold")

        ## Rectangle to hide the code
        rect = Rectangle(Point(0,610-spacing-bigRadius),Point(3*total+40+bigRadius+spacing,650))
        rect.setFill("black")


        ## Choosing Colors
        
        choose_color = ["red","orange","yellow","green","blue","pink"]
        choose_color_rect = []
        choose_rect_yPos = 610-spacing-bigRadius+20
        xPos = int(500/6)
        for i in range (6):
            choose_color_rect.append(Rectangle(Point(i*xPos,choose_rect_yPos),Point((i+1)*xPos,650)))
        for i in range(6):
            choose_color_rect[i].setFill(choose_color[i])
        choose_text = Text(Point(250,610-spacing-bigRadius+7),"Choose a color!")
        choose_text.setFace("courier")
        choose_text.setSize(14)
        choose_text.setStyle("bold")
        if generate == times_played:
            code_color_list = []
            a = 0
            number = 5
            code_list = ["red","green","yellow","blue","pink","orange"]
            while a < 4:
                code_num = random.randint(0,number)
                code[a].setFill(code_list[code_num])
                code_color_list.append(code_list[code_num])
                code_list = code_list[0:code_num]+code_list[code_num+1:]
                a += 1
                number -= 1
            print(code_color_list)
            generate += 1
        if k != None and k == 'Return':
            gamestate = 0
            losing.undraw()
            start.draw(win)
            times_played += 1
