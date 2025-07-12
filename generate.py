import json
import os

with open("channels.json") as f:
    channels = json.load(f)

template = """#EXTM3U
#EXT-X-STREAM-INF:BANDWIDTH=3000000
https://playflix.icu/mahesh/Jiotv/index.php?id={channel_id}&e=.m3u8
"""

for name, channel_id in channels.items():
    content = template.format(channel_id=channel_id)
    with open(f"{name}.m3u8", "w") as f:
        f.write(content)
