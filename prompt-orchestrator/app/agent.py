import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

# Setup LLM
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# --- 1. PROMPT WRITER (Orchestrator) ---
writer_prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a High-Level AI Prompt Engineer.
    Your job is to take raw user instructions and turn them into a detailed, structured,
    system-level prompt for another AI assistant to execute.
    
    Structure your output as:
    1. Role: [Persona]
    2. Goal: [Goal]
    3. Constraints: [Constraints]
    4. Task: [Actionable steps]
    
    User Request: {input}
    """),
])

prompt_writer_chain = writer_prompt | llm | StrOutputParser()

# --- 2. ACTION AGENT (Executor) ---
# In a real scenario, this would use LangGraph to call tools.
action_agent_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an specialized assistant. Follow these instructions: {instructions}"),
    ("user", "{task}")
])

action_chain = action_agent_prompt | llm | StrOutputParser()

def run_orchestration(user_input):
    """Orchestrates prompt creation and execution."""
    # Phase 1: Convert to prompt
    structured_prompt = prompt_writer_chain.invoke({"input": user_input})
    
    # Phase 2: Execute with the new prompt
    final_output = action_chain.invoke({
        "instructions": structured_prompt,
        "task": user_input
    })
    
    return {
        "generated_prompt": structured_prompt,
        "final_action_output": final_output
    }
