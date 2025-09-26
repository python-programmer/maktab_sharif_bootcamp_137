import itertools

# counter = itertools.count(1, 3)


# for index in range(10):
#     print(next(counter))


# from itertools import groupby

# students = [
#  {'name': 'Ali', 'grade': 'A'},
#  {'name': 'Reza', 'grade': 'B'},
#  {'name': 'Sara', 'grade': 'A'},
#  {'name': 'Maryam', 'grade': 'C'},
#  {'name': 'Mohammad', 'grade': 'B'},
# ]

# students.sort(key=lambda student: student['grade'])

# print("Grouping student(by grade)".center(50, '-'))
# for grade, group in groupby(students, key=lambda x: x['grade']):
#     print(f"Grade {grade}: {[student['name'] for student in group]}")


import itertools
premier_league_teams: list[str] = [
    "Arsenal",
    "Aston Villa",
    "Bournemouth",
    "Brentford",
    "Brighton & Hove Albion",
    "Chelsea",
    "Crystal Palace",
    "Everton",
    "Fulham",
    "Liverpool",
    "Luton Town",
    "Manchester City",
    "Manchester United",
    "Newcastle United",
    "Nottingham Forest",
    "Sheffield United",
    "Tottenham Hotspur",
    "West Ham United",
    "Wolverhampton Wanderers",
    "Burnley"
]
matches = itertools.permutations(premier_league_teams, 2)
# print(f"Total Matches: {len(list(matches))}") ???
print("Premier League Matches".center(50, "-"))
for match in matches:
    print(f"{match[0]} - {match[1]}")
# print(f"Total Matches: {len(list(matches))}") ???

# [{"name": "Arsenal", "points": 0, "matches": 0}]
# input for points => Arsenal 2 - Aston villa 1