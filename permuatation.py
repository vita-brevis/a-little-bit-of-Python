taken = []

def process(X):
     print X

def recurse(li, X, i, n):
     if i == n:
          process(X[0:i])
     else:
          for j in range(0, n):
               if taken[j] == False:
                    taken[j] = True
                    X.append(li[j])
                    recurse(li, X, i+1, n)
                    taken[j] = False
                    X.pop(i)

if __name__ == "__main__":
     li = [1, 2, 3, 4]
     X = []
     taken.extend([False, False, False, False])
     print taken
     recurse(li, X, 0, li.__len__())  
