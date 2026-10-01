"""
Generates the interactive figures that are embedded in plotly-lab.rst.

The code snippets shown in the docs are pulled straight out of this file (look for the
"# [name]" / "# [/name]" markers), so if you change an example here, re-run this script and
the docs will stay in sync:

    python docs/source/code-labs/plotly/generate_figures.py
"""

import pathlib

import plotly.express as px

OUTPUT_DIR = pathlib.Path(__file__).parent / "figures"


def save(fig, name):
    OUTPUT_DIR.mkdir(exist_ok=True)
    fig.write_html(
        OUTPUT_DIR / f"{name}.html",
        full_html=False,
        include_plotlyjs="cdn",
        default_height="450px",
        div_id=name,
    )


def main():
    # [load]
    import plotly.express as px

    df = px.data.tips()
    # [/load]

    # [scatter]
    fig = px.scatter(df, x="total_bill", y="tip", color="time", title="Tip vs. Total Bill")
    # [/scatter]
    save(fig, "scatter")

    # [scatter_average]
    day_averages = df.groupby("day").mean(numeric_only=True).reset_index()

    fig = px.scatter(day_averages, x="total_bill", y="tip", text="day", title="Average Tip vs. Average Bill per Day")
    fig.update_traces(textposition="top center")
    # [/scatter_average]
    save(fig, "scatter_average")

    # [box]
    fig = px.box(df, x="day", y="tip", points="all", title="Tips per Day")
    # [/box]
    save(fig, "box")

    # [bar]
    day_averages = df.groupby("day").mean(numeric_only=True).reset_index()
    day_averages = day_averages.sort_values("tip", ascending=False)

    fig = px.bar(day_averages, x="day", y="tip", title="Average Tip per Day")
    # [/bar]
    save(fig, "bar")

    # [pie_count]
    fig = px.pie(df, names="day", title="Number of Meals per Day")
    # [/pie_count]
    save(fig, "pie_count")

    # [pie_values]
    fig = px.pie(df, names="day", values="tip", title="Total Tips per Day")
    # [/pie_values]
    save(fig, "pie_values")

    # [stacked_count]
    smoker_counts = df.groupby(["day", "smoker"]).size().reset_index(name="count")

    fig = px.bar(smoker_counts, x="day", y="count", color="smoker", title="Number of Meals per Day")
    # [/stacked_count]
    save(fig, "stacked_count")

    # [stacked_sum]
    smoker_tips = df.groupby(["day", "smoker"])["tip"].sum().reset_index()

    fig = px.bar(smoker_tips, x="day", y="tip", color="smoker", title="Total Tips per Day")
    # [/stacked_sum]
    save(fig, "stacked_sum")

    # [stacked_columns]
    day_averages = df.groupby("day").mean(numeric_only=True).reset_index()

    fig = px.bar(day_averages, x="day", y=["total_bill", "tip"], title="Average Amount Paid per Day")
    # [/stacked_columns]
    save(fig, "stacked_columns")

    # [customized]
    fig = px.box(
        df,
        x="day",
        y="tip",
        color="time",
        points="all",
        hover_data=["total_bill", "size"],
        category_orders={"day": ["Thur", "Fri", "Sat", "Sun"]},
        labels={"day": "Day of the Week", "tip": "Tip ($)", "time": "Meal", "total_bill": "Bill ($)", "size": "Party Size"},
        title="Tips per Day, Split by Meal",
    )
    fig.update_layout(legend_title_text="Which Meal?")
    # [/customized]
    save(fig, "customized")


if __name__ == "__main__":
    main()
