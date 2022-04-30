import MM1Sever
import numpy as np
lam = 0.09
mu = 1/10
rou = lam/mu
E_N = rou/(1-rou)
T = 1/(mu-lam)

cacheLengthList = []
waitingTimeList = []

print("理论值\nλ:%f\nμ:%f\nrou:%f\nE[N]:%f\nT:%f"%(lam,mu,rou,E_N,T))

for i in range(50):

    sever = MM1Sever.Sever(lam,1/mu,5000)

    sever.startSimulation()


    cacheLength,waitingTime = sever.statistics()
    cacheLengthList.append(cacheLength)
    waitingTimeList.append(waitingTime)

print("平均队长：%3f"%np.mean(cacheLengthList))
print("平均等待时间：%3f"%np.mean(waitingTimeList))