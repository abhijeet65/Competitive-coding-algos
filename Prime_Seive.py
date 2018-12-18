'''
Created on Jul 1, 2017

@author: Abhijeet Saraf
'''
#Complexity: O(n * log2(log2(n)))
def getPrimeSieve(N):
    primes=[0]*N
    primes[1]=1
    primes[2]=2
    j=4
    while(j<N):
        primes[j]=2
        j+=2
    j=3
    while(j<N):
        if primes[j]==0:
            primes[j]=j
            i=j*j
            k=j<<1
            while(i<N):
                primes[i]=j
                i+=k
        j+=2
        
    return primes;    