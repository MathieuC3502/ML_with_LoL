import matplotlib.pyplot as plt
import random

def game_duration_distribution(dataframe,show=True):
    """Plots the distribution of game durations in the dataset

    Parameters
    ----------
    dataframe : pandas.DataFrame
        The dataset containing the game durations
    """
    # Drop duplicate gameIds to ensure each game is counted only once
    unique_games = dataframe.drop_duplicates(subset='gameId')

    # Plot the distribution of game durations
    plt.figure()
    unique_games['gameDuration'].plot(kind='hist',bins=100)
    plt.title('Distribution of Game Durations')
    plt.xlabel('Game Duration (minutes)')
    plt.ylabel('Amount of Games')
    if show:
        plt.show()

def get_unique_games_id(dataframe):
    """Returns the unique game IDs in the dataset

    Parameters
    ----------
    dataframe : pandas.DataFrame
        The dataset containing the game IDs

    Returns
    -------
    numpy.ndarray
        The unique game IDs in the dataset
    """
    return dataframe['gameId'].unique()

def prepare_game_data_for_plot(df,attribute,game_id):
    """
    Prepare data for plotting the gold difference over time for a specific game.

    Parameters:
    - df: pandas DataFrame containing the dataset.
    - game_id: The ID of the game to plot.
    - attribute: The attribute to plot over time.

    Returns:
    - A DataFrame with 'frame' and attribute columns for the specified game.
    """
    # Filter the DataFrame for the given gameId
    game_data = df[df['gameId'] == game_id]

    # Select the relevant columns for plotting
    plot_data = game_data[['frame', attribute]]

    # Sort by frame to ensure the time series is in order
    plot_data = plot_data.sort_values(by='frame')

    return plot_data

def plot_kills_and_deaths_of_blue_side(num_games, dataframe):
    """
    Plots the kills and deaths of the blue side over time for a given number of games.
    
    Parameters:
        num_games (int): Number of games to study.
        dataframe (pd.DataFrame): The dataframe containing game data.
    """
    unique_ids = get_unique_games_id(dataframe)
    
    plt.figure(figsize=(12, 5))
    
    for _ in range(num_games):
        game_id = random.choice(unique_ids)
        
        kills_data = prepare_game_data_for_plot(dataframe, 'kills', game_id)
        deaths_data = prepare_game_data_for_plot(dataframe, 'deaths', game_id)
        
        plt.subplot(1, 2, 1)
        plt.plot(kills_data['frame'], kills_data['kills'], label=f'Game {game_id}')
        
        plt.subplot(1, 2, 2)
        plt.plot(deaths_data['frame'], deaths_data['deaths'], label=f'Game {game_id}')
    
    # Formatting the first subplot (Kills)
    plt.subplot(1, 2, 1)
    plt.title('Kills of Blue Side Over Time for Several Games')
    plt.xlabel('Game Time (minutes)')
    plt.ylabel('Kills')
    plt.grid()
    plt.legend()
    
    # Formatting the second subplot (Deaths)
    plt.subplot(1, 2, 2)
    plt.title('Deaths of Blue Side Over Time for Several Games')
    plt.xlabel('Game Time (minutes)')
    plt.ylabel('Deaths')
    plt.grid()
    plt.legend()
    
    plt.tight_layout()
    plt.show()