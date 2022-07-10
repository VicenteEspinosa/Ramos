from backend_app.db_models.question import Question
from backend_app.db_models.block import Block


def get_values_header(question_ids, is_enumerated, report):
    """Returns the questions names."""

    values_header = []

    if is_enumerated:
        if report.question_based:
            for index, id_question in enumerate(question_ids):
                try:
                    values_header.append("{}. ".format(index + 1)+Question.objects.get(id=id_question).value)
                except Question.DoesNotExist:
                    values_header.append("{}. ERROR".format(index + 1))
        else:
            block_list_len = []
            for block_id in report.blocks["block_ids"]:
                block_list_len.append(len(Block.objects.get(id=int(block_id)).questions["question_ids"]))
            for length in block_list_len:
                for i in range(length):
                    try:
                        values_header.append("{}. ".format(i + 1)+Question.objects.get(id=question_ids[i]).value)
                    except Question.DoesNotExist:
                        values_header.append("{}. ERROR".format(i + 1))
    else:
        for id_question in question_ids:
            try:
                values_header.append(Question.objects.get(id=id_question).value)
            except Question.DoesNotExist:
                values_header.append("ERROR")
    return values_header


def get_values_header_auto(question_ids):
    """Returns the questions names."""

    values_header = []
    for id_question in question_ids:
        try:
            values_header.append(Question.objects.get(id=id_question).value)
        except Question.DoesNotExist:
            values_header.append("ERROR")
    return values_header


def get_question_ids(report):
    """Returns the questions ids."""

    question_ids = []
    if report.question_based:
        question_ids = [question.id for question in Question.objects.filter(category__lt=5, category_id=report.category, status=True)]
    else:
        question_ids = []
        for block_id in report.blocks["block_ids"]:
            for question_id in Block.objects.get(id=block_id).questions["question_ids"]:
                question_ids.append(question_id)
    return question_ids
