from PIL import Image

def remove_background():
    img = Image.open('img/gamer.png').convert("RGBA")
    width, height = img.size
    pixels = img.load()
    
    visited = set()
    queue = []
    
    for x in range(width):
        queue.append((x, 0))
        queue.append((x, height - 1))
    for y in range(height):
        queue.append((0, y))
        queue.append((width - 1, y))
        
    head = 0
    while head < len(queue):
        x, y = queue[head]
        head += 1
        
        if (x, y) in visited:
            continue
        visited.add((x, y))
        
        r, g, b, a = pixels[x, y]
        if r > 230 and g > 230 and b > 230 and a > 0:
            pixels[x, y] = (255, 255, 255, 0)
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < width and 0 <= ny < height:
                    if (nx, ny) not in visited:
                        queue.append((nx, ny))

    img.save('img/gamer.png')

remove_background()
print("Done")
