import json
from langchain.schema import Document

def load_json_as_documents(file_path, metadata_source):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return [
        Document(
            page_content=json.dumps(entry),
            metadata={"source": metadata_source}
        ) for entry in data
    ]