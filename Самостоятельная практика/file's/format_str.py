team1_num = 5
print('В команде Мастера кода участников: %d' % (team1_num),'!')
team2_num = 6
print('Итого сегодня в командах участников: %d и %d!' % (team1_num, team2_num))
score_2 =42
print('Команда Волшебники данных решила задач "{}!"'.format(score_2))
team1_time = 18015.2
team2_time = 1000.12
print('Волшебники данных решили задачи за "{}!"'.format(team1_time),'!')
score_1 = 40
score_2 = 42
print(f'Команды решили {score_1 } и {score_2} задач')
challenge_result = 'Мастер кода!'
print(f'Результат битвы: победа команды {challenge_result}')
tasks_total = 82
time_avg = 350.4
print(f'Сегодня было решено {tasks_total} задач, в среднем поратили {time_avg} секунды на задачу!')
team2_name = f'Волшебники данных'
def quest_1():
    for i in range(1):
        if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
            print(f'Победа команды {challenge_result}')
        elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
            print(f'Победа команды {team2_name}')
        else:
            print("Ничья ")
quest_1()