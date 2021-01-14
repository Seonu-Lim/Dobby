import os
from _stamper import *
from tqdm import tqdm
import argparse
import time


def stamp_all_files(origin_path, destination_path):
    filelist = os.listdir(origin_path)
    for f in tqdm(filelist):
        stamp_document(origin_path, f, destination_path)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", type=str)
    args = parser.parse_args()
    destination_path = os.path.join(args.origin_path,'output')
    if not os.path.exists(destination_path) :
        os.makedirs(destination_path)
    stamp_all_files(args.origin_path, destination_path)

if __name__ == "__main__":
    start_time = time.time()
    main()
    print(f'Execution Time : {time.time()-start_time} seconds.')
