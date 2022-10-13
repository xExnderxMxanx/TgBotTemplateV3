from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime

from dispatcher import model

class User(model):
    __tablename__ = 'Users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column("user_id", Integer, unique=True, nullable=False)
    user_name = Column("user_name", String(200), nullable=False)
    date_reg = Column("Date_registration", DateTime, default=datetime.now())
    
    def __str__(self) -> str:
        return f"User {self.user_id}"

    def __repr__(self):
        return f'<User {self.user_id}>'
