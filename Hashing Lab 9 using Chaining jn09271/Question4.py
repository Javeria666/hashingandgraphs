from Question3 import *

def delete(hashtable, key, size):
    hashvalue = hash_function(key,size)
    j=-1
    for i in range(len(hashtable[0][hashvalue])):
        if hashtable[0][hashvalue][i]==key:
            j=i
    if j>=0:
        hashtable[0][hashvalue][j] = "#"
        hashtable[1][hashvalue][j] = "#"
    else:
        print("Error: key not found")



if __name__ == "__main__":
    H = create_hashtable(10)
    put(H,5,3,10)
    delete(H,5,10)
    print(H)
    # Should print ([None, None, None, None, None, '#', None, None, None, None], [None, None, None, None, None, '#', None, None, None, None])