import os
import sys

# AUTHOR Kim Nikita 381908-1

############ CONSTANTS
# ONLINE
STUD_PER_GROUP = ('12', '22') # кол-во студентов в группе 12 или 22
PREPOD_SALARY = 35000  # руб
NALOG_NA_TRUD = 0.3  # начисления на оплату труда 30%
NDS = 0.13  # подоходный налог 13%
INTERNET = 10000  # руб за интернет
C1 = 15000  # руб 1C
#

# OFFLINE
SQUARE_PER_PREPOD = 4  # 4 кв. м. на препода
SQARE_PER_STUD = 2  # 1 кв. м. на человека и 1 кв. м. на окружение
SQUARE_COMM = 40  # 2 * 20 кв. м. общих комнат
RENT = 500  # 500 руб за кв. м. за помещения
COMMUNAL = 100  # 100 руб за кв. м. за коммунальные услуги
OTHERS_ROOMS = 0.02  # 2% на коридоры туалет и тд
#
############

# AVERAGE SALARIES в рублях
average_salaries = {
    'online': {
        'buh': 100000,  # 2 * 50000 бухгалтеры
        'sys_admin': 60000,  # сисадмин
        'met': 70000  # 2 * 35000 методисты
    },
    'offline': {
        'sequrity': 160000,  # 4 * 40000 охранники
        'cleaner': 40000,  # 2 * 20000 уборщицы
        'cloackroomer': 30000  # 2 * 15000 гардеробщицы
    }
}

# 6 - ти дневная рабочая неделя
# каждый препод ведет максимум 3 предмета
# 1 препод ведет 10 пар в неделю
# каждый препод ведет 2 пары в день
# 1 курс - 3 пары каждый день, 9 предметов в год
# 2 курс - 4, 13
# 3 курс - 3, 10
# 4 курс - 3, 12
# 4 группы в каждом курсе
# в среднем 2 группы у каждого препода на паре
# 1 курс - нужно 3*2=6 преподов
# 2 курс - 4*2=8
# 3 курс - 3*2=6
# 4 курс - 4*2=8
# Всего преподов:
num_prep = 30
# Всего студентов одновременно на парах в 1 день:
# (среднее кол-во человек в группе на 1 курсе + на втором + на 3 + на 4) * 2
num_stud_per_day_in_week = 0
num_stud = 0
studs = []

def main():
    global num_prep, num_stud_per_day_in_week, num_stud, studs
    ONLINE = (INTERNET + C1) * 12
    
    for key in average_salaries['online'].keys():
        ONLINE += average_salaries['online'][key] * 12 * (1 + NALOG_NA_TRUD) * (1 + NDS)
    OFFLINE = ONLINE
    for key in average_salaries['offline'].keys():
        OFFLINE += average_salaries['offline'][key] * 12 * (1 + NALOG_NA_TRUD) * (1 + NDS)

    with open(os.path.abspath('') + '\students.txt', 'r') as f:
        for i in range(4):
            studs.append(f.readline().split('\n')[0].split(':')[1][1:].split(' '))

        for i in range(4):
            average = 0
            for j in range(4):
                if studs[i][j] not in STUD_PER_GROUP:
                    raise ValueError('Number of students per group must be 12 or 22')
                num_stud += int(studs[i][j])
                average += int(studs[i][j])
            num_stud_per_day_in_week += average//4 * 2

    ONLINE += num_prep * PREPOD_SALARY * 12 * (1 + NALOG_NA_TRUD) * (1 + NDS)
    OFFLINE += num_prep * PREPOD_SALARY * 12 * (1 + NALOG_NA_TRUD) * (1 + NDS)
    OFFLINE += (num_stud_per_day_in_week * SQARE_PER_STUD + num_prep *
                SQUARE_PER_PREPOD + SQUARE_COMM) * (RENT + COMMUNAL) * (1 + OTHERS_ROOMS) * 12
 
    print('Стоимость онлайн обучения на 1 студента за 1 год: ' + str(ONLINE//num_stud) + ' рублей')
    print('Стоимость офлайн обучения на 1 студента за 1 год: ' + str(OFFLINE//num_stud) + ' рублей')


if __name__ == '__main__':
    sys.exit(main() or 0)
