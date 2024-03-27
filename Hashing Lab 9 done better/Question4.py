from Question3 import *

def delete(hashtable, key, size):
    newhash=0
    iteration=0
    hashvalue = hash_function(key,size)
    if hashtable[0][hashvalue]!=key:
        while hashtable[0][newhash]!=key or iteration!=size:
            newhash = collision_resolver(hashvalue,size,iteration)
            iteration+=1
        if hashtable[0][newhash] ==key:
            hashtable[0][newhash]="#"
            hashtable[1][newhash]="#"
        else:
            print("error not found key")
    else:
        hashtable[0][hashvalue]="#"
        hashtable[1][hashvalue]="#"
if __name__ == "__main__":
    H = create_hashtable(10)
    put(H,5,3,10)
    delete(H,5,10)
    print(H)
    # Should print ([None, None, None, None, None, '#', None, None, None, None], [None, None, None, None, None, '#', None, None, None, None])