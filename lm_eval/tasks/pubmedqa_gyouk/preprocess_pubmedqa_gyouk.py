def doc_to_text(doc) -> str:
    ctxs = "\n".join(doc["CONTEXTS"])
    return "개요: {}\n문제: {}\n정답:".format(
        ctxs,
        doc["QUESTION"],
    )
