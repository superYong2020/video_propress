# 安装依赖
```shell
pip install -r requirement.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

# 视频剪切
* 参考 [https://www.cnblogs.com/wybert/p/12400907.html](https://www.cnblogs.com/wybert/p/12400907.html)
### GUI
```python 
python video_formatting_ui.py
```
### Terminal
```python 
python video_formatting.py --src_path /mp4/path --dst_path /save/path/ --start_time 00:00:00 --end_time 00:12:02
```

# 视频格式转换
### Terminal
```python
python wmv2mp4.py --src_path /data/path --dst_path /save/path
```

* testcase    
filename = r'C:\Users\epic_cy\Desktop/temp.wmv'    
save_path =  r'C:\Users\epic_cy\Desktop/temp.mp4'     
  

# TODO
* 视频压缩
* 视频合并
* 其他格式(avi、mov)转MP4