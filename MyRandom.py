
import re
from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
class PoissonProcess:
    ''' 
    :param lam : λ
    :param T : 生成随机数的截止时间 
    :return 满足泊松过程的数组
    生成泊松过程https://zhuanlan.zhihu.com/p/265751697  
    '''
    
    def __init__(self,lam,T):
        self.t = []
        self.lam = lam
        self.T = T
        
        n = np.random.poisson(self.lam * self.T)  # T时间内发生的次数
        # 生成n个[0, T]均匀分布随机数并排序
        self.t = np.hstack([[0], np.sort(np.random.random(n) * self.T)])
        self.t = np.rint(self.t)
        
    def random(self):
        
        return self.t

class Exponential:
    ''' 
    :param lam : 1/μ
    :return 满足负指数分布的随机数
    生成负指数分布https://zhuanlan.zhihu.com/p/265751697  
    '''
    def __init__(self,lam) -> None:
        self.lam=lam


    def random(self):
        
        return np.rint(np.random.exponential(self.lam))

if __name__ == "__main__":
    # p=PoissonProcess(1,100)
    # print(p.random())

    e=Exponential(40)
    s=[]
    for i in range(10000):  
        s.append(e.random())  
    print(s)
    print(mean(s))
    plt.hist(s, bins=80, alpha=0.7) #绘制直方图
    plt.margins(0.02) 


    plt.show()


