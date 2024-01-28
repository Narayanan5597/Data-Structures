from collections import defaultdict
def max_wis(Numele):
    f = defaultdict(tuple)
    f[-2] = (0,[])
    f[-1] =  (0,[])
    def recursions(i):
        if f[i] == ():

            if i < 0:
                f[i] = (Numele[i],[Numele[i]])
            else:
                a = recursions(i-2)
                b = recursions(i-1)
                c = Numele[i]+a[0]
                d = b[0]
                if c >= d: f[i] = (c, a[1] + [Numele[i]]) 
                else: f[i] = (d, b[1])
        return f[i]
    return recursions(len(Numele)-1)
    
if __name__ == "__main__":
    Numele = []
    print(max_wis(Numele))