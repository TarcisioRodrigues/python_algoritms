#Comum
# def fatorial (n):
#   total, k = 1, 1
#   while k <= n:
#     total, k = total * k, k + 1
#   return total

# fatorial(7)

#Recursiva
n=5
def fatorial(n):
  if n == 1:
    return 1
  else:
    return n * fatorial(n-1)
  
  
