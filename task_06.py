def rps_game_winner(lst):

    def StrategyError():
        if (lst[0][1] and lst[1][1] != 'P') and (lst[0][1] and lst[1][1] != 'S') \
                and (lst[0][1] and lst[1][1] != 'R'):
            raise Exception('NoSuchStrategyError')

    StrategyError()

    def PlayersError():
        if len(lst) > 2:
            raise Exception('WrongNumberOfPlayersError')

    PlayersError()

    if lst[0][1] == lst[1][1]:
        return ' '.join(lst[0])
    elif lst[0][1] == 'P' and lst[1][1] == 'R':
        return ' '.join(lst[0])
    elif lst[0][1] == 'S' and lst[1][1] == 'P':
        return ' '.join(lst[0])
    elif lst[0][1] == 'R' and lst[1][1] == 'S':
        return ' '.join(lst[0])
    else:
        return ' '.join(lst[1])