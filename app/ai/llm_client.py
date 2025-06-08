from lmstudio import lms
from app.core.config import settings

client = lms.configure_default_client(settings.LMSTUDIO_URL)
