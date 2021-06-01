# -*- coding: utf-8 -*-
# @Time    : 2021/6/1 15:54 
# @Author  : Yong Cao
# @Email   : yongcao@fuzhi.ai
import cv2
from tqdm import tqdm
import argparse
import datetime


def main(filename, save_path):
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    cap = cv2.VideoCapture(filename)
    print("原视频帧率： ", cap.get(5))
    print("总帧数： ", cap.get(7))
    print("视频时长：", str(datetime.timedelta(seconds=int(cap.get(7)/cap.get(5)))))
    print("视频宽度：{}， 高度： {}".format(int(cap.get(3)), int(cap.get(4))))
    success = True
    videoWriter = cv2.VideoWriter(save_path, fourcc, int(cap.get(5)), (int(cap.get(3)), int(cap.get(4))))
    for i in tqdm(range(int(cap.get(7)))):
        success, frame = cap.read()
        videoWriter.write(frame)
    videoWriter.release()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='wmv to mp4 converter')
    parser.add_argument('--src_path', type=str, help='source file name')
    parser.add_argument('--dst_path', type=str, help='destination file name')
    args = parser.parse_args()

    src_path = args.src_path
    dst_path = args.dst_path
    main(src_path, dst_path)