#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys,pymysql,re
from user_reg_login import reg_main, login_main, user_center,send_email_code

def check_password1(password):
    '''
    函数功能：校验用户密码是否合法
    函数参数：
    password 待校验的密码
    返回值：校验通过返回0，校验错误返回非零（密码太长或太短返回1，密码安全强度太低返回2）
    '''
    if  re.match(r"^[0-9a-zA-Z]\w{6,18}", password):
        return 0
    elif  re.match(r"^[0-9]|[a-zA-Z]{6,15}$", password):
        return 2
    elif  re.match(r"^[0-9a-zA-Z]\w{3,20}$", password):
        return 1

def updata_passwd():
    while True:
        email = input("请输入邮箱：")
        if re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$',email):  
            #if re.match(r'[0-9a-zA-Z_]{0,19}@163.com',text):  
            print('你的邮箱输入正确') 
            break 
        else:  
            print('请重新输入的你的邮箱')
    email_code1=send_email_code()
    if email_code1:
        print("邮箱验证码已发送！")
    else:
        print("邮箱验证码发送失败，请检查网络连接！")
        sys.exit(1)
    while True:
        email1=input("请输入你收到的邮箱验证码：")
        if email_code1!=email1:
            print('验证码输入错误')
        else:
            break
    db = pymysql.connect("localhost","mx12","123456","mydb")
    sname=input("请输入你的用户名()：")
    while True:
        passwd=input("请输入你的新密码()：")
        # 使用cursor()方法获取操作游标 
        cursor = db.cursor()
        reg=check_password1(passwd)
        if reg==1:
            print("密码太长或者太短,请重新输入")
        elif reg==2:
            print("密码太简单,请重新输入")
        else:
            print("校验成功")
            break       
    sql = "update test set passwd=password('%s')\
         where uname='%s'"% (passwd,sname)
    cursor.execute(sql)
    db.commit()
    print("你设置的密码为%s"%passwd)
   
    db.close()
def main():
    
    while True:
        print("操作提示：")
        print("1：登录")
        print("2：注册")
        print("3:修改登录密码:")
        print("0：退出")
        op = input("\n>>>：")

        if op == "0":
            print("感谢你的使用，下次再见！")
            sys.exit(2)
        elif op == "1":
            user_name = login_main()
            if user_name:
                # print("登录成功！")
                user_center(user_name)
            else:
                print("密码错误，登录失败！")
        elif op == "2":

            reg_main()
        elif op=="3":
            updata_passwd()
        else:
            print("输入错误，请重新输入！")

if __name__ == "__main__":
    main()


    










