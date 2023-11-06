class shape:
    def __init__(self,color):
        self.color=color
    class rect(shape):
        def __init__(self,color,width,height):
            self.width=width
            self.height=height
    class sqr(rect):
        def __init__(self, color,side):
            self.side=side