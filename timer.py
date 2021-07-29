from time import sleep

timer = 5
print('Loading')

while timer > 0:
    print('.', end=' ', flush=True)
    sleep(1)
    timer -= 1

print('Complete!')

