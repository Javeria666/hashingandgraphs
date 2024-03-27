from Question1 import *
from Question2 import *

def put(hashtable,key, data,size):
    iteration=0
    hashvalue = hash_function(key,size)
    if hashtable[0][hashvalue]==None:
        hashtable[0][hashvalue]=key
        hashtable[1][hashvalue]=data
    else:
        if hashtable[0][hashvalue]==key:
            hashtable[1][hashvalue]=data
        else:
            newhash = collision_resolver(hashvalue,size,iteration)
            while hashtable[0][newhash] != None and hashtable[0][newhash]!=key and iteration!=size:
                iteration+=1
                newhash = collision_resolver(hashvalue,size,iteration)
            if hashtable[0][newhash]==None:
                hashtable[0][newhash]=key
                hashtable[1][newhash]=data
            else:
                #if hashtable[0][newhash] == key:
                hashtable[1][newhash]=data



def get(hashtable,key,size):
    start = hash_function(key,size)
    pos = start
    iteration=0
    while hashtable[0][pos]!=None:
        if hashtable[0][pos]==key:
            return hashtable[1][pos]
        else:
            pos = collision_resolver(start,size,iteration)
            while hashtable[0][pos]!=None and hashtable[0][pos]!=key:
                iteration+=1
                pos = collision_resolver(start,size,iteration)
                if iteration==size:
                    return None


if __name__ == "__main__":
    H = create_hashtable(10)
    put(H,5,3,10)
    print(get(H,5,10)) # Should print 3