total_seconds = 8640000
word_day = ''

while total_seconds < 0 or total_seconds > 8639999:
    total_seconds = int(input('Please enter a number between 0 and 8639999 inclusive: '))

tuple_days_seconds = divmod(total_seconds, 24 * 60 * 60)
tuple_hours_seconds = divmod(tuple_days_seconds[-1], 60 * 60)
tuple_minutes_seconds = divmod(tuple_hours_seconds[-1], 60)

num_days = tuple_days_seconds[0]
num_hours = tuple_hours_seconds[0]
num_minutes = tuple_minutes_seconds[0]
num_seconds = tuple_minutes_seconds[-1]

electronic_times = '{}:{}:{}'.format(str(num_hours).zfill(2), str(num_minutes).zfill(2), str(num_seconds).zfill(2))

if 11 <= num_days % 100 <= 14:
    word_day = 'днів'
elif num_days % 10 == 1:
    word_day = 'день'
elif 2 <= num_days % 10 <= 4:
    word_day = 'дні'
else:
    word_day = 'днів'

###### First version of the output result ######
print(f'{total_seconds} -> {num_days} {word_day}, {electronic_times}')

###### Second version of the output result ######
# print(f'{total_seconds} sec -> {num_days} {word_day}, {num_hours:02}:{num_minutes:02}:{num_seconds:02}')
