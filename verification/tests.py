"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ['hi'],
            "answer": 0,
        },
        {
            "input": ['who is 1st here'],
            "answer": 0,
        },
        {
            "input": ['my numbers is 2'],
            "answer": 2,
        },
        {
            "input": ['This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year'],
            "answer": 3755,
        },
        {
            "input": ['5 plus 6 is'],
            "answer": 11,
        },
        {
            "input": [''],
            "answer": 0,
        },
    ],
    "Extra": [
        {
            "input": ['It is the natural number following 4 and preceding 6  and is a prime number'],
            "answer": 10,
        },
    ]
}
