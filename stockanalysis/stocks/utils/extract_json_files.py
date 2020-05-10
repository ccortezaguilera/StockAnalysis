from typing import Dict
import aiofiles
import datetime
import json


async def extract_json_file(filename: str):
    async with aiofiles.open(filename, "r") as json_file:
        content = await json_file.read()
    return json.loads(content)


def generate_response(data: Dict, max_size: int):
    for i, k in enumerate(data.keys()):
        if i > max_size:
            break
        timestamp = datetime.datetime.fromisoformat(k.replace("Z", "+00:00")).strftime(
            "%Y-%m-%d"
        )
        yield (timestamp, data[k])
