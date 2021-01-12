import os
from _stamper import *
from tqdm import tqdm
import argparse


def stamp_all_files(origin_path, destination_path):
    filelist = os.listdir(origin_path)
    for f in tqdm(filelist):
        stamp_document(origin_path, f, destination_path)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--origin_path", type=str)
    parser.add_argument("--destination_path", type=str)
    args = parser.parse_args()
    stamp_all_files(args.origin_path, args.destination_path)


if __name__ == "__main__":
    main()
