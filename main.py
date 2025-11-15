from langchain_community.tools import ShellTool
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from langchain_core.tools import tool
from dotenv import load_dotenv
from langchain_core.prompts import load_prompt
from Tools.html_opener import  open_in_browser
from Tools.basic import write_content,create_file,create_folder,read_file

from langchain.prompts import PromptTemplate
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI


ques = input("🤖 Enter what to create : ")
prompt= load_prompt('prompt.json')
 


llm2 = ChatOpenAI(model="gpt-4o-mini")

agent = create_react_agent(
   llm = llm2,
   tools=[create_file,
          write_content,
          read_file,
          create_folder,
          open_in_browser],
   prompt=prompt
)
agent_executer = AgentExecutor(
   agent = agent,
   tools=[create_file,
          write_content,
          read_file,
          create_folder,
          open_in_browser],
   verbose= True,
   handle_parsing_errors=True
)
response = agent_executer.invoke({'input':ques})
print(response['output'])
