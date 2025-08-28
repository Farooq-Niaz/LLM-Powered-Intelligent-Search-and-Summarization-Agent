from langchain.agents import Tool, initialize_agent, AgentType
from langchain_community.llms import GPT4All
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_core.callbacks.base import BaseCallbackManager
from langchain_core.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_google_community import GoogleSearchAPIWrapper  # Updated wrapper
from dotenv import load_dotenv

# Load environment variables for Google API
load_dotenv()

# Initialize the GPT4All LLM with streaming
callback_manager = BaseCallbackManager([StreamingStdOutCallbackHandler()])
llm = GPT4All(
    model="E:\\LLM\\models\\Meta-Llama-3-8B-Instruct.Q4_0.gguf",
    callbacks=callback_manager,
    verbose=True
)

# Create a prompt template for the Summarizer tool

template = """Question: {query}
Answer: Let's answer in three sentences."""

prompt = PromptTemplate(template=template, input_variables=["query"])


summarize_chain = LLMChain(llm=llm, prompt=prompt)

# Define tools with proper input handling
search = GoogleSearchAPIWrapper()

tools = [
    Tool(
        name="Search",
        func=search.run,
        description="useful for finding information about recent events"
    ),
    Tool(
        name='Summarizer',
        func=lambda text: summarize_chain.invoke({"query": text}),
        description='useful for summarizing texts'
    )
]

# Initialize the agent with limited iterations to prevent loops
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    max_iterations=3  # prevents infinite thought/action cycles
)

# Ask a question
question = "What's the latest news about the Mars rover?"
response = agent.invoke({"input": question})

print("\nFinal Answer:")
print(response['output'])
