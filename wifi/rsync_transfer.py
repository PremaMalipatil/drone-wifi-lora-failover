import os
from config.settings import RSYNC_SOURCE, RSYNC_DEST

def start_rsync():
    print("Starting rsync transfer...")
    os.system(
        f"rsync -avz --partial {RSYNC_SOURCE} {RSYNC_DEST}"
    )
