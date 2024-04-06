import os
from dotenv import load_dotenv

load_dotenv()

print(os.environ["MY_NAME"])
print(os.environ["MY_SURNAME"])
