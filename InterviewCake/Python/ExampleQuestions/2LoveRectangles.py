#Find if you have a good match on Tinder
#Love Rectangles
def range_overlap(p1,l1,p2,l2):
    highest_start = max(p1,p2)
    low_corner = min(p1+l1,p2+l2)

    #overlap check:
    if highest_start >= low_corner:
        return (None,None)
    #Compute overlap length
    overlap_length = low_corner - highest_start
    return (highest_start,overlap_length)

def find_rectangular_overlap(my_rect1, my_rect2):
    #Find range_overlap in x and y coordinate
    x_intersect, x_overlap = range_overlap(my_rect1['left_x'],
    my_rect1['width'],my_rect2['left_x'],my_rect2['width'])
    y_intersect, y_overlap = range_overlap(my_rect1['bottom_y'],
    my_rect1['height'],my_rect2['bottom_y'],my_rect2['height'])

    if not x_overlap or not y_overlap:
        return {'left_x':None,
        'bottom_y':None,
        'width':None,
        'height':None}


    return {'left_x':x_intersect,
    'bottom_y':y_intersect,
    'width':x_overlap,
    'height':y_overlap}

#Now interviewer is gonna ask: Tell me about the space and time complexity:
#O(1) time O(1) space


#Now What if we had a list of rectangles and wanted to find all the rectangular
#overlaps between all of them, if there was one?
def make_pairs(full_list):
    pairs = [[full_list[a],full_list[b]] for a in range(len(full_list)-1) for b in range(1,len(full_list)) if not a==b]
    return pairs

def rect_overlaps(rect_pairs):
    intersections = []
    for pair in rect_pairs:
        _, x_overlap = range_overlap(pair[0]['left_x'],pair[0]['width'],
        pair[1]['left_x'],pair[1]['width'])

        _,y_overlap  = range_overlap(pair[0]['bottom_y'],pair[0]['height'],
        pair[1]['bottom_y'],pair[1]['height'])

        if x_overlap or y_overlap:
            intersections.append(pair)
    return intersections


if __name__ == '__main__':
    my_rect1 = {'left_x':1,
    'bottom_y':1,
    'width':6,
    'height':3}

    my_rect2 = {'left_x':5,
    'bottom_y':3,
    'width':7,
    'height':9}

    my_rect3 = {'left_x':5,
    'bottom_y':3,
    'width':7,
    'height':9}

    my_rect4 = {'left_x':5,
    'bottom_y':3,
    'width':7,
    'height':9}

    my_rect5 = {'left_x':5,
    'bottom_y':3,
    'width':7,
    'height':9}

    my_rect6 = {'left_x':5,
    'bottom_y':3,
    'width':7,
    'height':9}


    full_list = [my_rect1,my_rect2,my_rect3,my_rect4,my_rect5,my_rect6]
    #full_list = ['1','2','3','4','5','6']
    rect_pairs     = make_pairs(full_list)

    intersections = rect_overlaps(rect_pairs)

    print (intersections)
