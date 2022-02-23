class Player:
    def __init__(self, player_name = None):
        self.player_name = player_name
    
    def output_player_name(self):
        return self.player_name
    
    def input_player_data(self, player_name):
        self.player_name = player_name

def creat_name_func(cmd_input):
    player = Player()
    player.input_player_data(cmd_input)

    player_name = player.output_player_name()
    return player_name
