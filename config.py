import os

from dotenv import load_dotenv
load_dotenv()
token=str(os.getenv('token'))
ip=os.getenv('ip')