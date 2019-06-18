import mysql.connector


# 连接服务器
conn = mysql.connector.connect(user='root', password='mysqlDeer2018', database='db_011')


# 1.add
def add(student_num, student_name):
    cursor = conn.cursor()
    sql = f"insert into student (student_num, student_name) values('{student_num}', '{student_name}')"
    cursor.execute(sql)
    cursor.close()
    conn.commit()
    return True

# 2.delete 
def delete(student_id):
    # 新建一个“光标”
    cursor = conn.cursor()
    # 写一个没有什么特别之处的sql
    sql = f"delete from student where student_id = {student_id}"
    # 执行这个sql
    cursor.execute(sql)
    # 关闭光标
    cursor.close()
    # 提交事物（刷新数据库）
    conn.commit()
    return True


# 3.change


# 4.search: 根据关键字从数据库模糊查找
def seach(keyword):
    # 1.新建一个“光标”
    cursor = conn.cursor()
    # 2.写一个没有什么特别之处的sql
    sql = f"select * from student where student_name like '{keyword}%'"
    # 3.执行这个sql
    cursor.execute(sql)
    # ans: (1, 'xxx', 'xxxxx')
    ans = cursor.fetchall()
    print('ans:', ans)
    # 4.关闭光标
    cursor.close()
    # 5.提交事物（刷新数据库）
    conn.commit()
    return ans
   

# 5.all lines 返回数据库中所有的行
def all_lines():
    cursor = conn.cursor()
    sql = 'select * from student order by student_id desc'
    cursor.execute(sql)
    ans = cursor.fetchall()
    cursor.close()
    conn.commit()
    return ans


