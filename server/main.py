import os
from typing import Annotated
from dotenv import load_dotenv
from fastapi import Depends, FastAPI
from sqlmodel import Session, create_engine
from posts import router
from database import get_db
import models

load_dotenv()

postgres_uri = os.getenv("POSTGRES_URI")

engine = create_engine(postgres_uri)

models.Base.metadata.create_all(bind=engine)

SessionDep = Annotated[Session, Depends(get_db)]

app = FastAPI()
app.include_router(router)