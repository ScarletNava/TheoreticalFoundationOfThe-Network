import MM1Sever
import numpy as np






def mm1():
    # 在这改参数
    lam = 0.09 # λ
    mu = 0.1 # μ
    rou = lam/mu
    E_N = rou/(1-rou)
    T = 1/(mu-lam)

    cacheLengthList = []
    waitingTimeList = []

    print("理论值\nλ:%f\nμ:%f\nrou:%f\nE[N]:%f\nT:%f"%(lam,mu,rou,E_N,T))



    # 多次实验取平均
    for i in range(50):

        sever = MM1Sever.Sever(lam,1/mu,5000,False,[])

        sever.startSimulation()

        cacheLength,waitingTime = sever.statistics()
        cacheLengthList.append(cacheLength)
        waitingTimeList.append(waitingTime)

        print("平均队长:%.3f\t平均等待时间:%.3f"%(cacheLength,waitingTime))
    
    print("\n\n经过多次实验求平均后：")
    print("平均队长：% .3f"%np.mean(cacheLengthList))
    print("平均等待时间：% .3f"%np.mean(waitingTimeList))


def _2_mm1():
    # 在这改参数
    lam = 0.09 # λ
    mu_1 = 0.1
    mu_2 = 0.1

    T = 1/(mu_1-lam)+1/(mu_2-lam)

    # cacheLengthList = []
    waitingTimeList = []

    print("理论值\nλ:%f\nμ1:%f\nμ2:%f\nT:%f"%(lam,mu_1,mu_2,T))




    # 多次实验取平均
    for i in range(50):

        # mm1
        sever = MM1Sever.Sever(lam,1/mu_1,5000,False,[])
        sever.startSimulation()
     
        cacheLength,waitingTime_1 = sever.statistics()
        # cacheLengthList.append(cacheLength)      
        # print(sever.finishServicingTime)

        # 第二个mm1

        a = sever.finishServicingTime
        b=[]
        for i in range(len(a)):
            b.append(np.array(a[i]))
        c=np.array(b)
        sever_2 = MM1Sever.Sever(lam,1/mu_2,5000,True,c)
        sever_2.startSimulation()
        cacheLength,waitingTime_2 = sever.statistics()
        waitingTime = waitingTime_1+waitingTime_2
        waitingTimeList.append(waitingTime)

        print("平均等待时间:%.3f"%(waitingTime))

    print("\n\n经过多次实验求平均后：")
    print("平均等待时间：% .3f"%np.mean(waitingTimeList))


# mm1()
_2_mm1()