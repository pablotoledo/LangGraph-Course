from typing import List, Sequence

from dotenv import load_dotenv
load_dotenv()

import os
import openai
from langchain_openai import AzureChatOpenAI

from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import END, MessageGraph

from chains import generate_chain, reflect_chain

REFLECT = "reflect"
GENERATE = "generate"


def generation_node(state: Sequence[BaseMessage]):
    return generate_chain.invoke({"messages": state})


def reflection_node(messages: Sequence[BaseMessage]) -> List[BaseMessage]:
    res = reflect_chain.invoke({"messages": messages})
    return [HumanMessage(content=res.content)]


builder = MessageGraph()
builder.add_node(GENERATE, generation_node)
builder.add_node(REFLECT, reflection_node)
builder.set_entry_point(GENERATE)


def should_continue(state: List[BaseMessage]):
    if len(state) > 6:
        return END
    return REFLECT


builder.add_conditional_edges(GENERATE, should_continue)
builder.add_edge(REFLECT, GENERATE)

graph = builder.compile()
print(graph.get_graph().draw_mermaid())
graph.get_graph().print_ascii()

if __name__ == "__main__":
    print("Hello LangGraph")
    inputs = HumanMessage(content="""Make this tweet better:"
                                    @LangChainAI
            — newly Tool Calling feature is seriously underrated.
            After a long wait, it's  here- making the implementation of agents across different models with function calling - super easy.
            Made a video covering their newest blog post
                                  """)
    
    # To see the steps of processing
    print("\nProcessing Steps:")
    for step in graph.stream(inputs):
        print("\n=== Step Output ===")
        print("Step type:", type(step))
        print("Step content:", step)
        print("Available keys:", step.keys())
        print("==================\n")

    # Get and print final response
    print("\nFinal Response:")
    response = graph.invoke(inputs)
    for message in response:
        if hasattr(message, 'content'):
            print(f"\nRole: {message.__class__.__name__}")
            print(f"Content: {message.content}")