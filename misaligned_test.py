import misaligned

def test_print_color_map():
    assert(misaligned.result == 25)
    assert(misaligned.result("White", "Blue") == 0)
    assert(misaligned.result("White", "Slate") == 4)
    assert(misaligned.result("Red", "Blue") == 5)
    assert(misaligned.result("Red", "slate") == 9)
    assert(misaligned.result("Black", "Blue") == 10)
    assert(misaligned.result("Black", "Green") == 12)
    assert(misaligned.result("Black", "Slate") == 14)
    assert(misaligned.result("Yellow", "Blue") == 15)
    assert(misaligned.result("Yellow", "Slate") == 19)
    assert(misaligned.result("Voilet", "Blue") == 20)
    assert(misaligned.result("Voilet", "Slate") == 24)

if __name__ == '__main__':
    test_print_color_map()
    
print("All is well (maybe!)\n")  