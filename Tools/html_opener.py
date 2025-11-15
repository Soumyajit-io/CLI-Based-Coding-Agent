from langchain_core.tools import tool
import subprocess, os, platform

@tool
def open_in_browser(path:str)-> str:
    """Opens an HTML file in the default web browser.

    Args:
        path (str): path of the file

    Returns:
        str: Open the file in web browser
    """
    if not os.path.exists(path):
        return "Error: File does not exist."
    try: 
        subprocess.run(['start' ,path],shell=True)
    except Exception as e :
        return f"Error Opening the file: {str(e)}"