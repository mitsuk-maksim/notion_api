from notion.client import NotionClient

# Obtain the `token_v2` value by inspecting your browser cookies on a logged-in (non-guest) session on Notion.so
token = "0c885a798c2d71107add6e3ddb7c0464da1b91ced006c5ec1185bec99bf862953c2400f20d7aa3cc51b85781f78a352a13bdd4ad6d0f02b3080c9bc99ef103e10152c6effd3d91e25270d7b899d2"
client = NotionClient(token_v2=token)

# Replace this URL with the URL of the page you want to edit
url = "https://www.notion.so/mitsuk/3-833e0339940e47bd8cac44f650d8332e"
page = client.get_block(url).id

client.download_block(block_id=page, export_type='pdf', output_file_name='Мицук_А-05-18')

