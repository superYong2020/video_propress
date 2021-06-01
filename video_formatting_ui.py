# -*- coding: utf-8 -*-
# @Time    : 2021/6/1 15:37 
# @Author  : Yong Cao
# @Email   : yongcao@fuzhi.ai
# Author:Azrael
import win_unicode_console
win_unicode_console.enable()
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QLabel,
                             QApplication, QFileDialog)
from moviepy.video.io.VideoFileClip import VideoFileClip


class login(QWidget):
    def __init__(self):
        super(login, self).__init__()
        self.initUI()

    def initUI(self):
        # 源文件选择按钮和选择编辑框
        self.source_btn = QPushButton('source', self)
        self.source_btn.move(30, 30)
        self.source_btn.resize(60, 30)
        self.source_btn.clicked.connect(self.select_source)
        self.source_le = QLineEdit(self)
        self.source_le.move(120, 30)
        self.source_le.resize(250, 30)

        # 存储文件选择按钮和选择编辑框
        self.target_btn = QPushButton('target', self)
        self.target_btn.move(30, 90)
        self.target_btn.resize(60, 30)
        self.target_btn.clicked.connect(self.select_target)
        self.target_le = QLineEdit(self)
        self.target_le.move(120, 90)
        self.target_le.resize(250, 30)

        # 截切开始时间输入框和提示
        self.startLabel = QLabel(self)
        self.startLabel.move(30, 150)
        self.startLabel.resize(60, 30)
        self.startLabel.setText("stat_time")
        self.start_le = QLineEdit(self)
        self.start_le.move(120, 150)
        self.start_le.resize(50, 30)

        # 截切结束时间输入框和提示
        self.stopLabel = QLabel(self)
        self.stopLabel.move(230, 150)
        self.stopLabel.resize(60, 30)
        self.stopLabel.setText("stop_time")
        self.stop_le = QLineEdit(self)
        self.stop_le.move(320, 150)
        self.stop_le.resize(50, 30)

        # 保存按钮，调取数据增加函数等
        self.save_btn = QPushButton('save', self)
        self.save_btn.move(30, 210)
        self.save_btn.resize(140, 30)
        self.save_btn.clicked.connect(self.addNum)

        # 退出按钮，点击按钮退出整个程序
        self.cancle_btn = QPushButton('cancle', self)
        self.cancle_btn.move(230, 210)
        self.cancle_btn.resize(140, 30)
        self.cancle_btn.clicked.connect(QCoreApplication.quit)

        # 执行成功返回值显示位置设置
        self.result_le = QLabel(self)
        self.result_le.move(30, 270)
        self.result_le.resize(340, 30)

        # 技术支持框
        self.sourceLabel = QLabel(self)
        self.sourceLabel.move(30, 360)
        self.sourceLabel.resize(340, 30)
        self.sourceLabel.setText("Technical support:Azrael ")
        self.sourceLabel.setStyleSheet("color:blue;font-size:18px")
        self.sourceLabel.setAlignment(Qt.AlignCenter)

        # 整体界面设置
        self.setGeometry(400, 400, 400, 400)
        self.setWindowTitle('video binding')  # 设置界面标题名
        self.show()

    # 打开的视频文件名称
    def select_source(self):
        target, fileType = QFileDialog.getOpenFileName(self, "select the source file", "C:/")
        self.source_le.setText(str(target))

    # 保存的视频文件名称，要写上后缀名
    def select_target(self):
        target, fileType = QFileDialog.getSaveFileName(self, "select the save file", "C:/")
        self.target_le.setText(str(target))

    def addNum(self):
        source = self.source_le.text().strip()  # 获取需要剪切的文件
        target = self.target_le.text().strip()  # 获取剪切后视频保存的文件
        start_time = self.start_le.text().strip()  # 获取开始剪切时间
        stop_time = self.stop_le.text().strip()  # 获取剪切的结束时间
        video = VideoFileClip(source)  # 视频文件加载
        video = video.subclip(int(start_time), int(stop_time))  # 执行剪切操作
        print(int(start_time), int(stop_time))
        video.to_videofile(target, fps=20, remove_temp=True)  # 输出文件
        self.result_le.setText("ok!")  # 输出文件后界面返回OK
        self.result_le.setStyleSheet("color:red;font-size:40px")  # 设置OK颜色为红色，大小为四十像素
        self.result_le.setAlignment(Qt.AlignCenter)  # OK在指定框内居中


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = login()
    sys.exit(app.exec_())