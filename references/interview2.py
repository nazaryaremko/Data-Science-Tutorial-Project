'''

Sample input: 6 4 "x"
Sample output:
+----+
|xxxx|
|xxxx|
+----+

width/height >2
++
++

'''
# print '+' + width-2 * '-' + '+'
# for i range(height -2):
    #print '|' + width-2 * char + '|'
# print '+' + width-2 * '-' + '+'

'''
Sample inputs:
canvas: 40 20
rectangles:
4 2 12 5 "X"
6 5 5 9 "/"
23 5 8 12 "o"
2 8 33 4 "*"

Sample output:
........................................
........................................
....+----------+........................
....|XXXXXXXXXX|........................
....|XXXXXXXXXX|........................
....|X+---+XXXX|.......+------+.........
....+-|///|----+.......|oooooo|.........
......|///|............|oooooo|.........
..+-------------------------------+.....
..|*******************************|.....
..|*******************************|.....
..+-------------------------------+.....
......|///|............|oooooo|.........
......+---+............|oooooo|.........
.......................|oooooo|.........
.......................|oooooo|.........
.......................+------+.........
........................................
........................................
........................................


'''

def createRectangle(width, height, character):
    print('+' + (width-2) * '-' + '+')
    for i in range(height -2):
        print('|' + (width-2) * character + '|')
    print('+' + (width-2) * '-' + '+')


def createCanvas(width, height, rectangles):
    canvas = [['.' for _ in range(width)] for _ in range(height)]
    
    for right, down, width_rec, heigh_rec, character in rectangles:
        #print(canvas[down][right:right+width_rec])
        #print([['+'] + ['-' for i in range(width_rec-2)] + ['+']])
        canvas[down][right:right+width_rec] = ['+'] + ['-' for i in range(width_rec-2)] + ['+']
        for i in range(heigh_rec-2):
            canvas[down+1+i][right:right+width_rec] = ['|'] + [character for i in range(width_rec-2)] + ['|']
        canvas[down+heigh_rec][right:right+width_rec] = ['+'] + ['-' for i in range(width_rec-2)] + ['+']

    for row in canvas:
        print(('').join(row))

print(createCanvas(20, 20, [[4, 2, 12, 5, "X"]]))
