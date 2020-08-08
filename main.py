from notion.client import NotionClient


# Obtain the `token_v2` value by inspecting your browser cookies on a logged-in session on Notion.so
client = NotionClient(token_v2=notion_token, monitor=True, start_monitoring=True, enable_caching=False)

cv = client.get_collection_view(
		"https://www.notion.so/54da70a076a343d0aed1aac5acde40e6?v=d12dde21691942a7b8e50c7e426c7825"
	)
# Replace this URL with the URL of the page you want to edit

def watch_completed_milestones():

    
    def my_callback(record, difference):
        print("The record's title is now:" + record.title)
        print("Here's what was changed:")
        print(difference)


    for block_row in cv.collection.get_rows():
        if "cognito" in block_row.title.lower():
            print("Adding callback for:", block_row.title)
            
        block_row.add_callback(my_callback)

watch_completed_milestones()

print("Ready and watching!")


# input()