from backend_app.db_models.form_tree import FormTree
from backend_app.db_constants.filters import FILTERS
from backend_app.db_models.block import Block


def validate_blocks_form(blocks_json):
    """Validate the blocks in a form."""

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


def validate_tree_path(form_json):
    """Validate the form tree path asociated to a from."""

    form_tree = FormTree.objects.all().last()
    category_keys = list(form_tree.tree.keys())
    if form_json["category"] in category_keys:
        category_tree = form_tree.tree[form_json["category"]]
        category_levels = category_tree["levels"]
        audit_type_keys = list(category_tree[FILTERS[0]].keys())
        if form_json["audit_type"] in audit_type_keys:
            audit_tree = category_tree[FILTERS[0]][form_json["audit_type"]]
            audit_levels = category_levels - 1
            if audit_levels == 0:
                return True
            else:
                service_keys = list(audit_tree[FILTERS[1]].keys())
                if form_json["service_type"] in service_keys:
                    return True
    return False

def validate_blocks_category(blocks_ids, category):
    for id in blocks_ids:
        if str(Block.objects.get(id=id).category) != category:
            return False
    return True

def validate_for_form_blocks(blocks_ids):
    for id in blocks_ids:
        if not Block.objects.get(id=id).for_form:
            return False
    return True