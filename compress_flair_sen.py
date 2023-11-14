import numpy as np
import cv2
from tqdm import tqdm

from utils.io import write_image, read_json
from settings import raw_aerial_path, raw_sen_path, sen_path, img2centroid_path


def build_tci(sat):
    """
    returned tci is in bgr format
    3558 is max saturation for TCI in L1C product. L2C max saturation of 2000 oversaturates this dataset.
    https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-2-msi/definitions
    """
    sat = np.clip(sat[:, [0,1,2], ...], 0, 3558)
    sat = sat.astype(np.float32) / 3558
    sat = (sat * 255).astype(np.uint8)
    return sat


img2centroid = read_json(img2centroid_path)
img_paths = list(raw_sen_path.rglob("*data.npy"))
print(f"Total images: {len(img_paths)}")

# TODO: check cloud cover
def calc_highres_bounds(img2centroid, superarea, raw_aerial_path):
    aerial_path = raw_aerial_path/superarea.replace("-", "/")
    aerial_images = aerial_path.glob("img/*.tif")
    img_centroids = np.array([img2centroid[im.name] for im in aerial_images])
    (miny_c, minx_c), (maxy_c, maxx_c) = img_centroids.min(axis=0), img_centroids.max(axis=0)
    return miny_c, minx_c, maxy_c, maxx_c


for p in tqdm(img_paths):
    superarea = str(p.relative_to(raw_sen_path).parent.parent).replace("/", "-")
    superarea_dir = sen_path/superarea
    superarea_dir.mkdir(exist_ok=True)

    miny, minx, maxy, maxx = calc_highres_bounds(img2centroid, superarea, raw_aerial_path)

    sat = np.load(p)
    tci = build_tci(sat)
    tci = tci[:, :, miny:maxy, minx:maxx]

    for i, tci_at_time in enumerate(tci):
        write_image(superarea_dir/f"{i}.jpg", tci_at_time.transpose(1,2,0), rgb=False)
