import os

class CustomDocsService:
    @staticmethod
    def read_html_custom_docs(file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        with open(file_path, 'r') as file:
            content = file.read()
        
        return content