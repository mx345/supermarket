import pymysql
import socket,sys

srkl_cnt=0

def insert_db():
    print("1.添加新个商品")
    print("2.添加同一商品")
    iu=input(">>")
    if iu=="1":
        uname=input("请输入你的产品名：")
        jinjia=input("请输入你的产品进价格：")
        shoujia=input("请输入你的产品售价格：")
        rkl=input("请输入你的数量：")
        db = pymysql.connect("localhost","mx12","123456","mydb")
        cursor = db.cursor()
        sql = "insert into commodity (uname,jinjia,shoujia,rkl) values ('%s','%s','%s','%s')" % \
            (uname,jinjia,shoujia,rkl)
        cursor.execute(sql)
        db.commit()
        db.close()
    if iu=="2":
        insert_db1()

def insert_db1():
    db = pymysql.connect("localhost","mx12","123456","mydb")
    cursor = db.cursor()
    sname=input("请输入你你要查询的产品：")
    srkl=int(input("请输入你要入库的个数："))
    sql = "update commodity set rkl=rkl+{} \
                where uname='{}' ".format(srkl,sname)
    cursor.execute(sql)
    db.commit()
    db.close()
# 盘点库存
def select_knc():
   
    db = pymysql.connect("localhost","mx12","123456","mydb")
    sname=input("请输入你你要查询的产品(输入*是查看全部)：")
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()
    
    # SQL 查询语句
    if sname == "*":
        sql = "SELECT * FROM commodity"
    else:
        sql = "SELECT * FROM commodity \
            where uname='%s'"%sname         
    try:
    # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            id1 = row[0]
            name1 = row[1]
            jinjia = row[2]
            shoujia = row[3]
            rkl = row[4]
            # 打印结果
            print ("id1=%s,name1=%s,jinjia=%s,shoujia=%s,rkl=%s" % \
                    (id1, name1, jinjia, shoujia, rkl ))
    except:
        print ("Error: unable to fetch data")
        
        # 关闭数据库连接
        db.close()

def select_knc2():
   
    db = pymysql.connect("localhost","mx12","123456","mydb")
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()
    
    # SQL 查询语句
   
    sql = "SELECT * FROM commodity"
      
    try:
    # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            id1 = row[0]
            name1 = row[1]
            jinjia = row[2]
            shoujia = row[3]
            rkl = row[4]
            # 打印结果
            print ("id1=%s,name1=%s,jinjia=%s,shoujia=%s,rkl=%s" % \
                    (id1, name1, jinjia, shoujia, rkl ))
    except:
        print ("Error: unable to fetch data")
        # 关闭数据库连接
        db.close()


def update_xiaosh():
    global srkl_cnt
    
    # select_knc2()
    while True:
        print("1.商品出售")
        print("2.查看销售额")
        print("0.退出")
        ip = input(">>")
        # 使用cursor()方法获取操作游标 
        db = pymysql.connect("localhost","mx12","123456","mydb")
        cursor = db.cursor()
        if ip=="1":
            sname=input("请输入你你要查询的产品：")
            srkl=int(input("请输入你要出售的个数："))
            sql = "update commodity set rkl=rkl-{} \
                where uname='{}' ".format(srkl,sname)
            cursor.execute(sql)
            srkl_cnt+=srkl 
            db.commit()
            select_knc2()   
            db.close()
        elif ip=="2":
           
            db = pymysql.connect("localhost","mx12","123456","mydb")
            cursor = db.cursor()
            print(srkl_cnt)
            sq1= "select AVG(shoujia-jinjia) from commodity where shoujia-jinjia" 
            cursor.execute(sq1)
            data = cursor.fetchone()
            dat=int(data[0])*srkl_cnt
            print(" 销售额为 :%s" % dat)
            db.close()
        else:
            break

# update_xiaosh()
# insert_db()
# 打他=1
# print(打他)