def draw_box(height, width):
    for i in range(height):
        if i == 0 or i == height - 1:
            print('* ' * width)
        else:
            print('*' + ' ' * (2 * width - 3) + '*')

def main():
    height = int(input("Enter height: "))
    width = int(input("Enter width: "))
    draw_box(height, width)