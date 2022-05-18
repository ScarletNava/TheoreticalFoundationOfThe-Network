
from pickle import FALSE
import MM1Customer
import MyRandom
import numpy as np
class Sever:


    def __init__(self,lam,mu,endTime,connection,arriveTimeList) -> None:
        self.lam = lam
        self.mu = mu
        self.endTime = endTime
        self.customerList = []
        self.cache = [] #缓存

        self.idle = True #空闲
        self.servicing = None

        self.cacheLength = []

        self.finishServicingTime = []

        if(not connection):
            # 获取顾客到达时间
            arriveTimeList=MyRandom.PoissonProcess(self.lam,self.endTime).random()
            # print(arriveTimeList)
        

        # 获取顾客数量
        self.customerNum = arriveTimeList.size
        # print("顾客数量为",self.customerNum)

        # 初始化顾客
        exponential = MyRandom.Exponential(mu)
        for arriveTime in arriveTimeList:

            serviceTime = exponential.random()

            customer = MM1Customer.Customer(arriveTime,serviceTime)
            self.customerList.append(customer)

        # print("到达时间 | 服务时间")
        # for each in self.customerList:
        #     print("%8d |%8d"%(each.arriveTime,each.serviceTime))

    def startSimulation(self):
        
        # 推进仿真时间
        for currentTime in range(self.endTime):

            # print("当前时间：",currentTime)
            
            # 将当前到达的顾客放入缓存
            for customer in self.customerList:
                if customer.arriveTime == currentTime :
                    self.cache.append(customer)

            # 如果当前空闲 并且 缓存不为空 -> 服务缓存中的第一个顾客
            if self.idle and self.cache!=[]:
                # 开始服务缓存中的第一个顾客
                self.servicing = self.cache[0]
                self.cache.pop(0)
                self.servicing.startServiceTime = currentTime
                self.idle = False
                # print("开始服务顾客，到达时间%d,服务时间%d"%(self.servicing.arriveTime,self.servicing.serviceTime))

            # 开始服务或服务中
            if self.idle == False:

                # print("服务中")

                #判断服务完成
                if currentTime + 1 - self.servicing.startServiceTime == self.servicing.serviceTime:
                    
                    # print("服务完成")

                    self.finishServicingTime.append(currentTime)

                    self.idle = True
                    self.servicing = None

            # 有顾客在等待
            if self.cache!=[]:
                for customer in self.cache:
                    customer.waitingTime += 1

            self.cacheLength.append(len(self.cache))



    def statistics(self):
        waitingTimeList = []
        for customer in self.customerList:
            waitingTimeList.append(customer.waitingTime)

        
        

        return np.mean(self.cacheLength),np.mean(waitingTimeList)


  






