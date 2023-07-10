# Joshua Soto
# 1553869

player_dict = {}

i = 1

count = 1

# Allows 6 inputs with limits in rating and player number
# If input is outside of limits they are told so and prompted to try again
for i in range(1, 6):
    jersey_number = int(input('Enter player {}\'s jersey number:\n'.format(i)))
    rating = int(input('Enter player {}\'s rating:\n'.format(i)))
    print()

    if 0 > jersey_number > 99 and 0 > rating > 9:
        print('Entry is invalid, try again')
        break
    else:
        player_dict[jersey_number] = rating

# Prints roster's player numbers and rating
print("ROSTER")

for jersey_number, rating in sorted(player_dict.items()):
    print("Jersey number: %d, Rating: %d" % (jersey_number, rating))

option = ''

while option.upper() != 'Q':

    # Outputs menu that allows for edits in player_dict

    print('\nMENU\na - Add player\nd - Remove player\nu - Update player rating\n'
          'r - Output players above a rating\no - Output roster\nq - Quit\n')

    option = input('Choose an option:\n')

    # Appends player_dict to add another player.
    if option == 'a':
        jersey_number = int(input('Enter a new player\'s jersey number:\n'.format(i)))
        rating = int(input('Enter the players\'s rating:\n'.format(i)))
        player_dict[jersey_number] = rating

    # Deletes a player number and rating from player_dict
    elif option == 'd':
        jersey_number = int(input('Enter a jersey number:\n'))
        if jersey_number in player_dict.keys():
            del player_dict[jersey_number]

    # Edits a player's number and rating
    elif option == 'u':
        jersey_number = int(input('Enter a jersey number:\n'))
        if jersey_number in player_dict.keys():
            rating = int(input('Enter a new rating for player:\n'))
            player_dict[jersey_number] = rating

    # Shows which players are above a rating threshold
    elif option == 'r':
        rating_input = int(input('Enter a rating:\n'))

        print('ABOVE {}'.format(rating_input))
        for jersey_number, rating in sorted(player_dict.items()):
            if rating > rating_input:
                print("Jersey number: %d, Rating: %d" % (jersey_number, rating))

    # Shows the entire player roster
    elif option == 'o':
        print("ROSTER")
        for jersey_number, rating in sorted(player_dict.items()):
            print("Jersey number: %d, Rating: %d" % (jersey_number, rating))
