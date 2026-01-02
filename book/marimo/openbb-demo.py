# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo==0.14.16",
#     "python-dotenv==1.1.0",
#     "openbb",
#     "plotly==6.2.0"
# ]
# ///

"""OpenBB demonstration notebook using Marimo.

This script demonstrates how to use the OpenBB SDK to fetch financial data
for Apple Inc. and visualize it using Plotly within a Marimo interactive app.
"""

import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")

with app.setup:
    import plotly.graph_objects as go


@app.cell
def _():
    from openbb import obb

    # Fetch historical prices for AAPL
    result = obb.equity.price.historical(symbol="AAPL")

    # Convert OBObject to DataFrame
    df = result.to_dataframe()

    # Make sure Date is sorted ascending
    df = df.sort_values("date")

    return df


@app.cell
def _(df):
    # Create a Plotly candlestick chart
    fig = go.Figure(
        data=[
            go.Candlestick(
                x=df["date"], open=df["open"], high=df["high"], low=df["low"], close=df["close"], name="AAPL"
            )
        ]
    )

    fig.update_layout(
        title="AAPL Historical Prices",
        yaxis_title="Price (USD)",
        xaxis_title="Date",
        template="plotly_dark",
        xaxis_rangeslider_visible=False,
    )

    fig.show()
    return fig


if __name__ == "__main__":
    main = app.run
