from google.adk.agents import Agent
from google.adk.agents import LlmAgent
from google.adk.agents import SequentialAgent

def poet_tool(poet: str) -> str:
    return ""

poet_agent = LlmAgent(
    model='gemini-2.0-flash-001',
    name='poet_agent',
    description='generate a poet',
    instruction='100文字程度で詩を作成する',
    output_key='poet',
    tool=[poet_tool],
)


regional_lang_agent= LlmAgent(
    model='gemini-2.0-flash-001',
    name='hougen_agent',
    description='日本の方言に変換する',
    instruction='指定された方言で、この文章を変換して\n{poet}',
)

seq_agent = SequentialAgent(
    sub_agents=[poet_agent, regional_lang_agent],
    name='seq_agent',
    description='指定したテーマと方言を使って詩を作って',
)

root_agent = seq_agent
