class MovingAverage:
    def __init__(self, lista):
        a = self.a

    def compute(self):
        x=0
        print("[", end ="")
        while x<(len(a)-1):

            med = (a[x]+a[x+1])/2

            if x==0:
                pass
            else:
                print(",", end ="")

            print(med, end ="")
            x=x+1
        print("]")

result = MovingAverage([2,4,8,16])
compute.result
