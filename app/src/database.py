from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os 

from .config import settings
###
# Database Configuration
### 

engine = create_engine(
    os.getenv("DB_URL", settings.DB_URL)
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()