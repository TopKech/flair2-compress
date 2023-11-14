## FLAIR 2 compression for cross-domain matching

Download FLAIR #2 from https://ignf.github.io/FLAIR/  
Make sure you're downloading #2. Scroll to the bottom.  

Unzip into a dir, set the _FLAIR_PATH variable in settings.py to that dir.  

Run the following:
1. `SET="train" python compress_flair_aerial.py`
2. `SET="train" python compress_flair_sen.py`
3. `SET="test" python compress_flair_aerial.py`
4. `SET="test" python compress_flair_sen.py`
