from google.adk.agents import Agent

root_agent = Agent(
    model='gemini-2.0-flash-001',
    name='root_agent',
    description='generate a haiku',
    instruction='現代のキーワードを使った俳句を作成してください。',
)
