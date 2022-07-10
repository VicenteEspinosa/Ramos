from backend_app.db_models.form import Form
from backend_app.db_models.datalist import Datalist
from backend_app.db_models.form_tree import FormTree
from backend_app.db_constants.filters import FILTERS
import logging


def get_active_categories():
    form_tree = FormTree.objects.all().last()
    active_tree = {"id": form_tree.id,
                   "tree": {}}
    for category in form_tree.tree:
        if form_tree.tree[category]["is_active"]:
            active_tree["tree"][category] = form_tree.tree[category]
    return active_tree


def add_category(category_tree):
    """Creates a new category."""

    form_tree = FormTree.objects.all().last()
    len_tree = len(form_tree.tree)
    category_keys = form_tree.tree.keys()
    for x in range(len_tree + 100):
        if str(x) not in category_keys:
            new_category_id = str(x)
            form_tree.tree[new_category_id] = category_tree
            form_tree.save() 
            return new_category_id
    return False


def edit_category(category_id, category_tree):
    """Edit an existing category."""

    form_tree = FormTree.objects.all().last()
    category_keys = form_tree.tree.keys()
    if category_id in category_keys:
        form_tree.tree[category_id] = category_tree
        form_tree.save() 
        return True
    return False


def del_category(category_id):
    """Deletes a category."""

    form_tree = FormTree.objects.all().last()
    default_categories = ["0", "1"]
    category_keys = form_tree.tree.keys()
    if (category_id in category_keys) and (category_id not in default_categories):
        del form_tree.tree[category_id]
        form_tree.save()
        return True
    return False


def set_form_in_leaf(form):
    """Set a form id in a form_tree leaf"""

    form_tree = FormTree.objects.all().last()
    category = form_tree.tree[form.category]
    levels = category["levels"]
    if levels == 1:
        if category[FILTERS[0]][form.audit_type]["form_id"] != 0:
            try:
                old_form = Form.objects.get(id=int(category[FILTERS[0]][form.audit_type]["form_id"]))
                if old_form.id != form.id:
                    old_form.for_mobile = False
                    old_form.save()
            except Form.DoesNotExist:
                logging.error("Form in form tree doesnt exist")

        category[FILTERS[0]][form.audit_type]["form_id"] = form.id
    elif levels == 2:
        audit_tree = category[FILTERS[0]][form.audit_type]
        if audit_tree[FILTERS[1]][form.service_type]["form_id"] != 0:
            try:
                old_form = Form.objects.get(id=int(audit_tree[FILTERS[1]][form.service_type]["form_id"]))
                if old_form.id != form.id:
                    old_form.for_mobile = False
                    old_form.save()
            except Form.DoesNotExist:
                logging.error("Form in form tree doesnt exist")
                
        audit_tree[FILTERS[1]][form.service_type]["form_id"] = form.id
    form_tree.save()


def delete_form_from_leaf(form):
    """Deletes a form id in a form_tree leaf"""

    form_tree = FormTree.objects.all().last()
    category = form_tree.tree[form.category]
    levels = category["levels"]
    if levels == 1:
        category[FILTERS[0]][form.audit_type]["form_id"] = "0"
    elif levels == 2:
        audit_tree = category[FILTERS[0]][form.audit_type]
        audit_tree[FILTERS[1]][form.service_type]["form_id"] = "0"
    form_tree.save()


def get_categories():
    """Return all the categories."""

    form_tree = FormTree.objects.all().last()
    category_keys = form_tree.tree.keys()
    categories = {}
    for category_id in category_keys:
        categories[category_id] = form_tree.tree[category_id]['name']
    return categories

def get_categories_active():
    """Return all the categories."""

    form_tree = FormTree.objects.all().last()
    category_keys = form_tree.tree.keys()
    categories = {}
    for category_id in category_keys:
        if form_tree.tree[category_id]['is_active']:
            categories[category_id] = form_tree.tree[category_id]['name']
    return categories
  
def get_category_name(category):
    form_tree = FormTree.objects.all().last()
    return form_tree.tree[category]["name"].capitalize()


def get_category_goals(category):
    form_tree = FormTree.objects.all().last()
    return form_tree.tree[category]["goal_rm"], form_tree.tree[category]["goal_other"]


def inactive_category(category_id):
    form_tree = FormTree.objects.all().last()
    try:
        form_tree.tree[category_id]["is_active"] = False
        form_tree.save()
        return True
    except KeyError as Err:
        logging.error(Err)
        return False


def activate_category(category_id):
    form_tree = FormTree.objects.all().last()
    try:
        form_tree.tree[category_id]["is_active"] = True
        form_tree.save()
        return True
    except KeyError as Err:
        logging.error(Err)
        return False

def create_new_task_types(category_id):
    datalist = Datalist.objects.all().last()
    datalist.lists["task_types"][category_id] = []
    datalist.save()