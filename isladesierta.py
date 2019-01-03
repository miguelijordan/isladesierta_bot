class IslaDesierta:
    def __init__(self):
        self.players = {}

    def ok(self, word, player_name):
        player_name = player_name.lower()
        return word.startswith(player_name[0])

    def add_word_player(self, word, player):
        if player in self.players.keys():
            self.players[player].add(word)
        else:
            self.players[player] = set()
            self.players[player].add(word)

    def remove_player(self, player):
        if player in self.players.keys():
            del self.players[player]

    def player_win(self, player):
        if player in self.players.keys():
            return len(self.players[player]) >= 10
        else:
            return False

    def get_cosas(self, player)
        if player in self.players.keys():
            return self.players[player]
