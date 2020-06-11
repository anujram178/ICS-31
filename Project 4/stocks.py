#Ramaswamy, Anuj
class stock:
    def __init__(self):
        self.cash = 100000
        self.transactionList = []
        self.portfolioD = dict()
        self.dates = set()
    

    def readPrices(self,name1,name2,name3):
        self.name1 = name1[0:-4]
        self.name2 = name2[0:-4]
        self.name3 = name3[0:-4]
        
        self.portfolioD[self.name1] = 0
        self.portfolioD[self.name2] = 0
        self.portfolioD[self.name3] = 0
        
        self.file1 = open(name1)
        self.file2 = open(name2)
        self.file3 = open(name3)
        
        self.lst1 = []
        self.lst2 = []
        self.lst3 = []
        
        for line in self.file1:
            self.lst1.append(line)
        for i in range(len(self.lst1)):
            self.lst1[i] = self.lst1[i].strip('\n')
        for line in self.file2:
            self.lst2.append(line)
        for i in range(len(self.lst1)):
            self.lst2[i] = self.lst2[i].strip('\n')
        for line in self.file3:
            self.lst3.append(line)
        for i in range(len(self.lst1)):
            self.lst3[i] = self.lst3[i].strip('\n')



    def buy(self,stock,share,date):
        if date+stock in self.dates:
            print("Invalid Transaction")
            return
        else:
            self.dates.add(date+stock)
        price = 0
        myDate = None
        self.transactionList.append(self.userInput)
        if stock == self.name1:
            self.portfolioD[self.name1] += share
            for item in self.lst1[::-1]:
                tempDate = item[0:10]
                if date >= tempDate:
                    myDate = tempDate
                    price = float(item.split(',')[4])
                else:
                    break

        elif stock == self.name2:
            self.portfolioD[self.name2] += share
            for item in self.lst2[::-1]:
                tempDate = item[0:10]
                if date >= tempDate:
                    myDate = tempDate
                    price = float(item.split(',')[4])
                else:
                    break

        elif stock == self.name3:
            self.portfolioD[self.name3] += share
            for item in self.lst3[::-1]:
                tempDate = item[0:10]
                if date >= tempDate:
                    myDate = tempDate
                    price = float(item.split(',')[4])
                else:
                    break
        

        if self.cash - (price*share) <0:
            print("Invalid Transaction")
        else:
            self.cash -= price*share
            if date in self.portfolioD:
                self.portfolioD[date].append([stock,share,-price*share])
            else:
                self.portfolioD[date] = [[stock,share,-price*share]]

    def sell(self,stock,share,date):
        if date+stock in self.dates:
            print("Invalid Transaction")
            return
        else:
            self.dates.add(date+stock)
        price = 0
        myDate = None
        self.transactionList.append(self.userInput)
        if self.portfolioD[stock] < share:
            print("Invalid Transaction")
            return
        if stock == self.name1:
            self.portfolioD[self.name1] -= share
            for item in self.lst1[::-1]:
                tempDate = item[0:10]
                if date >= tempDate:
                    myDate = tempDate
                    price = float(item.split(',')[4])
                else:
                    break

        elif stock == self.name2:
            self.portfolioD[self.name2] -= share
            for item in self.lst2[::-1]:
                tempDate = item[0:10]
                if date >= tempDate:
                    myDate = tempDate
                    price = float(item.split(',')[4])
                else:
                    break

        elif stock == self.name3:
            self.portfolioD[self.name3] -= share
            for item in self.lst3[::-1]:
                tempDate = item[0:10]
                if date >= tempDate:
                    myDate = tempDate
                    price = float(item.split(',')[4])
                else:
                    break
                
        self.cash += price*share
        if date in self.portfolioD:
            self.portfolioD[date].append([stock,share,price*share])
        else:
            self.portfolioD[date] = [[stock,share,price*share]]
  

    def portfolio(self,date):
        summ = 100000
        D = {"AMZN":0, "FB": 0, "GOOG": 0}
        if date in self.portfolioD:
            for val in self.portfolioD[date]:
                D[val[0]] += val[1]
        for Tdate in self.portfolioD:
            if date >= Tdate:
                for val in self.portfolioD[date]:
                    summ += val[2]               
        print(f"AMZN: {D['AMZN']}, FB: {D['FB']}, GOOG: {D['GOOG']}, Cash: {summ}")
        
                       
    def transactionHistory(self,startDate, endDate):
        self.startdate = startDate
        self.enddate = endDate
        for item in self.transactionList:
            if startDate <= item[-10:] and item[-10:] <= endDate:
                print(item)

    def prices(self,date):
        for item in self.lst1[::-1]:
            tempDate = item[0:10]
            if date >= tempDate:
                myDate = tempDate
                price1 = float(item.split(',')[4])
            else:
                break
        for item in self.lst2[::-1]:
            tempDate = item[0:10]
            if date >= tempDate:
                myDate = tempDate
                price2 = float(item.split(',')[4])
            else:
                break
        for item in self.lst3[::-1]:
            tempDate = item[0:10]
            if date >= tempDate:
                myDate = tempDate
                price3 = float(item.split(',')[4])
            else:
                break
        print(f"AMZN: {price1}, FB: {price2}, GOOG: {price3}")
        



    def smarket(self):
        program = 1
        myStockSet = {"AMZN","FB","GOOG"}
        while program == 1:
            self.userInput = input("$ ")
            self.commandList = self.userInput.split()
            if self.commandList[0] == "ReadPrices":
                self.readPrices(self.commandList[1], self.commandList[2], self.commandList[3])
            elif self.commandList[0] == 'Buy':
                if self.commandList[1] not in myStockSet or self.commandList[3]> '2019-06-17' or self.commandList[3]< '2015-02-02':
                    print("Invalid Transaction")
                else:
                    self.buy(self.commandList[1],int(self.commandList[2]),self.commandList[3])
            elif self.commandList[0] == "Sell":
                if self.commandList[1] not in myStockSet or self.commandList[3]> '2019-06-17' or self.commandList[3]< '2015-02-02':
                    print("Invalid Transaction")
                else:
                    self.sell(self.commandList[1],int(self.commandList[2]),self.commandList[3])
            elif self.commandList[0] == "Portfolio":
                self.portfolio(self.commandList[1])
            elif self.commandList[0] == "TransactionHistory":
                self.transactionHistory(self.commandList[1], self.commandList[2])
            elif self.commandList[0] == "Prices":
                self.prices(self.commandList[1])
            elif self.commandList[0] == 'quit':
                program = 0
                
            
stockObject = stock()
stockObject.smarket()


