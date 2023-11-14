import os
from pathlib import Path


_SET = os.environ.get("SET", "train")
assert _SET in ("train", "test")
_is_train = _SET == "train"

_FLAIR_PATH = Path("/home/topkech/work/sat_datasets/flair")
FLAIR_AERIAL_SZ = 512

img2centroid_path = _FLAIR_PATH/"flair-2_centroids_sp_to_patch.json"
superarea2img_path = _FLAIR_PATH/"superarea2img.json"

raw_aerial_path = _FLAIR_PATH/"flair_aerial_train" if _is_train else _FLAIR_PATH/"flair_2_aerial_test"
aerial_path = _FLAIR_PATH/f"flair_aerial_{_SET}_compressed"
aerial_path.mkdir(parents=True, exist_ok=True)

raw_sen_path = _FLAIR_PATH/"flair_sen_train" if _is_train else _FLAIR_PATH/"flair_2_sen_test"
sen_path = _FLAIR_PATH/f"flair_sen_{_SET}_compressed"
sen_path.mkdir(parents=True, exist_ok=True)
