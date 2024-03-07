import datetime, random

def getBirthdays(numBirthdays):
    '''Returns a list of numBirthdays random date objects for birthdays'''
    birthdays = []
    for i in range(numBirthdays):
        # Here, the year is unimportant for our simulation
        startOfYear = datetime.date(2001,1,1)
        # Get a random day into the year
        randomNumberOfDays = datetime.timedelta(random.randint(0,364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays
# print info
print('''
    The birthday paradox shows us that in a group of N people,
    the odds that two people share the same birthday are surprisingly large.
    This program does a Monte Carlo simulation, i.e. repeated random simulations
    to explore this concept. It's not actually a paradox, it's just a surprising result.
''')

# Set up a tuple of month names in order
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

# Keep asking until the user enters a valid amount
while True:
    print('How many birthdays shall I generate? (Max 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBirthdays = int(response)
        break # User has entered a valid amount
print()

# Generate and display the birthdays
print('Here are {} birthdays'.format(numBirthdays))
birthdays = getBirthdays(numBirthdays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        # Display a comma for each birthday after the first birthday
        print(', ', end='')  
    monthName = MONTHS[birthday.month - 1]
    dateText = '{} {}'.format(monthName, birthday.day)
    print(dateText, end='')
print()
print()                              

