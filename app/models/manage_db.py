from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from logging import getLogger
from dotenv import load_dotenv
import os


logger = getLogger('app_logger')

load_dotenv()

# Database setup
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class UserSignup(Base):
    __tablename__ = 'user_signup'

    id = Column(Integer, primary_key=True)
    email = Column(String(255), nullable=False)
    username = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    company_name = Column(String(255), nullable=False)
    user_role = Column(String(50), nullable=False, default="user")
    license_amount = Column(Integer, default=0)
    disabled = Column(Integer, default=1)
    create_date = Column(DateTime)
    update_date = Column(DateTime)

    groups = relationship("Group", back_populates="user")

    @classmethod
    def update_disabled_status(cls, user_id: int, disabled: bool):
        with SessionLocal() as session:
            user = session.query(cls).filter(cls.id == user_id).first()
            if user:
                user.disabled = disabled
                user.update_date = func.now()
                session.commit()
                return True
            return False

    @classmethod
    def update_license_amount(cls, user_id: int, license_amount: int):
        with SessionLocal() as session:
            user = session.query(cls).filter(cls.id == user_id).first()
            if user:
                user.license_amount = license_amount
                user.update_date = func.now()
                session.commit()
                return True
            return False

class Group(Base):
    __tablename__ = 'group_signup'

    group_name = Column(String(255), primary_key=True, nullable=False)
    user_signup_id = Column(Integer, ForeignKey('user_signup.id'), nullable=True)
    create_date = Column(DateTime, server_default=func.now(), nullable=True)
    update_date = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=True)

    user = relationship("UserSignup", back_populates="groups")
    
Base.metadata.create_all(bind=engine)