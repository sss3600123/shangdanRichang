# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, Column, String, Sequence, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
	# 表名
	__tablename__ = 'user'

    # 表结构
	id = Column(Integer, primary_key=True)
	name = Column(String(45))
	password = Column(String(45))

	def __str__(self):
		return "<User(name='%s')>" % (self.name)


engine = create_engine('mysql+pymysql://root:root@localhost:3306/mytest')
DBSession = sessionmaker(bind=engine)
# print(engine)

# 创建session对象
session = DBSession()

# 创建新USER对象
new_user = User(name=u'John10', password=u'qweqwe11')

# 添加到session
session.add(new_user)

# 提交即保存到数据库
session.commit()

#关闭session
session.close()
