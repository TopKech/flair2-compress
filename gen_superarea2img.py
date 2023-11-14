from collections import defaultdict
from tqdm import tqdm

from utils.io import  write_json
from settings import superarea2img_path, raw_aerial_path


superarea2img = defaultdict(list)
for path in tqdm(list(raw_aerial_path.rglob("*.tif"))):
    img = str(path.stem)
    superarea = str(path.relative_to(raw_aerial_path).parent.parent)
    superarea2img[superarea].append(img)

write_json(superarea2img_path, superarea2img)
