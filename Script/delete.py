import os
root_dir = '.'

def delete_images(directory):
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        
        if os.path.isdir(item_path):
            delete_images(item_path)
        elif item.lower().endswith(('.jpg', '.png', '.jpeg', '.gif', 'webp', '.jfif', '.avif')):
            os.remove(item_path)
            print(f'Removed {item}')
delete_images(root_dir)