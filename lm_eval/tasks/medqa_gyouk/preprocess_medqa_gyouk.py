def doc_to_text(doc) -> str:
    option_choices = {
        "A": doc["options"]["A"],
        "B": doc["options"]["B"],
        "C": doc["options"]["C"],
        "D": doc["options"]["D"],
    }
    answers = "".join((f"{k}. {v}\n") for k, v in option_choices.items())
    return f"Question: {doc['question']}\n{answers}Answer:"


def doc_to_target(doc) -> int:
    if doc['answer_idx']=="A":
        return 0
    elif doc['answer_idx']=="B":
        return 1
    elif doc['answer_idx']=="C":
        return 2
    else:
        return 3
