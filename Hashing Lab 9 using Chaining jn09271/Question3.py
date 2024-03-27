from Question1 import *
from Question2 import *


def put(hashtable,key, data,size):
    hashvalue = hash_function(key,size)
    hashtable[0][hashvalue].append(key)
    hashtable[1][hashvalue].append(data)


def get(hashtable,key,size):
    hashvalue = hash_function(key,size)
    j = -1
    for i in range(len(hashtable[0][hashvalue])):
        if key == hashtable[0][hashvalue][i]:
            j = i

    if j>=0:
        return hashtable[1][hashvalue][j]
    else:
        return None
 
    

if __name__ == "__main__":
    H = create_hashtable(10)
    put(H,5,3,10)
    print(get(H,5,10)) # Should print 3