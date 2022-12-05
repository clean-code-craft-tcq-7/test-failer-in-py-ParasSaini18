import misaligned

def test_format_color_map():
    misaligned.format_color_map()
    assert(misaligned.color_map[0] == '| White | Blue' )
    assert(misaligned.color_map[4] == '| White | Slate' )
    assert(misaligned.color_map[5] == '| Red | Blue' )
    assert(misaligned.color_map[9] == '| Red | Slate' )
    assert(misaligned.color_map[10] == '| Black | Blue' )
    assert(misaligned.color_map[14] == '| Black | Slate' )
    assert(misaligned.color_map[20] == '| Violet | Blue' )
    assert(misaligned.color_map[24] == '| Violet | Slate' )
    assert(misaligned.color_map[2] == '| White | Green' )

if __name__ == '__main__':
    test_format_color_map()
    
print("All is well (maybe!)\n")