# --------------------------------     
# CROPPING FUNCTIONS
# --------------------------------
# Methodology
# crop mode -> crop -> rename the category, add the category, shows up as image + add table

def start_cropping(event, image_visual):
    start_x = image_visual.canvasx(event.x)
    start_y = image_visual.canvasy(event.y)
    current_crop = image_visual.create_rectangle(start_x, start_y, start_x, 
                                                      start_y, outline="yellow", width=4)
    start_coord = (start_x, start_y)
    return current_crop, start_coord


def draw_rectangle(event, image_visual, current_crop, start_coord):
    start_x, start_y = start_coord
    cur_x = image_visual.canvasx(event.x)
    cur_y = image_visual.canvasy(event.y)
    image_visual.coords(current_crop, start_x, start_y, cur_x, cur_y)


def end_cropping(event, image_visual, current_crop, start_coord):
    start_x, start_y = start_coord
    end_x = min(max(event.x, 0), image_visual.winfo_width())
    end_y = min(max(event.y, 0), image_visual.winfo_height())
    image_visual.itemconfig(current_crop, outline="lime")
    x1 = min(start_x, end_x)
    y1 = min(start_y, end_y)
    x2 = max(start_x, end_x)
    y2 = max(start_y, end_y)

    coordinates = (x1, y1, x2, y2)
        
    # Calculate the width and height of the cropped area
    width = x2 - x1
    height = y2 - y1
    print(f'Cropped: {x1}, {y1}, {x2}, {y2}')
    adjust_cropping(image_visual=image_visual, current_crop=current_crop, coordinates=coordinates)

    return current_crop, coordinates

def adjust_cropping(self, image_visual, current_crop, coordinates):
    x1, y1, x2, y2 = coordinates
    image_visual.coords(current_crop, x1, y1, x2, y2)