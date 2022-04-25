class FourCal:
    def setdata(sel, fir, sec):
        sel.fir = fir
        sel.sec = sec
    
    def add(sel):
        result = sel.fir + sel.sec
        return result
    
a = FourCal()
a.setdata(4, 2)
print(a.add())