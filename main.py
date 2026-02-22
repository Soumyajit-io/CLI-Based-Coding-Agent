from agent import create_agent
from langchain_core.messages import HumanMessage,AIMessage

agent = create_agent()

history =[]
def main():
   print("====Welcome to AI Coding Assistant====")
   while True : 
      user_input = input("🧑 You: ")

      if user_input.lower() in ["exit", "quit"]:
            print("Goodbye! Developed by SoumyajiT")
            break
      
      # store
      history.append(HumanMessage(user_input))
      
      # llm calling
      response = agent.invoke({'input':history})

      # print
      print(f"🤖: {response['output']}")

      # store
      history.append(AIMessage(response['output']))

if __name__ == '__main__':
   main()