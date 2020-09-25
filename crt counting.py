import collections
S = input("Enter the string")
frequencies = collections.Counter(S)
repeated = {}

for key,value in frequencies.items():


    if value>= 1:
        repeated[key] = value
print("The number of repeated strings")
for S in sorted(S,key=repeated.get,reverse=True):
   print(S,"=>", repeated[S])
#for S in sorted(S, key=repeated.get,reverse=true):
 # print (S, repeated[S])
