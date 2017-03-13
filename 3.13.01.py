# SQLAlchemy

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'bilibili_user_info'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fans = Column(Integer)
    friend = Column(Integer)

    def __repr__(self):
        return "<User(name='%s', )> % (self.name)"


# 创建会话
engine = create_engine('mysql+mysqlconnector://python:Python@2017@localhost/testDB')
Session = sessionmaker(bind=engine)
session = Session()

# 查询记录
for instance in session.query(User).order_by(User.id):
    print(instance.name, '\t\t', instance.fans, '\t', instance.friend)

# 添加记录
ed_user = User(name='ed', fans=20, friend=999)
session.add(ed_user)
session.commit()

# 查询记录
jack = session.query(User).filter_by(name='ed').one()
print(jack.name, jack.fans, jack.friend)

# 查询计数
jack = session.query(User).filter_by(name='ed').count()
print(jack)

# 删除记录
jack = session.query(User).filter_by(name='ed').first()
session.delete(jack)
session.commit()

# 关闭会话
session.close()
