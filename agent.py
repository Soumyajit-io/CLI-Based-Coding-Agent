from langchain.agents import create_react_agent, AgentExecutor
from dotenv import load_dotenv
from langchain_core.prompts import load_prompt
from Tools.html_opener import  open_in_browser
from Tools.basic import write_content,create_file,create_folder,read_file
from langchain_openai import ChatOpenAI

load_dotenv()
def create_agent():
   prompt= load_prompt('prompt.json')
   llm2 = ChatOpenAI(model="gpt-4o-mini",temperature=0)

   agent = create_react_agent(
      llm = llm2,
      tools=[create_file,
            write_content,
            read_file,
            create_folder,
            open_in_browser],
      prompt=prompt
   )
   agent_executor = AgentExecutor(
      agent = agent,
      tools=[create_file,
            write_content,
            read_file,
            create_folder,
            open_in_browser],
      # verbose= True,# if you want to see explanation
      handle_parsing_errors=True
   )
   return agent_executor

