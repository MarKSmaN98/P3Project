from models import *
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///db.db')
Session = sessionmaker(bind=engine)
session = Session()

john = User(first_name='John', last_name='Smith')
session.add(john)

task1 = Task(task='Take out trash')
session.add(task1)

join1 = JoinUserTask(user=john, task=task1)
session.add(join1)

session.commit()