import random

class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0
        self.money = 1500
        self.properties = []

class Property:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.owner = None

class MonopolyGame:
    def __init__(self, num_players):
        self.board = self.create_board()
        self.players = [Player(input(f"Enter player {i+1}'s name: ")) for i in range(num_players)]
        self.num_players = num_players
        self.current_player_index = 0

    def create_board(self):
        board = [
            Property("Go", 0),
            Property("Mediterranean Avenue", 60),
            Property("Community Chest", 0),
            Property("Baltic Avenue", 60),
            Property("Income Tax", 200),
            Property("Reading Railroad", 200),
            Property("Oriental Avenue", 100),
            Property("Chance", 0),
            Property("Vermont Avenue", 100),
            Property("Connecticut Avenue", 120),
            Property("Jail", 0),
            Property("St. Charles Place", 140),
            Property("Electric Company", 150),
            Property("States Avenue", 140),
            Property("Virginia Avenue", 160),
            Property("Pennsylvania Railroad", 200),
            Property("St. James Place", 180),
            Property("Community Chest", 0),
            Property("Tennessee Avenue", 180),
            Property("New York Avenue", 200),
            Property("Free Parking", 0),
            Property("Kentucky Avenue", 220),
            Property("Chance", 0),
            Property("Indiana Avenue", 220),
            Property("Illinois Avenue", 240),
            Property("B. & O. Railroad", 200),
            Property("Atlantic Avenue", 260),
            Property("Ventnor Avenue", 260),
            Property("Water Works", 150),
            Property("Marvin Gardens", 280),
            Property("Go To Jail", 0),
            Property("Pacific Avenue", 300),
            Property("North Carolina Avenue", 300),
            Property("Community Chest", 0),
            Property("Pennsylvania Avenue", 320),
            Property("Short Line", 200),
            Property("Chance", 0),
            Property("Park Place", 350),
            Property("Luxury Tax", 100),
            Property("Boardwalk", 400)
        ]
        return board

    def roll_dice(self):
        return random.randint(1, 6), random.randint(1, 6)

    def move_player(self, player, steps):
        player.position = (player.position + steps) % len(self.board)

    def handle_property(self, player, property):
        if property.owner is None:
            buy = input(f"{property.name} is unowned. Do you want to buy it for ${property.price}? (yes/no): ")
            if buy.lower() == "yes":
                if player.money >= property.price:
                    player.money -= property.price
                    player.properties.append(property)
                    property.owner = player
                    print(f"{player.name} bought {property.name}.")
                else:
                    print("You don't have enough money to buy this property.")
            else:
                print(f"{property.name} remains unowned.")
        elif property.owner != player:
            rent = property.price // 10  # Arbitrary rent calculation
            player.money -= rent
            property.owner.money += rent
            print(f"{player.name} paid ${rent} as rent to {property.owner.name} for landing on {property.name}.")
        else:
            print(f"You already own {property.name}.")

    def play_turn(self, player):
        input(f"It's {player.name}'s turn. Press Enter to roll the dice...")
        dice1, dice2 = self.roll_dice()
        total_steps = dice1 + dice2
        print(f"{player.name} rolled {dice1} and {dice2}, moving {total_steps} steps.")
        self.move_player(player, total_steps)
        current_property = self.board[player.position]
        print(f"{player.name} landed on {current_property.name}.")
        if isinstance(current_property, Property):
            self.handle_property(player, current_property)

    def start_game(self):
        while True:
            for player in self.players:
                self.play_turn(player)
                if input("Press 'q' to quit, any other key to continue: ") == 'q':
                    return

# Example usage:
num_players = int(input("Enter the number of players: "))
game = MonopolyGame(num_players)
game.start_game()
