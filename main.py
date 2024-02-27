import random

class Player:
    def __init__(self, name, starting_balance, properties):
        self.name = name
        self.position = 0
        self.money = starting_balance
        self.properties = properties

    def move(self, steps):
        self.position = (self.position + steps) % len(self.properties)


class Property:
    def __init__(self, name, cost, rent):
        self.name = name
        self.cost = cost
        self.owner = None
        self.rent = rent
        self.is_mortgaged = False

    def is_owned(self):
        return self.owner is not None

    def mortgage(self):
        if not self.is_mortgaged:
            self.is_mortgaged = True
            self.owner.money += self.cost // 2  # Player gets half of the property cost when mortgaging

    def unmortgage(self):
        if self.is_mortgaged:
            self.is_mortgaged = False
            self.owner.money -= int(self.cost * 0.6)  # Player pays 10% interest when unmortgaging

    def calculate_rent(self):
        if self.is_mortgaged:
            return 0
        else:
            return self.rent


class MonopolyGame:
    def __init__(self, players):
        self.players = players
        self.properties = [
            Property("Mediterranean Avenue", 60, 2),
            Property("Baltic Avenue", 60, 4),
            Property("Oriental Avenue", 100, 6),
            Property("Vermont Avenue", 100, 6),
            Property("Connecticut Avenue", 120, 8),
            Property("St. Charles Place", 140, 10),
            Property("States Avenue", 140, 10),
            Property("Virginia Avenue", 160, 12),
            Property("St. James Place", 180, 14),
            Property("Tennessee Avenue", 180, 14),
            Property("New York Avenue", 200, 16),
            Property("Kentucky Avenue", 220, 18),
            Property("Indiana Avenue", 220, 18),
            Property("Illinois Avenue", 240, 20),
            Property("Atlantic Avenue", 260, 22),
            Property("Ventnor Avenue", 260, 22),
            Property("Marvin Gardens", 280, 24),
            Property("Pacific Avenue", 300, 26),
            Property("North Carolina Avenue", 300, 26),
            Property("Pennsylvania Avenue", 320, 28),
            Property("Park Place", 350, 35),
            Property("Boardwalk", 400, 50),
            # Add utilities
            Property("Electric Company", 150, 0),  # Rent calculated based on dice roll
            Property("Water Works", 150, 0),  # Rent calculated based on dice roll
            # Add railroads
            Property("Reading Railroad", 200, 25),
            Property("Pennsylvania Railroad", 200, 25),
            Property("B&O Railroad", 200, 25),
            Property("Short Line", 200, 25),
            # Add special spaces (Chance and Community Chest)
            Property("Chance", 0, 0),
            Property("Community Chest", 0, 0),
            # Add tax spaces
            Property("Income Tax", 200, 0),  # Usually 10% or $200
            Property("Luxury Tax", 100, 0),  # Usually $100
            # Add Jail and Go to Jail spaces
            Property("Jail", 0, 0),
            Property("Go to Jail", 0, 0),
            # Add Free Parking space
            Property("Free Parking", 0, 0),
        ]

        for player in self.players:
            player.properties = self.properties  # Pass the properties list to each player
        self.current_player_index = 0

    def roll_dice(self):
        return random.randint(1, 6), random.randint(1, 6)

    def next_player(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def play_turn(self):
        player = self.players[self.current_player_index]
        print(f"It's {player.name}'s turn.")
        input("Press Enter to roll the dice...")
        dice1, dice2 = self.roll_dice()
        steps = dice1 + dice2
        print(f"{player.name} rolled {dice1} and {dice2}, moving {steps} steps.")
        player.move(steps)
        current_property = self.properties[player.position]
        print(f"{player.name} landed on {current_property.name}.")

        if not current_property.is_owned():
            buy_option = input("Do you want to buy this property? (yes/no): ")
            if buy_option.lower() == "yes":
                if player.money >= current_property.cost:
                    player.money -= current_property.cost
                    current_property.owner = player
                    print(f"{player.name} bought {current_property.name}.")
                else:
                    print("You don't have enough money to buy this property.")
            else:
                print(f"{current_property.name} remains unowned.")

        elif current_property.owner != player:
            rent = current_property.calculate_rent()
            print(f"This property is owned by {current_property.owner.name}. You need to pay rent of ${rent}.")
            player.money -= rent
            current_property.owner.money += rent
            print(f"{player.name} paid ${rent} in rent to {current_property.owner.name}.")

        # Handle special spaces
        if current_property.name == "Chance":
            # Implement Chance card logic
            pass
        elif current_property.name == "Community Chest":
            # Implement Community Chest card logic
            pass
        elif current_property.name == "Income Tax":
            player.money -= 200  # Pay $200 income tax
            print(f"{player.name} paid $200 in income tax.")
        elif current_property.name == "Luxury Tax":
            player.money -= 100  # Pay $100 luxury tax
            print(f"{player.name} paid $100 in luxury tax.")
        elif current_property.name == "Jail":
            print(f"{player.name} is just visiting Jail.")
        elif current_property.name == "Go to Jail":
            player.position = self.properties.index(next(p for p in self.properties if p.name == "Jail"))
            print(f"{player.name} goes to Jail.")
        elif current_property.name == "Free Parking":
            print(f"{player.name} is in Free Parking.")

        self.next_player()

    def start(self):
        while True:
            self.play_turn()
            self.next_player()


if __name__ == "__main__":
    num_players = int(input("Enter the number of players: "))
    starting_balances = [1500, 1500, 1500, 1500]  # Adjust starting balances as needed
    players = [Player(input(f"Enter player {i+1}'s name: "), starting_balances[i], []) for i in range(num_players)]
    game = MonopolyGame(players)
    game.start()
