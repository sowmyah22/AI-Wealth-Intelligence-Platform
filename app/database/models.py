from sqlalchemy import Column,Integer,Float,String
from app.database.conection import Base

class PortfolioHolding(Base):
    __tablename__="portfolio_holdings"
    id=Column(Integer,primary_key=True,index=True)
    stock=Column(String)
    quantity=Column(Integer)
    buy_price=Column(Float)


#CREATE TABLE portfolio_holdings (id INTEGER PRIMARY KEY,stock TEXT,quantity INTEGER, buy_price FLOAT)