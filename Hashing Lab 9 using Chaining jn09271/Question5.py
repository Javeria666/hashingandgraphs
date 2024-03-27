from Question4 import *

def main(to_put,to_delete,to_get,size): # returns tuple(list,hash table)
    hashtable = create_hashtable(size)
    for tup in to_put:
        put(hashtable,tup[0], tup[1],size)
    for key in to_delete:
        delete(hashtable, key, size)
    
    getoutput=[]
    for key in to_get:
        getoutput.append(get(hashtable,key,size))    

    return (getoutput,hashtable)


    

if __name__ == "__main__":
    size = 5
    to_put = [(1 ,2) ,(" key "," value")]
    to_delete = [1]
    to_get = [" key "]
    print(main (to_put , to_delete , to_get , size))
    # Shoud print ([' value '], ([None, '#', None, ' key ', None], [None, '#', None, ' value ', None]))