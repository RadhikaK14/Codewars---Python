# def multi_table(number):
#     for i in range(1,11):
#         answer = i*number
#         print(f'{i} * {number} = {answer}')
#         if i<10:
#             print()

# kata accepted solution 
# def multi_table(number):
#     y = ''
#     for i in range(1,11):
#         answer = i*number
#         x = '{}*{}={}'.format(i, number, answer)
#         if i <10:
#             x+='\n'
#         y = y + x
#     return y

# alternate solution

def multi_table(number):
    return '\n'.join(f'{i} * {number} = {i * number}' for i in range(1, 11))

table = multi_table(5)
print(table)

