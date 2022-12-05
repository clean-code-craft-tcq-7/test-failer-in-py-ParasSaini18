color_map = {}

def format_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            color_map[i * 5 + j] =  '| ' +  major + ' | ' + minor

def print_color_map():
    format_color_map()
    print(color_map)