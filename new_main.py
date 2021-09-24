import os
from dotenv import load_dotenv
from notion.client import NotionClient

load_dotenv()

# Obtain the `token_v2` value by inspecting your browser cookies on a logged-in (non-guest) session on Notion.so
token = os.getenv('token_v2')
client = NotionClient(token_v2=token)

# Replace this URL with the URL of the page you want to edit
url = "https://www.notion.so/mitsuk/3-833e0339940e47bd8cac44f650d8332e"
page = client.get_block(url).id

client.download_block(block_id=page, export_type='pdf', output_file_name='Мицук_А-05-18')

