# .env ファイルをロードして環境変数へ反映
import os
from dotenv import load_dotenv
load_dotenv()

# 環境変数を参照
LINE_NOTIFY_TOKEN = os.environ.get("LINE_NOTIFY_TOKEN")
