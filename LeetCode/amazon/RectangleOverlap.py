
def RectangleOverlap(rect1,rect2):
    min_x1 = min(rect1[0],rect1[2])
    min_x2 = min(rect2[0],rect1[2])

    min_y1 = min(rect1[1],rect1[3])
    min_y2 = min(rect2[1],rect2[3])

    if  min_x1<rect2[0]  and rect2[0] < rect1[2] or min_x2 < rect1[0] and rect1[0] <rect2[2]:
        if  min_y1<rect2[1]  and rect2[1] < rect1[3] or min_x2 < rect1[1] and rect1[1] <rect2[3]:
            return True

if __name__== "__main__":
    rect1 = [0,0,2,2]
    rect2 = [1,1,3,3]
    print (RectangleOverlap(rect1,rect2))
