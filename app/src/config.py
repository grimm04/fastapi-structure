from typing import List

from starlette.config import Config

from starlette.datastructures import CommaSeparatedStrings, Secret
from pydantic_settings import BaseSettings, SettingsConfigDict

###
# Properties configurations 
###

class Settings(BaseSettings):
    ENV_STATE:str
    DB_URL: str
    SECRET_KEY: str
    DEBUG: bool = False
    #prefix
    API_PREFIX:str  
    ROUTE_PREFIX_V1:str
    #jwt
    JWT_TOKEN_PREFIX:str 
    ALGORITHM:str   
    
    
    model_config = SettingsConfigDict(env_file=('.env.prod', '.env'),extra='ignore',from_attributes=True)


settings = Settings()

API_PREFIX = settings.API_PREFIX

JWT_TOKEN_PREFIX = settings.JWT_TOKEN_PREFIX 

config = Config(".env")

ROUTE_PREFIX_V1 = settings.ROUTE_PREFIX_V1 

ALLOWED_HOSTS: List[str] = config(
    "ALLOWED_HOSTS",
    cast=CommaSeparatedStrings,
    default="",
) 
 
# print(settings.model_dump())