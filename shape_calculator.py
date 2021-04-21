class Rectangle:
  def __init__(self,width,height):
        self.width=width
        self.height=height
    def set_width(self,width):
        self.width=width
    def set_height(self,height):
        self.height=height
    def get_area(self):
        return self.width*self.height
    def get_perimeter(self):
        return (2*self.width+2*self.height)
    def get_diagonal(self):
        return (self.width**2+self.height**2)**0.5
    def get_picture(self):
        string=""
        if(self.width>50 or self.height>50):
            string="Too big for picture."
            return string
        for j in range(0,self.height):
            for i in range(0,self.width):
                string+="*"
            string+="\n"
        return string
    def get_amount_inside(self,shape):
        return self.get_area()//shape.get_area()
    def __str__(self):
        string_to_be_disp="Rectangle"+"("+"width"+"="+str(self.width)+","+" height"+"="+str(self.height)+")"
        return string_to_be_disp  
class Square:
 def __init__(self,side):
        self.side=side
        super().__init__(self.side,self.side)
    def set_side(self,side):
        self.side=side
        super().set_width(self.side)
        super().set_height(self.side)
    def __str__(self):
        string="Square("+"side="+str(self.side)+")"
        return string
    def set_width(self,side):
        super().set_width(self.side)
        self.set_side(side)
    def set_height(self,side):
        super().set_height(self.side)
        self.set_side(side)
