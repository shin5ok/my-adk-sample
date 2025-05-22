from google.adk.agents import LlmAgent
from google.adk.sessions import InMemorySessionService  # セッション管理サービスをインポート
from google.adk.runners import Runner # エージェントを実行するためのRunnerをインポート

def haiku_tool(theme: str) -> str:
    '''
    指定されたテーマに沿って、俳句を作成します
    俳句は5-7-5の形式で、ユーザーの指示に従ってください

    Return: 文字列
    '''
    return "ほげほげ俳句"

def tanka_tool(theme: str) -> str:
    '''
    指定されたテーマに沿って、短歌を作成します
    短歌は5-7-5-7-7の形式で、ユーザーの指示に従ってください

    Return: 文字列
    '''
    return "ほげほげ短歌"

def novel_tool(theme: str) -> str:
    '''
    指定されたテーマに沿って、小説を作成します
    小説は1000文字程度で、ユーザーの指示に従ってください

    Return: 文字列
    '''
    return "ほげほげ小説です"

root_agent = LlmAgent(
    model='gemini-2.0-flash-001',
    name='root_agent',
    description='指定されたテーマに沿って、俳句、短歌、小説を作成する',
    instruction='''
    あなたは文章のプロで、日本人です
    また、博多出身なので、博多弁で話します
    あなたは、指定されたテーマに沿って、俳句、短歌、小説を作成します
    俳句は5-7-5の形式で、短歌は5-7-5-7-7の形式で、小説は1000文字程度で作成します
    俳句、短歌、小説のどれを選択するかは、ユーザーの指示に従ってください
    ''',
    tools=[haiku_tool, tanka_tool, novel_tool]
)

def main():
    agent = root_agent
    runner = Runner(
        agent=agent,
        session_service=InMemorySessionService() # セッションサービスを設定 [9]
    )

    # ユーザーとの対話 [9]
    session = runner.create_session()
    response = runner.run(session, "大阪の天気を教えてください") # ユーザー入力を実行 [9]
    print(response.text)

if __name__ == "__main__":
    main()