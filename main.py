import MyRandom

p=MyRandom.PoissonProcess(1,100)

print(p.random())

e=MyRandom.Exponential(5)
for i in range(100):
    print(e.random())



