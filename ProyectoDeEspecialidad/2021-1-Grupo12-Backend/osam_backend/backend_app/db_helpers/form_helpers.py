from backend_app.db_models.form import Form


def check_form_dependencies(block):
    """Checks if block belongs to any form."""

    allowed_to_delete = True
    form_dependency_list = []
    forms = Form.objects.filter(category=block.category)
    for form in forms:
        if block.id in form.blocks["block_ids"]:
            allowed_to_delete = False
            form_dependency_list.append({"id": form.id, "name": form.name})
    return (form_dependency_list, allowed_to_delete)
