from pathlib import Path

import pandas as pd
import plotly.express as px
from shiny import App, ui
from shinywidgets import output_widget, render_widget

# Instructions for each step are on the docs page, in the "Shiny Codelab" section.
# Run the app with:
#     shiny run --reload source/CL5_shiny_codelab.py

##########################################
# Model
##########################################
scouted_data = pd.read_csv(Path(__file__).parent / "data" / "scouted_data.csv")

# NOTE: Don't do this in the real app. Normally we would have separate csv / json files for the match schedule
# and team list, but for simplicity this example piggybacks off the fact that scouted_data is for a finished competition.
match_numbers = [str(match_number) for match_number in sorted(scouted_data["match_number"].unique())]
team_keys = sorted(scouted_data["team_key"].unique(), key=lambda team_key: int(team_key[3:]))


##########################################
# View
##########################################
match_preview_ui = ui.layout_sidebar(
    ui.sidebar(
        ui.input_select("match_select", "Match Number:", choices=match_numbers),
    ),
    ui.card(output_widget("match_average_points")),
    ui.card(output_widget("match_contributed_points")),
    # TODO: Step 4
)

team_overview_ui = ui.layout_sidebar(
    ui.sidebar(
        ui.input_select("team_select", "Team:", choices=team_keys),
    ),
    ui.card(output_widget("team_points_over_time")),
    # TODO: Step 7
)

app_ui = ui.page_navbar(
    ui.nav_panel("Match Preview", match_preview_ui),
    ui.nav_panel("Team Overview", team_overview_ui),
    title="GOS Scouting Codelab",
)


##########################################
# Presenter
##########################################
def server(input, output, session):

    ##########################################
    # Match Preview
    ##########################################
    def get_teams_in_selected_match():
        # TODO: Step 1 - Read the match number from the "match_select" combo box
        match_number = None

        # NOTE: The real app gets the teams from the match schedule, see the note at the top
        teams = scouted_data.loc[scouted_data["match_number"] == match_number, "team_key"].unique()
        return scouted_data[scouted_data["team_key"].isin(teams)]

    # TODO: Step 2

    # TODO: Step 3

    # TODO: Step 4

    ##########################################
    # Team Overview
    ##########################################
    def get_selected_team_data():
        # TODO: Step 5 - Read the team from the "team_select" combo box
        team = None

        return scouted_data[scouted_data["team_key"] == team]

    # TODO: Step 6

    # TODO: Step 7


app = App(app_ui, server)
