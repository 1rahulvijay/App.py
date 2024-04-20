import pandas as pd

def calculate_mean(df):
    """
    Calculate the mean of the DataFrame.

    Parameters:
    df (DataFrame): Input DataFrame.

    Returns:
    float: Mean of the DataFrame.

    Examples:
    >>> df = pd.DataFrame({'A': [1, 2, 3, 4]})
    >>> calculate_mean(df)
    2.5
    """
    return df.mean()

if __name__ == "__main__":
    import doctest
    doctest.testmod()

