# -*- coding: utf-8 -*-
# @Time    : 2021/6/1 15:37 
# @Author  : Yong Cao
# @Email   : yongcao@fuzhi.ai
import argparse
from moviepy.video.io.VideoFileClip import VideoFileClip


class VideoCutter:
    def __init__(self, source_path, save_path, start_time, stop_time):
        self.source_path = source_path
        self.save_path = save_path
        self.start_time = start_time
        self.stop_time = stop_time
        self.format_time()

    # 剪辑视频
    def cut_video(self):
        source = self.source_path  # 获取需要剪切的文件
        target = self.save_path  # 获取剪切后视频保存的文件
        start_time = self.start_time  # 获取开始剪切时间
        stop_time = self.stop_time  # 获取剪切的结束时间
        video = VideoFileClip(source)  # 视频文件加载
        video = video.subclip(int(start_time), int(stop_time))  # 执行剪切操作
        video.to_videofile(target, fps=20, remove_temp=True)  # 输出文件

    # 时间标准化
    def format_time(self):
        h, m, s = self.start_time.strip().split(":")
        self.start_time = int(h) * 3600 + int(m) * 60 + int(s)
        h, m, s = self.stop_time.strip().split(":")
        self.stop_time = int(h) * 3600 + int(m) * 60 + int(s)
        print(self.start_time)
        print(self.stop_time)


if __name__ == "__main__":
    # 传入四个参数
    parser = argparse.ArgumentParser(description='wmv to mp4 converter')
    parser.add_argument('--src_path', type=str, help='source file name')
    parser.add_argument('--dst_path', type=str, help='destination file name')
    parser.add_argument('--start_time', type=str, help='standard time format h:m:s, eg.00:01:15')
    parser.add_argument('--end_time', type=str, help='standard time format h:m:s, eg.00:10:15')
    args = parser.parse_args()

    src_path = args.src_path
    dst_path = args.dst_path
    begin_time = args.start_time
    end_time = args.end_time

    video_cutter = VideoCutter(src_path, dst_path, begin_time, end_time)
    video_cutter.cut_video()