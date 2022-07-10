from backend_app.db_models.block import Block
from backend_app.db_models.form_tree import FormTree


def validate_blocks_answer(blocks_data):
    """Validate al the blocks answers."""

    if type(blocks_data) != list:
        return False 
    for block in blocks_data:
        if not validate_block(block):
            return False
    return True


def validate_block(block):
    """Validate if the current block has all the questions."""

    if type(block) != dict:
        return False 
    keys = block.keys()
    if len(keys) != 2:
        return False
    for key in keys:
        value = block[key]
        if key == "block_name":
            if type(value) != str:
                return False
        elif key == "questions":
            if type(value) != list:
                return False 
            for question in value:
                if type(question) != int:
                    return False
    return True


def validate_blocks_report(blocks_json):
    """Validate all the blocks that go into a report exist."""

    if len(blocks_json.keys()) == 1:
        if "block_ids" in blocks_json.keys():
            block_list = Block.objects.all()
            block_ids_list = [block.id for block in block_list]
            if isinstance(blocks_json["block_ids"], list):
                for x in blocks_json["block_ids"]:
                    if x not in block_ids_list:
                        return False
                return True
    return False


def validate_blocks_are_for_report(block_ids):
    """Validates that the only blocks for a report have for_form:false"""
    
    correct = True
    for block_id in block_ids:
        if Block.objects.get(id=block_id).for_form == True:
            correct = False
    return correct


def check_blocks_category(block_ids, category):
    """Checks if the blocks are of the same category"""

    correct = True
    for block_id in block_ids:
        if str(Block.objects.get(id=block_id).category) != category:
            correct = False
    return correct


def check_block_dependencies(question):
    """Checks if question belong to any block."""

    allowed_to_delete = True
    block_dependency_list = []
    blocks = Block.objects.all()
    for block in blocks:
        if question.id in block.questions["question_ids"]:
            allowed_to_delete = False
            block_dependency_list.append({"id": block.id, "name": block.name})
    return (block_dependency_list, allowed_to_delete)


def validate_block_category_exits(category):
    """Validate if the category exists in the form_tree"""

    categories = FormTree.objects.all().last().tree.keys()
    if str(category) in categories:
        return True
    return False

def validate_anwers_unique(answers):
    set_answer = set(answers)
    return len(answers) == len(set_answer)
