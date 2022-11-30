import tshirts

def tshirt_test():
    assert(tshirts.size(37) == 'S')
    assert(tshirts.size(38) == 'M')
    assert(tshirts.size(40) == 'M')
    assert(tshirts.size(42) == 'L')
    assert(tshirts.size(43) == 'L')
    
if __name__ == '__main__':
    tshirt_test()

print("All is well (maybe!)\n")