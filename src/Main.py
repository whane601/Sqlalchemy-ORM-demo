from src.common import postgresql
from src.common.postgresql import Users, Transcripts

# 簡單寫入DB
users = Users()
users.name = "Jack"
users.phone = "0975xxxxxx"

postgresql.insertDB(users)

transcripts = Transcripts()
transcripts.user_id = 1
transcripts.score = 99

postgresql.insertDB(transcripts)

# 簡單查詢
session = postgresql.Session()
people = session.query(Users).filter(Users.name == "Jack").order_by(Users.id)

for person in people:
    print(person.name)

for i in session.query(Users).all():
    print(i.name, i.phone)

# inner join查詢
for i in session.query(Users.name, Transcripts.score).join(Transcripts, Users.id == Transcripts.user_id):
    print(i.name, i.score)

# 資訊修改
session = postgresql.Session()
query_resault = session.query(Users).filter(Users.name == "Jack").first()
query_resault.name = "JackKuo"
session.commit()

# 資訊刪除
session = postgresql.Session()
query_resault = session.query(Transcripts).filter(Transcripts.user_id == 1).first()
session.delete(query_resault)
session.commit()