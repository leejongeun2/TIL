# 내가 보고 싶은 주가를 선택할 수 있도록
# 코스피 200, 코스피, 코스닥을 대쉬보드 그리기.
# 드롭다운 메뉴로 위 속성 구성 

import dash
from dash.dependencies import Input, Output # 정의
from dash import dcc 
from dash import html # 렌더링 할 요소 구현
import pandas as pd

# 대시보드 앱 정의
app = dash.Dash('K-Index', external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])

# app layout-> html 수정.
app.layout = html.Div([
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            # dropdown 메뉴 만들기!
            {'label':'KOSPI', 'value':'./data/kospi.xlsx'},
            {'label':'KOSPI200', 'value':'./data/kpi200.xlsx'},
            {'label':'KOSDAQ', 'value':'./data/kosdaq.xlsx'}          
        ],  
        value='./data/kospi.xlsx'# 기본값 세팅하기
    ),  
    dcc.Graph(id='my-graph')
], style={'width': '600'})



@app.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value')])
# dash가 실제로 실행하는 그래프를 update_graph 함수로 정의합니다.
def update_graph(selected_dropdown_value):
    # 내가 선택한 label에 해당하는 파일 이름
    
    df = pd.read_excel(selected_dropdown_value).sort_values(by="date")
    return {
        'data': [
            # dash가 보여줄 dashboard의 그래프를 dict 형태로 지정합니다.
            {'x':df.date,
             'y':df.price}
        
        ],
        'layout': {'margin': {'l': 40, 'r': 0, 't': 20, 'b': 30}} # 색깔, 크기, 위치, 타이틀 조절 가능
    }   

# dash app이 실행됩니다.
# result = app.run_server(debug=True, use_reloader=False)
result = app.run_server(host='192.168.0.3', port=3003)
print(result)