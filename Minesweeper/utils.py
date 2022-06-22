from Minesweeper import settings

def height_percentage(percentage):
    return (settings.HEIGHT / 100) * percentage

# TEST OF FUNCTION
# print(height_percentage(25))

def width_percentage(percentage):
    return (settings.WIDTH / 100) * percentage
