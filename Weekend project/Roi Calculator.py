#Create a program to calculate the ROI on an income property, using Object oriented programming anad four-square method
#Establish variables we want to use
#Define funcion and any variables we want to pass to the function


Investment = 300,000
RentalIncome = 2,100
Loss = 1,650
CashFlow = 1,150
TotalInvestment = 40,000
AnnualCashflow = 5,400


class ROIcalculator():
    def __init__(self,CashFlow,RentalIncome,Loss,AnnualCashflow,ROI):
        self.CashFlow = CashFlow
        self.Loss = Loss
        self.RentalIncome = RentalIncome
        self.AnnualCashflow = AnnualCashflow
        self.ROI = ROI
        

    def subtraction(self):
        print("Sum:",self.RentalIncome-Loss)
        #sum is Annual Income

    def division(self):
        print("Division :",self.AnnualCashflow/TotalInvestment * 100)
        # sum will be the ROI -however we will need to multiply by 100 to get percentage

    input(input("Enter AnnualCashflow amount then total investment amount :"))
n1ROIcalculator=(RentalIncome,Loss) 
n2ROIcalculator=(5400,40000) 

n1.subtraction()
n2.multiplication()