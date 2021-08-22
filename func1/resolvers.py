QUESTIONS = {
    "segment": 4,
    "org_size": 5,
    "sec_department": 6,
    "web": 8,
    "sql": 9,
    "storage": 10,
    "cloud": 11,
    "containers": 12,
    "iot": 13,
    "industrial": 14,
    "internet_exposed": 16,
    "top_concern": 18,
    "top_impact": 20,
    "sensitivity": 22
}

# The function returns the answer of the question q
def get_answer(q, content):
    question_id = QUESTIONS[q]
    question_str = str(question_id)

    if (question_id < 10):
        question_str = "0" + question_str

    return content[[k for k in content.keys() if k.startswith(question_str)][0]]
