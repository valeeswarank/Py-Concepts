from functools import reduce

employees = [{
    "name": "valee",
    "salary": 90000,
    "job_title": "developer"
},{
    "name": "rishi",
    "salary": 100000,
    "job_title": "developer"
},{
    "name": "bhuvana",
    "salary": 87000,
    "job_title": "executive"
},{
    "name": "vaishu",
    "salary": 50000,
    "job_title": "writter"
}
]


def is_developer(employee):
    return employee["job_title"] == "developer"


def is_not_developer(employee):
    return employee["job_title"] != "developer"


developers = [x for x in employees if is_developer(x)]
non_developers = [x for x in employees if is_not_developer(x)]


def get_salary(employee):
    return employee["salary"]

developer_salaries = [get_salary(x) for x in developers]
non_developers_salaries = [get_salary(x) for x in non_developers]

def get_sum(acc, x):
    return acc + x

total_developer_slaries = reduce(get_sum, developer_salaries)
average_developer_salaries = total_developer_slaries / len(developers)

total_non_developer_salaries = reduce(get_sum, non_developers_salaries)