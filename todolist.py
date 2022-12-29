import pymysql
from pymysql import OperationalError
import time

connection = pymysql.connect(
    host='localhost',  # 数据库地址
    user='root',  # 数据库用户名
    password='12345678',  # 数据库密码
    db='todo',  # 数据库名称
    # charset = 'utf8 -- UTF-8 Unicode'
)


cursor = connection.cursor()
#没有表格，就创建表格
try:
    cursor.execute("create table todo(id int ,student varchar(20))ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1")
except OperationalError:
    pass

sql = 'select student from todo'
#execute执行操作

cursor.execute(sql)
results = cursor.fetchall()
print(type(results),cursor.rowcount)
print(results)


from flask import Flask,render_template
todolist = []
for result in results:
    result=str(result)[2:-3]
    todolist.append(str(result))

app = Flask(__name__)
print(todolist)


@app.route('/')
def home():
    return render_template('todolist.html')
@app.route('/api/todolist/checkItems',methods=['POST'])
def checkTodo():
    return str(todolist),200
@app.route('/api/todolist/delItem/<int:item>',methods=['POST'])
def deleteTodo(item):
    print(item)
    lines=todolist[item]
    lines=lines.splitlines()
    todolist.pop(item)
    print(lines[0])
    del_sql = 'delete from todo where student = %s'
    cursor.execute(del_sql, lines[0])
    connection.commit()

    return ''
@app.route('/api/todolist/addItem/<content>',methods=['POST'])
def addTodo(content):
    todolist.append(content)
    id= len(todolist)
    print(id)
    add_sql = 'insert into todo(id,student) values (%s,%s)'
    data=[(id,content)]
    cursor.execute(add_sql, data)
    # 涉及写操作要提交
    connection.commit()
    return ''

app.run()





