from backend_app.db_helpers.form_tree_helpers import get_categories
from backend_app.db_constants.filters import FILTERS
from backend_app.db_models.form_tree import FormTree
TECHNICIANS_POSSIBLE_VALUES = [1, 2]
import logging


def validate_formtree(tree_json):
    """Validate the form tree."""

    for category in tree_json:
        if not category.isnumeric():
            return False
        else:
            category_tree = tree_json[category]
            if not validate_category_tree(category_tree):
                return False
    return True


def validate_filternames(category_tree):
    """Validate the category in the form tree."""

    if type(category_tree["filter_names"]) != list:
        logging.error("filter_names must be a list.")
        return False
    else:
        if len(category_tree["filter_names"]) == category_tree["levels"]:
            for filter_name in category_tree["filter_names"]:
                if type(filter_name) != str:
                    logging.error("filter_names invalid format. It only accepts str values.")
                    return False
        else:
            logging.error("Invalid filter_names len, must be equal to levels.")
            return False
    return True


def validate_levels(category_tree):
    """Validates the strcuture in the form tree."""

    if type(category_tree["levels"]) != int:
        return False
    else:
        possible_levels = [x + 1 for x in range(len(FILTERS))]
        if category_tree["levels"] not in possible_levels:
            return False
    return True


def validate_category_tree(category_tree):
    """Validate if the category structure is correct."""

    category_keys = list(category_tree.keys())
    valid_keys = 0
    if len(category_keys) == 8:
        if "name" in category_keys:
            if type(category_tree["name"]) != str:
                logging.error("category name must be str.")
                return False
            valid_keys += 1
        if "is_active" in category_keys:
            if type(category_tree["is_active"]) != bool:
                logging.error("category is_active must be bool.")
                return False
            valid_keys += 1
        if "goal_rm" in category_keys:
            if type(category_tree["goal_rm"]) != int:
                if category_tree["goal_rm"] > 0:
                    logging.error("goal number RM must be int and greater than 0.")
                    return False
            valid_keys += 1
        if "goal_other" in category_keys:
            if type(category_tree["goal_other"]) != int:
                if category_tree["goal_other"] > 0:
                    logging.error("goal number OTHER must be int and greater than 0.")
                    return False
            valid_keys += 1
        if "levels" in category_keys:
            if not validate_levels(category_tree):
                logging.error(f"levels must be an integer between 1 and {len(FILTERS)}")
                return False
            valid_keys += 1
        if "filter_names" in category_keys:
            if not validate_filternames(category_tree):
                return False
            valid_keys += 1
        if "technicians" in category_keys:
            if category_tree["technicians"] not in TECHNICIANS_POSSIBLE_VALUES:
                logging.error(f"Technicians must be 1 or 2.")
                return False
            valid_keys += 1
        if FILTERS[0] in category_keys:
            if type(category_tree[FILTERS[0]]) != dict:
                return False
            else:
                valid_keys += 1
                for branch_tree in category_tree[FILTERS[0]].values():
                    levels = category_tree["levels"]
                    if levels == 1:
                        if not validate_leaf(branch_tree):
                            return False
                    else:
                        if not validate_tree_branch(branch_tree, levels, levels - 1):
                            return False
        if valid_keys == len(category_keys):
            return True
    print(category_tree)
    logging.error(f"Invalid category keys structure. valid keys: {valid_keys}/{len(category_keys)}")

def validate_tree_branch(branch, levels, actual_level):
    """Validate the specific branch into the form tree."""

    branch_filter = FILTERS[levels - actual_level]
    branch_keys = list(branch.keys())
    if len(branch_keys) == 2:
        if "name" in branch_keys:
            if type(branch["name"]) != str:
                return False

        if branch_filter in branch_keys:
            if type(branch[branch_filter]) != dict:
                return False
            else:
                for branch_tree in branch[branch_filter].values():
                    if actual_level == 1:
                        if not validate_leaf(branch_tree):
                            return False
                    else:
                        if not validate_tree_branch(branch_tree, levels, actual_level - 1):
                            return False
        return True


def validate_leaf(leaf):
    """Validate the specific leaf in the form tree."""

    leaf_keys = list(leaf.keys())
    if len(leaf_keys) == 2:
        if "name" in leaf_keys:
            if type(leaf["name"]) != str:
                return False

        if "form_id" in leaf_keys:
            if type(leaf["form_id"]) != int:
                return False
        return True

def validate_category_report(json_data):
    """Validate if the category exists."""

    if "category" in json_data:
        form_tree = FormTree.objects.all().last()
        if json_data["category"] in form_tree.tree:
            return True
    return False

def validate_category(category_id):
    """Validate if the category exists."""

    category_keys = get_categories().keys()
    if str(category_id) in category_keys:
        return True
    else:
        return False
