class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(status)
        boxes_to_open = initialBoxes 
        result = 0 
        opened = True 
        while opened:
            ind = 0
            opened = False
            while ind < len(boxes_to_open):
                box = boxes_to_open[ind]
                if status[box]:
                    result += candies[box]
                    for key in keys[box]:
                        status[key] = 1 
                    boxes_to_open.extend(containedBoxes[box])
                    if ind == len(boxes_to_open)-1:
                        boxes_to_open.pop()
                    else:
                        boxes_to_open[ind] = boxes_to_open.pop()
                    opened = True 
                else:
                    ind += 1 
        return result 
