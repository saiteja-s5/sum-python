# Build-in libraries
from datetime import datetime

# 3rd Party libraries
import requests
import plotly.graph_objects as go


fund_url = 'http://localhost:9393/chart/fund/BWT6410561408'
fund_api_response = requests.get(fund_url)
if fund_api_response.status_code == 200:
    chart_data = fund_api_response.json().get('chart')
    chart_dates = [datetime.fromisoformat(dt) for dt in chart_data.keys()]
    chart_values = [float(val) for val in chart_data.values()]

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=chart_dates,
        y=chart_values,
        mode='lines+markers',
        line=dict(color='royalblue', width=2),
        marker=dict(size=1)
    ))

    fig.update_layout(
        title='Fund Chart',
        xaxis_title='Date',
        yaxis_title='Value',
        hovermode='x unified',
        xaxis=dict(
            rangeslider=dict(visible=True),
            type='date'
        )
    )

    fig.show()

else:
    print('Data not fetched from API')