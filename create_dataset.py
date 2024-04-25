import os
from PIL import ImageFile, Image
from tqdm import tqdm

from data.caption import make_caption_from_id
from data.db import load_db


ImageFile.LOAD_TRUNCATED_IMAGES = True
Image.MAX_IMAGE_PIXELS = None

db = load_db("/data/jwang/db2023/danbooru2023.db")
root_dir = "/data/jwang/danbooruindex/"


for sub_folder in os.listdir(root_dir):
    for item in os.listdir(os.path.join(root_dir, sub_folder)):
        print(os.path.join(root_dir, sub_folder, item))
        id = int(os.path.basename(item).split('.')[0])
        if os.path.exists(os.path.join(root_dir, sub_folder, str(id) + '.txt')):
            pass
        else:
            caption = make_caption_from_id(id, processor=[])
            with open(os.path.join(root_dir, sub_folder, str(id) + '.txt'), 'w') as file:
                file.write(caption)