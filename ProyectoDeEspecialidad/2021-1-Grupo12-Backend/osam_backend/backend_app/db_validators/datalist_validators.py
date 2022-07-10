from backend_app.db_models.form_tree import FormTree

def validate_str_list(data_list: list):
    if type(data_list) != list:
        return False 
    else:
        for element in data_list:
            if type(element) != str:
                return False 
    return True


def validate_work_types(work_types_obj: dict):
    if type(work_types_obj) != dict:
        return False
    keys = work_types_obj.keys()
    form_tree = FormTree.objects.all().last()
    categories = form_tree.tree.keys()
    for key in keys:
        if key not in categories:
            return False 
        category_work_types = work_types_obj[key]
        if not validate_str_list(category_work_types):
            return False 
    return True 
