import rasterio as rio
from rasterio.merge import merge
from rasterio.enums import Resampling
from tqdm import tqdm

from utils.io import write_image
from settings import raw_aerial_path, aerial_path, FLAIR_AERIAL_SZ


superarea_paths = list(raw_aerial_path.glob("*/*"))
print(f"Total superareas: {len(superarea_paths)}")


for sa_path in tqdm(superarea_paths):
    superarea = str(sa_path.relative_to(raw_aerial_path)).replace("/", "-")
    output_path = aerial_path / f"{superarea}.jpg"
    images = list(sa_path.glob("img/*.tif"))
    merged, _ = merge(images, indexes=(1, 2, 3), resampling=Resampling.lanczos)  # rio indexes start with 1 !!!
    merged = merged.transpose(1,2,0)
    # crop on edge tiles' centroids. It is the last known point to be (almost) pixel-to-pixel aligned between aerial and sen
    offset = FLAIR_AERIAL_SZ // 2
    merged = merged[offset:-offset, offset:-offset, :]
    write_image(output_path, merged)
