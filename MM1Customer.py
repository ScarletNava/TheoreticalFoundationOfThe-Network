

class Customer:
    def __init__(self,arriveTime,serviceTime) -> None:
        '''
        :parma arriveTime 顾客到达的时间
        :parma serviceTime 顾客需要服务的时间
        :parma waitingTime 顾客排队等待的时间
        :parma startServiceTime 顾客开始被服务的时间
        :parma 
        
        '''
        self.arriveTime = arriveTime
        self.serviceTime = serviceTime

        self.waitingTime = 0
        self.startServiceTime = 0

        pass