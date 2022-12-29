使用flask和sql进行运行

安装运行必要的requirements
然后就可以运行了

```
pip3 install requirements.txt
python3 todolist.py
```



```
connection = pymysql.connect(
    host='localhost',  # 数据库地址
    user='root',  # 数据库用户名
    password='12345678',  # 数据库密码
    db='todo',  # 数据库名称
    # charset = 'utf8 -- UTF-8 Unicode'
)
```
