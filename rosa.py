#Complementing a DNA strand
# from dataclasses import replace
# import sys

# if sys.argv[1] == "sample":
#     data = "AAAACCCGGT"
# else:
#     data = open(sys.argv[1]).read()

# def complement(dnafile):
#     compDNA =""
#     for nuc in dnafile:
#         if nuc == "A": compDNA += nuc.replace("A", "T")
#         elif nuc == "T": compDNA += nuc.replace("T", "A")
#         elif nuc == "C": compDNA += nuc.replace("C", "G")
#         elif nuc == "G": compDNA += nuc.replace("G", "C")
#     return compDNA[::-1]

# print(complement(data))

# Fibonacci
# cache = {}

# def fibo(n, k=1): #where n is the number of months and k is the number of new offspring per breeding age rabbit every month
#     cache = {}
    
#     def cacheUpdate(k=1):
#         cache = {1:1, 2:1, 3:(1+k), 4:((1+k)+k)}
    
#     cacheUpdate(k)
#     print(cache)
#     if n in cache:
#         return cache[n]
#     else:
#         cache[n] = (fibo(n-1) + ((fibo(n-2)*k)))
#         print(cache)
#         return cache[n]
    

# print(fibo(5, 3))

with open.

cache = {1:1, 2:1} #Tout fonctionne si j'écris directement 3:4, 4:7, mais évidemment on ne veut pas ça

def fibo(n, k=1):
    cache[3] = (cache[2]+k)
    cache[4] = (cache[3]+k)
    print(cache) #Correct, donne {1: 1, 2: 1, 3: 4, 4: 7}

    if n in cache: #Ici, oublie le cache précédent
        return cache[n]
    cache[n] = fibo(n-1) + (fibo(n-2)*k)
    print(cache)
    return cache[n]

print(fibo(5, 3))