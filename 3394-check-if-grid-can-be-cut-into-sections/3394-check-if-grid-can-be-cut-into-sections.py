class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def can_cut(start_cords,end_cords):
            m = len(start_cords)
            start_cords.sort()
            end_cords.sort()
            valid_cords = []
            all_cords = sorted(set(start_cords+end_cords))
            for cord in all_cords:
                #Number of rectangles = #rect with start <cord - #rect with end<=c
                active_rects = bisect_left(start_cords,cord)-bisect_right(end_cords,cord)
                if active_rects==0: valid_cords.append(cord)
            bottom_rects = None
            for cord in valid_cords:
                if bottom_rects==None:
                    temp = bisect_right(end_cords,cord)
                    if temp>0: bottom_rects = temp
                else:
                    top_rects = m - bisect_left(start_cords,cord)
                    middle_rects = m - top_rects-bottom_rects
                    if top_rects>0 and middle_rects>0: return True
            return False
        return can_cut([r[0] for r in rectangles],[r[2] for r in rectangles]) or can_cut([r[1] for r in rectangles],[r[3] for r in rectangles])



        