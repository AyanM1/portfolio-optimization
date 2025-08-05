# Visualization utilities for portfolio analysis

import plotly.express as px
import plotly.graph_objects as go


def plot_efficient_frontier(risks, returns):
    """
    Plot the efficient frontier (risk vs. return scatter).
    """
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=risks, y=returns, mode='lines+markers', name='Efficient Frontier'))
    fig.update_layout(title='Efficient Frontier', xaxis_title='Risk (Volatility)', yaxis_title='Return')
    fig.show()

def plot_correlation_heatmap(data):
    """
    Plot a correlation heatmap for the given data.
    """
    corr = data.corr()
    fig = px.imshow(corr, text_auto=True, color_continuous_scale='Viridis', title='Correlation Heatmap')
    fig.show()

def plot_risk_metrics_bar(metrics: dict):
    """
    Plot risk metrics as a bar chart.
    """
    fig = px.bar(x=list(metrics.keys()), y=list(metrics.values()), labels={'x':'Metric', 'y':'Value'}, title='Risk Metrics')
    fig.show()
