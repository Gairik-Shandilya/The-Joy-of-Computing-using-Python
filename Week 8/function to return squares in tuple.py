#Given a Tuple T, create a function squareT that accepts one argument and 
#returns a tuple containing similar elements given in tuple T and its sqaures in sequence.

def squareT(T):
  return(T+tuple([i*i for i in T]))
if __name__ == "__main__":
    n = int(input())
    L = list(map(int, input().split()))
    T = tuple(L)
    ans = squareT(T)
    if type(ans) == type(T):
        print(ans)
