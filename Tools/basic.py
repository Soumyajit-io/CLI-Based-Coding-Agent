from langchain_core.tools import tool
import os
import os
import json 

from pydantic import BaseModel, Field
import time


class WriteContentArgs(BaseModel):
    path: str = Field(description="The full file path (e.g., 'TODO/index.html')")
    content: str = Field(description="The text content to write into the file")

@tool
def create_file(path: str) -> str:
    """
    Creates an empty file at the specified path.

    - Does not creates parent folders if they don't exist.
    - Does NOT overwrite existing files.
    - Returns a clear success or error message.

    Args:
        path (str): The full file path (e.g., "TODO/index.html")

    Returns:
        str: Message indicating success or the type of error.
    """
    try:
        path = path.strip()
        
        # Check if file already exists
        if os.path.exists(path):
            return f"File already exists: {path}"

        # Create empty file (x mode avoids overwrite)
        with open(path, "x", encoding="utf-8") as f:
            pass

        return f"Empty file created successfully: {path}"

    except FileExistsError:
        return f"File already exists: {path}"
    except Exception as e:
        return f"Error creating file '{path}': {str(e)}"


@tool
def write_content(input_json: str) -> str: 
    """
    Writes content to a file.
    The input MUST be a single JSON string with 'path' and 'content' keys.
    Example: '{"path": "TODO/index.html", "content": "<html>..."}'
    """
    try:
        # 1. Parse the single JSON string that the agent provides
        data = json.loads(input_json)
        
        # 2. Validate the data using the Pydantic model
        validated_args = WriteContentArgs(**data)
        
        # 3. Use the validated arguments
        with open(validated_args.path, 'w', encoding="utf-8") as f:
            for i in validated_args.content:
                f.write(i)
                f.flush()
                time.sleep(0.02)
        
        return f"File successfully written: {validated_args.path}"
    
    except json.JSONDecodeError:
        return f"Error: Invalid JSON format. Expected a JSON string. Received: {input_json}"
    except Exception as e:
       
        return f"Error processing write_content: {str(e)}"
   

@tool
def create_folder (path:str)-> str:
   """Create a empty folder

   Args:
       path (str): Path of the folder

   Returns:
       str: Creates a folder (and intermediate directories if needed).
    Returns a success message or error.
   """
   try:
       path = path.strip()
       os.makedirs(path,exist_ok=True)
       return f" Folder created or already exists: {path}"
   except Exception as e:
        return f" Error creating folder '{path}': {str(e)}"

@tool
def read_file (path:str) ->str:
   """Reads the file content

   Args:
       path (str): path of the file

   Returns:
       str: Reads the content of the file.
   """
   try:   
      with open(path,'r',encoding="utf-8") as f :   
         return f.read()
         
   except Exception as e :
         return f"Error: {str(e)}"