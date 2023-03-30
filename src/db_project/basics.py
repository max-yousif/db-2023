"""
Contains basic functions, also implemented in the notebooks themselves.
"""

import getpass  # Package om een paswoordveldje te genereren.

import mysql.connector
import pandas as pd  # Populaire package voor data-verwerking



def res_to_df(query_result, column_names):
    """
    Zet ruwe output van een query om naar een DataFrame met gegeven kolomnamen.

    Let op: Het resultaat van de query moet dus exact evenveel kolommen bevatten
    als kolomnamen die je meegeeft. Als dit niet het geval is, is dit een indicatie
    dat je oplossing fout is. (Gezien wij de kolomnamen van de oplossing al cadeau doen)

    Parameters
    ----------
    query_result:
                    Resultaat van een uitgevoerde query zoals dat gegeven wordt
                    door cursor.fetchall()
    column_names    list
                    Lijst van kolomnamen voor het resulterende DataFrame

    Returns
    -------
    df:             pd.DataFrame
                    DataFrame dat het resultaat bevat.

    """

    df = pd.DataFrame(query_result, columns=column_names)
    return df
