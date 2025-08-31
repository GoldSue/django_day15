



import pymysql

def test_mysql_connection():
    try:
        # 修改为你的配置
        conn = pymysql.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="Gold7789@",
            database="day15",  # 可以先写一个已存在的库，比如mysql
            charset="utf8mb4"
        )
        print("✅ MySQL连接成功！")
        conn.close()
    except Exception as e:
        print("❌ MySQL连接失败：", e)

if __name__ == "__main__":
    test_mysql_connection()



