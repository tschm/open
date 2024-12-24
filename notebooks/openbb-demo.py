import marimo

__generated_with = "0.10.6"
app = marimo.App(width="medium")


@app.cell
def _():
    from openbb import obb
    output = obb.equity.price.historical("AAPL")
    df = output.to_dataframe()
    return df, obb, output


@app.cell
def _(df):
    import plotly.graph_objects as go

    # Extract the last 5 rows
    df_tail = df.drop(['dividend','volume'], axis=1)

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
    fig.show()
    return column, df_tail, fig, go


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
