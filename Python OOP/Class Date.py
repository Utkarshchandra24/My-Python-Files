class Date:
    def __init__(self,d,m,y):
        self.d=d
        self.m=m
        self.y=y

    def is_valid(self):
        pass

    def add_day(self,days):
        pass

    def add_days(self,days):
        pass

    def find_weekday(self):
        pass

    @staticmethod
    def is_leap(year):
        if year%4==0 and year%100 !=0 or year%400==0:
            return True
        else:
            return False

    
