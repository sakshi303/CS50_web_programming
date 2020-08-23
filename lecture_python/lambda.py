people = [
    {"name":"hannah", "squad":"elite"},
    {"name":"lottie","squad":"top"},
    {"name":"olivia","squad":"gold"}
]

people.sort(key=lambda person: person["squad"])

print(people)
