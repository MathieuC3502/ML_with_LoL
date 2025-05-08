from load_dataset import get_dataset, convert_gameDuration_to_minutes
from explore_data import game_duration_distribution, get_unique_games_id, prepare_game_data_for_plot, plot_kills_and_deaths_of_blue_side
import matplotlib.pyplot as plt

dataset_name ='League-of-Legends-SOLO-Q-Ranked-Games'
dataset_format ='dataframe'

dataframe = get_dataset(dataset_name,dataset_format)
dataframe = convert_gameDuration_to_minutes(dataframe)

# game_duration_distribution(dataframe,show=False)
plot_kills_and_deaths_of_blue_side(5, dataframe)