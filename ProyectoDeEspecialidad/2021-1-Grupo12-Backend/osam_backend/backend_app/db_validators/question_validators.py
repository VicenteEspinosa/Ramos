from backend_app.db_models.question import Question
from backend_app.db_models.form_tree import FormTree


def validate_questions(question_json):
    """Validate if all the questions exists."""

    if len(question_json.keys()) == 1:
        if "question_ids" in question_json.keys():
            question_list = Question.objects.all()
            question_ids_list = [question.id for question in question_list]
            if isinstance(question_json["question_ids"], list):
                for x in question_json["question_ids"]:
                    if x not in question_ids_list:
                        return False
                return True
    return False


def validate_options(options_json):
    """Validate if the options are a list of strings."""

    if len(options_json.keys()) == 1:
        if "possible_values" in options_json.keys():
            if isinstance(options_json["possible_values"], list):
                for x in options_json["possible_values"]:
                    if type(x) != str:
                        return False
                return True
    return False


def check_questions_category(question_ids, category):
    """Checks if the questions are of the same category"""

    correct = True
    for question_id in question_ids:
        if Question.objects.get(id=question_id).category_id != category:
            correct = False
    return correct


def validate_question_category_exits(category):
    """Validate if the category exists in the form_tree"""

    categories = FormTree.objects.all().last().tree.keys()
    if str(category) in categories:
        return True
    return False


def validate_question_unique(category, value):
    """Validates if question value is unique"""
    questions = Question.objects.filter(category_id=category, value=value)
    if len(questions) > 0:
        return False
    return True


def validate_question_put_type(question, question_data):
    if question.category != question_data["category"]:
        if question.category in [0,1] and question_data["category"] in [0,1]:
            return True
        else:
            return False
    return True
