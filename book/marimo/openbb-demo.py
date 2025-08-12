# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo==0.13.15",
#     "python-dotenv==1.1.0",
#     "openbb==4.4.3",
#     "plotly==6.1.2",
# ]
# ///
import marimo

__generated_with = "0.13.15"
app = marimo.App(width="medium")

with app.setup:
    import openbb as obb
    import plotly.graph_objects as go
    from dotenv import load_dotenv

@app.cell
def _():
    import os

    load_dotenv(verbose=True, override=True)
    api_token = os.getenv("PAT")
    return api_token


@app.cell
def _(api_token):
    obb.account.login(pat=api_token)

    output = obb.equity.price.historical("AAPL")
    dframe = output.to_dataframe()
    return dframe


@app.cell
def _(dframe):
    # Extract the last 5 rows
    df_tail = dframe.drop(['dividend','volume'], axis=1)

    # Create an empty figure
    fig = go.Figure()

    # Loop through each column (excluding the Date column) and add a trace for each
    for column in df_tail.columns:
        fig.add_trace(go.Scatter(
            x=df_tail.index,
            y=df_tail[column],
            mode='lines+markers',  # 'lines+markers' shows both lines and data points
            name=column  # The legend will show the column name
        ))

    # Add labels and title
    fig.update_layout(
        title='Line Chart for Each Column',
        xaxis_title='Date',
        yaxis_title='Value',
        legend_title="Columns",
        template='ggplot2',  # Optional: You can choose from different Plotly themes (e.g., 'plotly', 'plotly_dark')
    )

    # Show the plot
    # fig

if __name__ == "__main__":
    app.run()
