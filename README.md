# Sqlalchemy ORM demo
此demo以postgresql、mysql為範例

## 參考文獻
https://www.zlovezl.cn/articles/sqlalchemy-intro-for-django-guys/
https://docs.sqlalchemy.org/en/latest/orm/

## 操作說明
- 執行`pip install -r requirements.txt`安裝相關套件
- 至src/config/config.ini修改DB路徑
- 在src/common/postgresql.py or src/common/mysql.py定義你要的table格式
- 至src/Main.py對剛建立的table進行操作(查詢、新增、修改、刪除...等)