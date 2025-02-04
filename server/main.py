import os
from typing import Annotated
from dotenv import load_dotenv
from fastapi import Depends, FastAPI
from sqlmodel import Session, create_engine
from fastapi_socketio import SocketManager
from auth import auth_router
from bid import bid_router
from products import product_router
from database import get_db
import models

load_dotenv()

postgres_uri = os.getenv("POSTGRES_URI")

engine = create_engine(postgres_uri)

models.Base.metadata.create_all(bind=engine)

SessionDep = Annotated[Session, Depends(get_db)]

app = FastAPI()
socket_manager = SocketManager(app=app)
app.include_router(auth_router)
app.include_router(bid_router)
app.include_router(product_router)