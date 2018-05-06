import datetime

def print_header():
  print('--------------------------------------')
  print('           BIRTHDAY APP')
  print('--------------------------------------')
  print()

def get_birthday_from_user():
  print('When were you born?')
  year = int(input('Year [YYYY]: '))
  month = int(input('Month [MM]: '))
  day = int(input('Day [DD]: '))
  birthday = datetime.date(year, month, day)
  return birthday



def compute_days_between_date():
  pass


def print_bday_info():
  pass


def main():
  print_header()
  bday = get_birthday_from_user()
  print(bday)
  now = None
  number_of_days = compute_days_between_date(bday, now)
  print_bday_info(number_of_days)

main()