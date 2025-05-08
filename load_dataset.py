import openml

def get_dataset(dataset_name,dataset_format):
    """Loads the desired OpenML dataset from its name and returns it in the specified format

    Parameters
    ----------
    dataset_name : str
        Name of the desired OpenML dataset
    dataset_format : str
        Desired format of the dataset.

    Returns
    -------
    Format specified by dataset_format
        The desired dataset in the specified format
    """
    # Get dataset by name
    dataset = openml.datasets.get_dataset(dataset_name)

    # Get the data itself as a dataframe
    dataframe,_,_,_ = dataset.get_data(dataset_format=dataset_format)
    return dataframe

def convert_gameDuration_to_minutes(dataframe):
    """Converts the gameDuration column from milliseconds to minutes

    Parameters
    ----------
    dataframe : pandas.DataFrame
        The dataset containing the game durations

    Returns
    -------
    pandas.DataFrame
        The dataset with the gameDuration column converted to minutes
    """
    # Convert gameDuration from milliseconds to minutes
    dataframe['gameDuration'] = dataframe['gameDuration'] / 60000
    return dataframe