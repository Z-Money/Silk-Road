import os
import random
import time

'''
 pygame.init()
 # Load the image
 img = pygame.image.load("images/caravan-screen.jpg")
 # Create the display surface
 screen_width = 400
 screen_height = 200
 screen = pygame.display.set_mode((screen_width,screen_height))
 # Resize the image to fit the display surface
 img = pygame.transform.scale(img, (screen_width,screen_height))
 # Display the image
 screen.blit(img, (0, 0))
 pygame.display.flip()
'''

food_num = 0
health_num = 0

print('Welcome to the Silk Roads!\n')

#asking name
easter_egg_names = ["marco polo", "ibn battuta", "genghis khan"]
player_name = input('Enter your name: ')
while len(player_name) >= 0:
  if (len(player_name) > 0) and (player_name.lower() not in easter_egg_names):
    print("\n" + str(player_name) + "? I've never heard that name on the Silk Roads before.\n")
    break
  elif len(player_name) > 0:
    break
  else:
    player_name = input()


mode_choice = ""
#easter eggs for names
if player_name.lower() == 'ibn battuta' or player_name.lower() == 'marco polo':
  year_set = 1300
  mode_choice = '3'
  print("\n" + str(player_name) + ", its such an honor to meet a traveler like you! Good luck on your travels!")
  time.sleep(2)
elif player_name.lower() == "genghis khan":
  print("Why are you on the Silk Roads? Shouldn't you be off killing people?")
  year_set = 1220
  mode_choice = "2"
  time.sleep(2)
else:
  year_set = input('Enter a year: ')
  if year_set.isdigit():
    return_num = 0
  else:
    return_num = 1
  while return_num == 1:
    print('Error, please try again!')
    year_set = input('Enter a year: ')
    if year_set.isdigit():
      return_num = 0
    else:
      return_num = 1
  year_set = int(year_set)
  #get VALID game mode choice
  while mode_choice == "":
    print('\nWhich mode do you want to play?')
    modes = ["Easy", "Normal", "Hard", "Impossible", "Customize"]
    for i in range(0, 5):
      print(str(i + 1) + ". " + modes[i])
    mode_choice = input("Type the number of the mode you want: ")
    if mode_choice.isdigit():
      if int(mode_choice) not in range(1,6):
        print("Thats not a valid option, try again!\n")
        mode_choice = ""
      else:
        break
    else:
      print("Thats not a valid option, try again!\n")
      mode_choice = ""

#set game mode
print()
if mode_choice == '1':
  food_num = 1000
  health_num = 10
  money_num = 1000
  print("You have been given " + str(food_num) + " food, " + str(health_num)+ " health, and " + str(money_num)+ " paper money.")
elif mode_choice == '2':
  food_num = 500
  health_num = 5
  money_num = 5
  print("You have been given " + str(food_num) + " food, " + str(health_num)+ " health, and " + str(money_num)+ " paper money.")
elif mode_choice == '3':
  food_num = 300
  health_num = 4
  money_num = 300
  print("You have been given " + str(food_num) + " food, " + str(health_num)+ " health, and " + str(money_num)+ " paper money.")
elif mode_choice == '4':
  food_num = 150
  health_num = 3
  money_num = 150
  print("You have been given " + str(food_num) + " food, " + str(health_num)+ " health, and " + str(money_num)+ " paper money.")
else:
  food_num = int(input('How much food do you want: '))
  health_num = int(input('How much health do you want: '))
  money_num = int(input('How much money do you want: '))
input('\nPress enter to continue')
os.system('clear')


#other basic strating value setting
player_move_distance = 0
month_num = 1
days_pass = 1
total_days = 0
MONTHS_WITH_31_DAYS = [1, 3, 5, 7, 8, 10, 12]
random_result = 0
accident_appear = random.randint(1, 30)
travel_total_num = 0
rest_total_num = 0
hunt_total_num = 0
status_total_num = 0
month_appear = 'March'
camel_num = 0
ammo_num = 0
stops = ["", "Bukhara", "Samarkand", "Kashgar"]

#add days:
def add_days(min, max, safe):
  global days_pass, month_num, MONTHS_WITH_31_DAYS, random_result, money_num, food_num, camel_num, health_num, total_days, accident_appear, ammo_num, player_move_distance
  
  random_result = random.randint(min, max)
  print(random_result, "days have passed.")
  days_pass_min = days_pass
  check_big = days_pass + random_result
  time.sleep(1)

  #accident
  if not safe:
    if accident_appear >= days_pass and accident_appear <= check_big:
      a_number = random.randint(1, 3)
      a_health_num = random.randint(1, 2)
      injury = random.randint(1, 5)
      if a_number == 1 and random.randint(1,3) == 1 and camel_num > 0:
        print('During this time, you crossed a river.')
        print("You lost 1 camel.")
        camel_num -= 1
      else:
        a_number = random.randint(2, 3)
      if a_number == 2:
        print('During this time, you had a dysentery.')
        health_lost = random.randint(3,5)
        print('You lost ' + str(health_lost) + ' health.')
        health_num -= health_lost
      if a_number == 3:
        print('During this time, you stayed in a caravanserai and learned about other cultures.')
        random_result2_food = random.randint(3, 10)
        random_result2_day = random.randint(3, 8)
        print('As a result, you eat ' + str(random_result2_food) +
              ' lbs extra food.')
        print('It also took up extra ' + str(random_result2_day) + ' days.')
        food_num -= random_result2_food + random_result2_day * 5
        days_pass += random_result2_day
        total_days += random_result2_day
      if a_health_num == 1 and a_number != 2:
        if injury == 1:
          print('\nYou stub your toe and lose 1 health')
          health_num -= 1
        elif injury == 2:
          print('\nYou get a cold and lose 1 health')
          health_num -= 1
        else:
          money_gone = random.randint(0, money_num)
          #camel_gone = min(1, camel_num)
          camel_gone = 0
          if camel_num > 0:
            camel_gone = 1
          ammo_gone = random.randint(0, ammo_num)
          print('\nYou got robbed and lose ' + str(money_gone) + " money, " + str(camel_gone) + " camel, and " + str(ammo_gone) + " ammo.\n")
          print('The robber also broke your arm and you lose 1 health.')
          health_num -= 1
          money_num -= money_gone
          camel_num -= camel_gone
          ammo_num -= ammo_gone
    print()
    
  nextStop(player_move_distance)
  days_pass += random_result
  total_days += random_result
  food_num -= random_result * 5
  if days_pass >= 30:
    if month_num not in MONTHS_WITH_31_DAYS:
      if days_pass > 30:
        days_pass -= 30
        month_num += 1
        accident_appear == random.randint(1, 30)
    else:
      if days_pass > 31:
        days_pass -= 31
        month_num += 1
        accident_appear == random.randint(1, 30)

#functions
def travel1(movedistance):
  global travel_total_num
  add_days(3, 7, False)
  move_change = random.randint(40, 60)
  if movedistance >= 2240 and movedistance < 2300:
    move_change = 2300 - movedistance
  elif movedistance >= 2540 and movedistance < 2600:
    move_change = 2600 - movedistance
  elif movedistance >= 2740 and movedistance < 2800:
    move_change = 2800 - movedistance
  elif movedistance >= 2940 and movedistance < 3000:
    move_change = 3000 - movedistance
  movedistance += move_change
  print("You traveled " + str(move_change) + " miles.")
  travel_total_num += 1
  input('\nPress enter to continue')
  return movedistance


def rest(health):
  global rest_total_num
  add_days(1, 3, True)
  health = health + 1
  rest_total_num += 1
  return health


def hunt(hunting_food):
  global hunt_total_num, ammo_num
  print("\nAmmo: " + str(ammo_num))
  if ammo_num < 5:
    print("You must have at least 5 ammo to hunt.")
    input('\nPress enter to continue')
    return hunting_food
  ammo_used = int(input("How much ammo do you want to use (5, 10, 25): "))
  while ammo_used != 5 and ammo_used != 10 and ammo_used != 25:
    print("That is not a valid amount.")
    ammo_used = int(input("How much ammo do you want to use (5, 10, 25): "))
  if ammo_used == 5:
    hunting_food += 50
    ammo_num -= 5
    print('Gain: 50 lbs food')
    hunt_total_num += 1
    add_days(1, 3, True)
  elif ammo_used == 10:
    hunting_food += 100
    ammo_num -= 10
    print('Gain: 100 lbs food')
    hunt_total_num += 1
    add_days(1, 4, True)
  elif ammo_used == 25:
    hunting_food += 200
    ammo_num -= 25
    print('Gain: 200 lbs food')
    hunt_total_num += 1
    add_days(2, 5, True)
  input('\nPress enter to continue')
  return hunting_food

#check distance to next stop
def nextStop(dist):
  if dist >= 2240 and dist < 2300:
    print("You are close to the next stop: Bukhara\n")
  elif dist >= 2540 and dist < 2600:
    print("You are close to the next stop: Samarkand\n")
  elif dist >= 2740 and dist < 2800:
    print("You are close to the next stop: Kashgar\n")
  elif dist >= 2940 and dist < 3000:
    print("You are close to the final destination: Karakorum\n")

#plaza to buy items
def shop(stop):
  global food_num, money_num, camel_num, ammo_num, stops
  if stop == 0:
    print("Welcome to the Silk Road Shop! Here you can buy items prior to starting your journey!")
    print("We suggest having 4 camels, 100 ammo, and 500 food to start off your journey.")
  else:
    print("Welcome to the merchant plaza at " + stops[stop] + "!")
  print("\nYour inventory: ")
  print("Money: " + str(money_num) + " paper bills")
  print("Food: " + str(food_num))
  print("Camels: " + str(camel_num))
  print("Ammo: " + str(ammo_num) + "\n")
  merchants = ["Food", "Camels", "Ammo", "Leave"]
  for i in merchants:
    print("-" + i)
  merchant_choice = input("What do you want to purchase: ")
  if (merchant_choice.isdigit()) or (merchant_choice.capitalize() not in merchants):
    print("Thats not a valid choice, try again!")
    time.sleep(2)
    os.system('clear')
    shop(stop)
  else:
    print()
    merchant_choice = merchant_choice.lower()
    match merchant_choice:
      case "food":
        print("Food cost 1 paper bill per pound.")
        buy_temp = int(input("How much do you want to buy: "))
        credit = checkBalance(buy_temp)
        if credit == 1:
          food_num += buy_temp
          money_num -= buy_temp
          print("You have bought " + str(buy_temp) + " food")
        time.sleep(3)
        os.system('clear')
        shop(stop)
      case "camels":
        print("Camels cost 200 paper bills each.")
        buy_temp = int(input("How many do you want to buy: "))
        credit = checkBalance(buy_temp*200)
        if credit == 1:
          camel_num += buy_temp
          money_num -= buy_temp*200
          print("You have bought " + str(buy_temp) + " camels")
        time.sleep(3)
        os.system('clear')
        shop(stop)
      case "ammo":
        print("Ammo cost 2 paper bills per bullet.")
        buy_temp = int(input("How many do you want to buy: "))
        credit = checkBalance(buy_temp*2)
        if credit == 1:
          ammo_num += buy_temp
          money_num -= buy_temp*2
          print("You have bought " + str(buy_temp) + " ammo")
        time.sleep(3)
        os.system('clear')
        shop(stop)
      case "leave":
        print("Thanks for shopping!")
        time.sleep(2)
        os.system("clear")

#check balance prior to paying
def checkBalance(cost):
  global money_num
  if cost > money_num:
    print("Thats too expensive, try again!")
    time.sleep(2)
    return 0
  else:
    return 1

#month_appear
def month_appear_fun():
  global month_appear, month_num
  if month_num > 12:
    month_num -= 12
  match month_num:
    case 1:
      month_appear = 'January'
    case 2:
      month_appear = 'February'
    case 3:
      month_appear = 'March'
    case 4:
      month_appear = 'April'
    case 5:
      month_appear = 'May'
    case 6:
      month_appear = 'June'
    case 7:
      month_appear = 'July'
    case 8:
      month_appear = 'August'
    case 9:
      month_appear = 'September'
    case 10:
      month_appear = 'October'
    case 11:
      month_appear = 'November'
    case 12:
      month_appear = 'December'
  return month_appear

def checkStop(distance):
  match distance:
    case 2300:
      print('You\'ve made it to Bukhara! The next stop is Samarkand.')
      shop(1)
    case 2600:
      print('You\'ve made it to Samarkand! The next stop is Kashgar.')
      shop(2)
    case 2800:
      print('You\'ve made it to Kashgar! The next stop is China.')
      shop(3)


#loading part
'''
os.system('clear')
print('Now Loding...')
time.sleep(0.5)
print('Now loading the player setting...')
time.sleep(2)
print('Successfully!')
time.sleep(0.5)
print('Now loading the game setting...')
time.sleep(2)
print('Successfully!')
time.sleep(0.5)
print('Prepearing the trip for Karakorum...')
time.sleep(2)
print('Successfully!')
time.sleep(0.5)
print('Now game is ready!')
time.sleep(1)
os.system('clear')
'''
shop(0)
print('Attention:')
print('Welcome to the Silk Roads! The goal is to travel from Constantinople to China (3000 miles). However, the trail is arduous. Each day costs you food and health. You can hunt and rest, but make sure you watch out for thieves. GOOD LUCK!\n')

#main
while player_move_distance < 3000 and food_num > 0 and health_num > 0:
  os.system('clear')
  checkStop(player_move_distance)
  month_appear_fun()
  if food_num <= 0:
    print('You run out of food and starve to death.')
    break
  if food_num <= 50:
    print('Warning! You only have ' + str(food_num) + " pounds of food left.")
  if health_num <= 0:
    print('You run out of health and die.')
    break
  if health_num <= 2:
    print('Warning! You only have ' + str(health_num) + " health left.")
  print(str(player_name) + ', now it is ' + month_appear + ' ' + str(days_pass) + ', ' + str(year_set) + ", and you have travled " + str(player_move_distance) + " miles.")
  menuOptions = ["Travel", "Rest", "Hunt", "Status", "Help", "Quit"]
  menuOptionNums = [1, 2, 3, 4, 5, 6]
  for i in menuOptions:
    print("-" + i)
  choice = input('Your choice: ').lower()
  #travel
  if choice == 'travel':
    player_move_distance = travel1(player_move_distance)
  #rest
  elif choice == 'rest':
    if health_num < 10:
      print("You get 1 heath!")
      health_num = rest(health_num)
    else:
      print("Your health is full, the maximum number for health is 10!")
    input('\nPress enter to continue')
    
  #hunt
  elif choice == 'hunt':
    food_num = hunt(food_num)
  #status
  elif choice == 'status':
    print('\n' + str(player_name) + ', it is ' + str(month_num) + '/' +
          str(days_pass) + '/' + str(year_set) + ".")
    print('-Food:', food_num, "lbs")
    print('-Health: ' + str(health_num) + '/10')
    print('-Paper Money:', money_num)
    print('-Camels:', camel_num)
    print('-Distance traveled:', player_move_distance, 'miles')
    distance_left = 3000 - player_move_distance
    print('-Distance remaining: ' + str(distance_left) + ' miles left.')
    print('-' + str(total_days) + ' days have passed.')
    status_total_num += 1
    input("\nPress enter to continue")
  #help
  elif choice == 'help':
    print('\n[travel]: moves you randomly between 40-60 miles and takes 3-7 days (random).')
    print('[rest]: increases health by 1 and takes 1-3 days (random).')
    print('[hunt]: adds 100 lbs of food and takes 2-5 days (random).')
    print('[status]: lists food, health, money, distance traveled, and day.')
    print('[quit]: will end the game.')
    input('\nPress enter to continue')
  #quit
  elif choice == 'quit':
    quit_choice = input('Are you sure that you want to quit? (y/n) ')
    if quit_choice == 'y':
      os.system("clear")
      print('Game over...I cannot believe that you quit...')
      break
  #suicide
  elif choice == 'suicide':
    quit_choice = input('Are you sure? (y/n) ')
    if quit_choice == 'n':
      continue
    os.system("clear")
    print('Game over...You kill youslf...\n')
    break
  #lobotomy
  elif choice == 'lobotomy':
    quit_choice = input('Are you sure? (y/n) ')
    if quit_choice == 'n':
      continue
    os.system("clear")
    print('Game over...You lobotomized yourself...')
    break
  elif choice == 'skip':
    player_move_distance = 2000
  #invalid input
  else:
    print("This choice is not available, please try again.")
    time.sleep(2)
  os.system("clear")

#succeed!
if player_move_distance >= 3000:
  print('Nice job! You have arrived in China in ' + str(total_days) + ' days!\n')

#game over
if food_num <= 0:
  print('Game over, you are out of food.')

if health_num <= 0:
  print('Game over, you ran out of health.')

print('\nDuring the whole game, you:')
print('Travel ' + str(travel_total_num) + ' times.')
print('Rest ' + str(rest_total_num) + ' times.')
print('Had ' + str(money_num) + ' pieces of paper money')
print('Hunt ' + str(hunt_total_num) + ' times.')
print('Status ' + str(status_total_num) + ' times.')
print('\nAuthors: Zachariah Kersery and Gavin Moore')
print('Thanks for playing!')