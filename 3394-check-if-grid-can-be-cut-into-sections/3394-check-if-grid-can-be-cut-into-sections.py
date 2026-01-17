class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def can_cut(start_cords,end_cords):
            m = len(start_cords)
            start_cords.sort()
            end_cords.sort()
            all_cords = sorted(set(start_cords+end_cords))
            valid_cords = [] #cords at which we can cut
            for cord in all_cords:
                #num of active rectangles = #rects that begin < cord - #rect that end <=cord
                active_rects = bisect_left(start_cords,cord) - bisect_right(end_cords,cord)
                if active_rects==0: valid_cords.append(cord)
            if len(valid_cords)<2: return False
            
            valid_bottom_cord = None
            bottom_rects = 0
            top_rects = 0
            middle_rects = 0
            for cord in valid_cords:
                if valid_bottom_cord is None:
                    bottom_cords = bisect_right(end_cords,cord)
                    if bottom_cords==0: continue
                    valid_bottom_cord = bottom_cords
                    bottom_rects = bottom_cords
                
                else:
                    #middle number of rectangles and top
                    top_rects = m - bisect_left(start_cords,cord)
                    middle_rects = m - top_rects -bottom_rects
                    if top_rects>0 and middle_rects>0: return True
            return False
        return can_cut([x[0] for x in rectangles],[x[2] for x in rectangles]) or can_cut([x[1] for x in rectangles],[x[3] for x in rectangles]) 


                    
