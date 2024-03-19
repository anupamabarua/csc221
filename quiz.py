#!/usr/bin/env python3
#
# Custom script to generate random DJ4E groups
#
import os
import sys
import random

sections = {
    'P4': {
        'Section': 'Period 4',
        'SysAdmins': ['Toby', 'Alex', 'Blu', 'Jack'],
        'PCEPers': ['Abi', 'Alessandra', 'Grant', 'Jake', 'Noah', 'Conrad'],
        'Students': ['Anupama', 'Erica', 'Amelie', 'Adrian', 'Kiersten']
    },
    'P5': {
        'Section': 'Period 5',
        'SysAdmins': ['Luka', 'Mayah', 'Gabriel', 'Evan'],
        'PCEPers': ['Colin', 'Sam', 'Rockwell', 'Donovan'],
        'Students': ['Dylan', 'Sean', 'Yuri', 'Timh', 'Udval', 'Daniel',
                     'Jonathan', 'Fatima']
    }
}


def choose_groups(period):
    groups = {}
    groups['section'] = period['Section'] 
    people = period.copy()
    for gnum in range(1, 5):
        group = 'group' + str(gnum)
        groups[group] = []
        # select a sysadmin
        sysadmin = random.choice(people['SysAdmins'])
        groups[group].append(sysadmin)
        people['SysAdmins'].remove(sysadmin)
        # select another PCEPer 
        pceper = random.choice(people['PCEPers'])
        groups[group].append(pceper)
        people['PCEPers'].remove(pceper)
        while len(groups[group]) < 4:
            if people['Students']:
                student = random.choice(people['Students'])
                groups[group].append(student)
                people['Students'].remove(student)
            elif people['PCEPers']:
                student = random.choice(people['PCEPers'])
                groups[group].append(student)
                people['PCEPers'].remove(student)
            else:
                break

    return groups


def pretty_print_groups(groups):
    idnt1, idnt2 = 6 * ' ', 11 * ' '
    os.system('clear')
    print(f"\n\n\n{idnt1}DJ4E Groups for {groups['section']}:\n")
    for i in range(1, 5):
        print(f"{idnt2}Group {i}: {', '.join(groups['group' + str(i)])}")
    indent = 6 * ' '
    print(10 * '\n')
    input(f"{idnt1}Press the Enter key to exit... ")
    os.system('clear')


if __name__ == '__main__':
    if len(sys.argv) != 2 or not sys.argv[1] in ['P4', 'P5']:
        print("Invalid input. Usage: choose P4 or P5.")
        exit()
    pretty_print_groups(choose_groups(sections[sys.argv[1]]))
