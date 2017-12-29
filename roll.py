import random
import argparse

def main():
	parser = argparse.ArgumentParser(description='let\'s roll some dice!')

	parser.add_argument(
        '-r', '--roll', required=True,
        help='dice + modifiers to roll')

	args = parser.parse_args()

	roll = args.roll

	print('rolling {}...'.format(roll))

	result = roll_dice(roll)

	print('\033[1mresult: \033[92m{}'.format(result))

# roll dice by: (multiplier * dice) + modifier
def roll_dice(roll):
	parsed_roll = roll.split('d')

	multiplier = int(parsed_roll[0])

	# if there's a modififer, split the parsed_roll into dice + mod
	if '+' in parsed_roll[1]:
		dice_and_modifier = parsed_roll[1].split('+')
		
		dice = int(dice_and_modifier[0])
		modifier = int(dice_and_modifier[1])

	else:
		dice = int(parsed_roll[1])
		modifier = 0

	# roll the dice
	dice_roll = 0

	print('rolls: ', end='')
	for number_of_dice in range(1,multiplier+1):
		roll = random.randint(1,dice)
		print('{}'.format(roll), end=' + ')
		dice_roll += roll
		
	result = dice_roll + modifier
	print('{}'.format(modifier))

	return result
	

if __name__ == '__main__':
    main()