def query_01(connection, column_names, X=1980, Y=50):

    # Bouw je query
    query = """
    SELECT DISTINCT nameLast, nameFirst, height
    FROM master as m JOIN allstarfull as a on a.playerID=m.playerID
    ORDER by nameLast, nameFirst, height DESC; 
    """

    # Stap 2 & 3
    res = run_query(connection, query)  # Query uitvoeren
    df = res_to_df(res, column_names)  # Query in DataFrame brengen

    return df

def query_02(connection, column_names, X="'USA'", Y=40):

    # Bouw je query
    query = """
    Maak hier je query
    """

    # Stap 2 & 3
    res = run_query(connection, query)  # Query uitvoeren
    df = res_to_df(res, column_names)  # Query in DataFrame brengen

    return df

def query_03(connection, column_names, X=1940, Y=1980, Z=1):

    # Bouw je query
    query = """
        Maak hier je query
        """

    # Stap 2 & 3
    res = run_query(connection, query)  # Query uitvoeren
    df = res_to_df(res, column_names)  # Query in DataFrame brengen

    return df

def query_04(connection, column_names, X=1940, Y=30):

    # Bouw je query
    query = """
        Maak hier je query
        """

    # Stap 2 & 3
    res = run_query(connection, query)  # Query uitvoeren
    df = res_to_df(res, column_names)  # Query in DataFrame brengen

    return df

def query_05(connection, column_names, X=1960):

    # Bouw je query
    query = """
        Maak hier je query
        """

    # Stap 2 & 3
    res = run_query(connection, query)  # Query uitvoeren
    df = res_to_df(res, column_names)  # Query in DataFrame brengen

    return df


def query_06(connection, column_names, X="'TX'"):

    # Bouw je query
    query = """
        Maak hier je query
        """

    # Stap 2 & 3
    res = run_query(connection, query)  # Query uitvoeren
    df = res_to_df(res, column_names)  # Query in DataFrame brengen

    return df

def query_07(connection, column_names, X=500):

    # Bouw je query
    query = """
        Maak hier je query
        """

    # Stap 2 & 3
    res = run_query(connection, query)  # Query uitvoeren
    df = res_to_df(res, column_names)  # Query in DataFrame brengen

    return df


def query_08(connection, column_names):
    # Bouw je 1ste query die de tabel opbouwt
    query = """
        Maak hier je query
        """

    try:
        run_query(connection, query)  # Query uitvoeren
    except Exception as e:
        print(e)

    # bouw je 2de query die alle resultaten uit die tabel opvraagt
    query = """
        Maak hier je query
        """

    # Stap 2 & 3
    res = run_query(connection, query)  # Query uitvoeren
    df = res_to_df(res, column_names)  # Query in DataFrame brengen

    return df


def query_09(connection, column_names, X=4):
    # Bouw je query die de gevraagde waardes verwijdert
    query = """
        Maak hier je query
        """

    # Stap 2 & 3
    try:
        run_query(connection, query)  # Query uitvoeren
    except Exception as e:
        print(e)

    # Bouw je query die alle resultaten uit de geupdate tabel opvraagt
    query = """
        Maak hier je query
        """

    # Stap 2 & 3
    res = run_query(connection, query)  # Query uitvoeren
    df = res_to_df(res, column_names)  # Query in DataFrame brengen

    return df

def query_10(connection, column_names,X=1990, Y=91):

    # Bouw je query
    query = """
        Maak hier je query
        """

    # Stap 2 & 3
    res = run_query(connection, query)  # Query uitvoeren
    df = res_to_df(res, column_names)  # Query in DataFrame brengen

    return df

