from db.models import *
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///db.db')
Session = sessionmaker(bind=engine)
session = Session()

john = User('John', 'Smith')
session.add(john)

task1 = Task('Take out trash')
session.add(task1)

join1 = JoinUserTask(john, task1)
session.add(join1)

session.commit()



