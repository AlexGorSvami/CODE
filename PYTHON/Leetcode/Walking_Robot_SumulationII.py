class Robot:

    def __init__(self, width: int, height: int):
        self.width = width 
        self.height = height 
        self.perimeter = (self.width + self.height) * 2 - 4 
        self.pos = 0
        self.dir = 1 
        self.moved = False 
        self.num = 0
        
    def step(self, num: int) -> None:
        self.num += num 
        self.moved = True

    def _calc(self):
        self.num %= self.perimeter 
        if not self.num:
            self.num = self.perimeter 
        while self.num:
            next = self.pos + self.dir 
            if not (0 <= next.real < self.width and 0 <= next.imag < self.height):              
                self.dir *= 1j
                continue 
            if self.dir.real:
                step_limit = abs([None, self.width - 1, 0][int(self.dir.real)] - self.pos.real)
            else:
                step_limit = abs([None, self.height - 1, 0][int(self.dir.imag)] - self.pos.imag)
            step = min(step_limit, self.num)
            self.pos += self.dir * step 
            self.num -= step 
        self.moved = False 


    def getPos(self) -> List[int]:
        if self.moved:  
            self._calc()
        return [int(self.pos.real), int(self.pos.imag)]
    
    def getDir(self) -> str:
        if self.moved:
            self._calc()
        return [[None, 'North', 'South'], ['East'], ['West'],][int(self.dir.real)][int(self.dir.imag)]

