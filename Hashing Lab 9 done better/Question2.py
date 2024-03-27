def hash_function(key,size):
    if type(key)==int:
        index = key%size
        return index
    elif type(key)==str:
        sum=0
        for i in key:
            sum+=ord(i)
        return sum%size


def collision_resolver(key,size, iteration):
    return (key+iteration)%size

if __name__ == "__main__":
    print(hash_function(5,10)) # Should print 5
    print(hash_function("Hello", 10)) # Should print 0
    print(collision_resolver(hash_function("Hello", 10),10,2)) # Should print 2