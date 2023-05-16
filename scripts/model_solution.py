def query_01(connection, column_names, X=1980, Y=50):

    # Bouw je query
    query = """
    SELECT DISTINCT nameLast, nameFirst, height
    FROM master as m JOIN allstarfull as a on a.playerID=m.playerID
    WHERE a.yearID < {X} and m.height>{Y}
    ORDER by nameLast, nameFirst, height DESC; 
    """.format(X=X,Y=Y)

    # Stap 2 & 3
    res = run_query(connection, query)  # Query uitvoeren
    df = res_to_df(res, column_names)  # Query in DataFrame brengen

    return df

def query_02(connection, column_names, X="'USA'", Y=40):

    # Bouw je query
    query = """
    SELECT nameLast, nameFirst, deathYear-birthYear as age, deathCountry 
    FROM master 
    WHERE birthCountry={X} 
        and deathYear>0
        and birthYear>0 
        and deathYear-birthYear<{Y}
    ORDER BY age ASC, nameFirst, nameLast, deathCountry;
    """.format(X=X,Y=Y)

    # Stap 2 & 3
    res = run_query(connection, query)  # Query uitvoeren
    df = res_to_df(res, column_names)  # Query in DataFrame brengen

    return df

def query_03(connection, column_names, X=1940, Y=1980, Z=1):

    # Bouw je query
    query = """
    SELECT m.nameLast, m.nameFirst, m.birthYear, t.name, ma.yearID,  100*t.w/t.G as teamWins, 100*ma.L/ma.G as managerLosses
    FROM master as m JOIN managers as ma on m.playerID=ma.playerID join teams as t on ma.teamID=t.teamID
    WHERE ma.yearID=t.yearID and ma.yearID>={X} and ma.yearID<={Y} and ma.inseason={Z} and t.W > t.L and ma.W<ma.L and birthyear>0
    ORDER BY nameLast, nameFirst, birthYear DESC, t.name,teamWins DESC, managerLosses DESC;
    """.format(X=X,Y=Y,Z=Z)

    # Stap 2 & 3
    res = run_query(connection, query)  # Query uitvoeren
    df = res_to_df(res, column_names)  # Query in DataFrame brengen

    return df

def query_04(connection, column_names, X=1940, Y=3):

    # Bouw je query
    query = """
    SELECT h.yearId,h.votedby, count(distinct h.playerID) as cv, avg(h.votes) as av
    FROM halloffame as h join managers as m on h.playerID=m.playerID join master as ma on ma.playerID=m.playerID
    WHERE ma.birthYear>{X} and h.votes>0
    GROUP BY h.yearid, h.votedby
    HAVING cv>={Y}
    ORDER BY yearID DESC, votedBy ASC, cv DESC, av DESC;
    """.format(X=X,Y=Y)

    # Stap 2 & 3
    res = run_query(connection, query)  # Query uitvoeren
    df = res_to_df(res, column_names)  # Query in DataFrame brengen

    return df

def query_05(connection, column_names, X=1960):

    # Bouw je query
    query = """
    SELECT m.nameLast, m.nameFirst, m.birthYear
    FROM Pitching p join Master m on  p.playerID=m.playerID
    WHERE m.birthYear>0
    GROUP BY p.playerID
    HAVING MIN(p.yearID) < {X} AND  SUM(p.W)>SUM(p.L) AND SUM(p.SO)>SUM(p.H) 
    ORDER BY m.nameLast, m.nameFirst, m.birthYear ASC;
    """.format(X=X)

    # Stap 2 & 3
    res = run_query(connection, query)  # Query uitvoeren
    df = res_to_df(res, column_names)  # Query in DataFrame brengen

    return df


def query_06(connection, column_names, X="'TX'"):

    # Bouw je query
    query = """
    SELECT DISTINCT m.nameLast, m.nameFirst, h.yearid, h.votes
    FROM schools as s join collegeplaying as c on s.schoolID=c.schoolID join master as m on m.playerID=c.playerID LEFT OUTER JOIN halloffame as h on m.playerid=h.playerID
    WHERE NOT EXISTS (SELECT * from fielding as f join teams as t on f.teamID=t.teamID join parks as p on p.`park.name`=t.park 
                      where f.playerID=m.playerID and f.yearid=t.yearid and p.city=m.birthCity)
          AND s.state={X}
    ORDER BY  m.nameLast, m.nameFirst, h.yearid, h.votes DESC;
    """.format(X=X)

    # Stap 2 & 3
    res = run_query(connection, query)  # Query uitvoeren
    df = res_to_df(res, column_names)  # Query in DataFrame brengen

    return df

def query_07(connection, column_names, X=2, Y=500):

    # Bouw je query
    query = """
    SELECT m.nameLast, m.nameFirst, sum(f.e)/sum(f.G) as err
    FROM master as m join fielding as f on f.playerID=m.playerID
    WHERE (SELECT max(p.yearid) 
           FROM pitching as p 
           WHERE p.playerID=m.playerID GROUP BY p.playerID)+{X} in (SELECT b.yearid FROM batting as b WHERE b.playerID=m.playerID)
    and EXISTS (SELECT *
         FROM managers as ma join collegeplaying as c on c.playerID=ma.playerID 
         WHERE ma.yearID=(SELECT min(pi.yearID) FROM pitching as pi WHERE pi.playerID=m.playerID and pi.stint=1)
            and ma.teamID=(SELECT pi2.teamID FROM pitching as pi2 WHERE pi2.playerID=m.playerID and pi2.yearID=ma.yearID and pi2.stint=1)
            and c.schoolID in (SELECT c2.schoolID FROM collegeplaying as c2 WHERE c2.playerID=m.playerID))
    GROUP BY m.playerID
    HAVING sum(f.a)>{Y}
    ORDER BY err DESC, m.nameLast, m.nameFirst;
    """.format(X=X, Y=Y)

    # Stap 2 & 3
    res = run_query(connection, query)  # Query uitvoeren
    df = res_to_df(res, column_names)  # Query in DataFrame brengen

    return df


def query_08(connection, column_names):
    # Bouw je 1ste query die de tabel opbouwt
    query = """
    CREATE OR REPLACE TABLE lahman2016.sieben_bocklandt AS
    SELECT m.nameLast as last_name, m.nameFirst as first_name, count(DISTINCT a.yearid)+count(DISTINCT ma2.yearid) as ycount
    FROM master as m join awardsplayers as a on a.playerID=m.playerID join awardsmanagers as ma2 on ma2.playerID = m.playerID
    WHERE (SELECT max(a1.yearID) FROM awardsplayers as a1 WHERE a1.playerID=m.playerID) + 20 > ANY (SELECT ma.yearID FROM awardsmanagers as ma WHERE ma.playerID=m.playerID) 
    and ma2.yearID not in (Select yearid from awardsplayers as a2 where a2.playerID=m.playerID)
    GROUP BY m.nameLast, m.nameFirst; 
    """

    try:
        run_query(connection, query)  # Query uitvoeren
    except Exception as e:
        print(e)

    # bouw je 2de query die alle resultaten uit die tabel opvraagt
    query = """
    SELECT * from lahman2016.sieben_bocklandt
    ORDER BY last_name, first_name, ycount;
    """

    # Stap 2 & 3
    res = run_query(connection, query)  # Query uitvoeren
    df = res_to_df(res, column_names)  # Query in DataFrame brengen

    return df


def query_09(connection, column_names, X=4):
    # Bouw je query die de gevraagde waardes verwijdert
    query = """
    DELETE FROM lahman2016.sieben_bocklandt
    WHERE ycount IN (SELECT s1.ycount FROM lahman2016.sieben_bocklandt as s1 GROUP BY s1.ycount HAVING count(s1.ycount)>{X}+1);
    """.format(X=X)

    # Stap 2 & 3
    try:
        run_query(connection, query)  # Query uitvoeren
    except Exception as e:
        print(e)

    # Bouw je query die alle resultaten uit de geupdate tabel opvraagt
    query = """
    SELECT * from lahman2016.sieben_bocklandt
    ORDER BY last_name, first_name, ycount;
    """

    # Stap 2 & 3
    res = run_query(connection, query)  # Query uitvoeren
    df = res_to_df(res, column_names)  # Query in DataFrame brengen

    return df

def query_10(connection, column_names,X=1990, Y=91):

    # Bouw je query
    query = """
    SELECT m.nameLast, m.nameFirst
    FROM master as m 
    WHERE NOT EXISTS (
    SELECT *
    FROM teams as t
        where t.yearID={X} and t.W>{Y} and
      NOT EXISTS (
    SELECT *
    FROM pitching as p 
    WHERE p.playerID = m.playerID and
    p.teamID=t.teamID)
    );
    """.format(X=X,Y=Y)

    # Stap 2 & 3
    res = run_query(connection, query)  # Query uitvoeren
    df = res_to_df(res, column_names)  # Query in DataFrame brengen

    return df

