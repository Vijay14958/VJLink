# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "27639102"))
API_HASH = os.environ.get("API_HASH", "35142c1407be6264e68fb6bec5dcabd9")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5804525901:AAEBbNOQEegVYW7DPqzJ0u4VyUnMlOCctBo")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("5606411877")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "VJLinkShortner")
DATABASE_URL = os.getenv("DATABASE_URL", "Monfo url") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "5606411877")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(Id Owned Id)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001716170358")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
