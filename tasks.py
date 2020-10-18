import json
import os
import multiprocessing
import time
from pathlib import Path
from mongo import MongoAPI

PROCESSES = multiprocessing.cpu_count() - 1

BASE_DIR = Path(__file__).resolve(strict=True).parent
DATA_DIR = Path(BASE_DIR).joinpath("data")


db = MongoAPI({"database": "CurlDB", "collection": "ticker"})


def create_ticker_task(records):
    for record in records:
        try:
            db.write(record)
        except:
            print("there was a problem with line")
    print('{} ticker created with success!'.format(len(records)))


def read_file(filename):
    with open(Path(DATA_DIR).joinpath(filename), "r", encoding="utf8") as f:
        all_lines = json.load(f)
        create_ticker_task(all_lines.values())

    proc = os.getpid()
    print(f"Processed {filename} with process id: {proc}")


def run():
    print(f"Running with {PROCESSES} processes!")

    filename_arr = os.listdir(Path(DATA_DIR))
    start = time.time()
    with multiprocessing.Pool(PROCESSES) as p:
        p.map_async(
            read_file,
            filename_arr,
        )
        # clean up
        p.close()
        p.join()

    print(f"Time taken = {time.time() - start:.10f}")


if __name__ == '__main__':
    run()