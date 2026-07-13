# FastAPI entry point for the application

from fastapi import FastAPI
from app.routes import router
from app.database.connection import engine
from app.database.models import Base

app=FastAPI(title="AI INVESTMENT ANALYST")

#creates database tables automatically
Base.metadata.create_all(bind=engine)  

#include routes
app.include_router(router)

