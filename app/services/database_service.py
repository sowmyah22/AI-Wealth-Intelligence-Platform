# Create Database Service

from app.database.conection import SessionLocal
from app.database.models import PortfolioHolding

def save_portfolio_holdings(holdings:list):
    db=SessionLocal()

    for holding in holdings:
        db_holding=PortfolioHolding(
            stock=holding.stock,
            quantity=holding.quantity,
            buy_price=holding.buy_price
        )
        db.add(db_holding)
    db.commit()
    db.close()

# Add retrieval function
def get_saved_portfolios():
    db=SessionLocal()

    holdings=db.query(PortfolioHolding).all()  # select * from PortfolioHolding

    db.close()
    return holdings