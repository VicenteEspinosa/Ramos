
from backend_app.db_models.form_tree import FormTree
from backend_app.db_serializers.form_tree_serializer import FormTreeSerializer
from backend_app.db_helpers.form_tree_helpers import (
    add_category, 
    edit_category, 
    del_category,
    inactive_category,
    activate_category,
    get_active_categories,
    create_new_task_types
)
from backend_app.db_helpers.client_helpers import create_new_client
from backend_app.db_validators.form_tree_validators import validate_category_tree, validate_formtree
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser


@api_view(['GET'])
def get_form_tree(request):
    """Return the last form tree created."""

    form_tree = FormTree.objects.all().last()
    form_tree_serializer = FormTreeSerializer(form_tree)
    return JsonResponse(form_tree_serializer.data, safe=False, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_active_tree(request):
    """Return the last form tree created with valid categories."""

    active_tree = get_active_categories()
    return JsonResponse(active_tree, safe=False, status=status.HTTP_200_OK)


@api_view(['POST'])
def post_form_tree(request):
    """Add a new form tree."""

    form_tree_data = JSONParser().parse(request)
    form_tree_json = form_tree_data['tree']
    form_tree_serializer = FormTreeSerializer(data=form_tree_data)
    if form_tree_serializer.is_valid():
        if validate_formtree(form_tree_json):
            f = form_tree_serializer.save()
            f.save()
            return JsonResponse(form_tree_serializer.data, status=status.HTTP_201_CREATED)
        tree_error = {"error": "The tree structure is incorrect."}
        return JsonResponse(tree_error, status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse(form_tree_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_post_category(request):
    """Add a new category into the form tree or get all categories."""

    if request.method == 'POST':
        category_data = JSONParser().parse(request)
        if validate_category_tree(category_data):
            new_category_id = add_category(category_data)
            if new_category_id:
                create_new_task_types(new_category_id)
                create_new_client(new_category_id)
                return JsonResponse(f"The category {new_category_id} was created successfully", 
                                    safe=False, status=status.HTTP_201_CREATED)
        tree_error = {"error": "The category could not be created."}
        return JsonResponse(tree_error, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        form_tree = FormTree.objects.all().last()
        category_keys = form_tree.tree.keys()
        categories = []
        for category_id in category_keys:
            data = {
                'id': category_id,
                'name': form_tree.tree[category_id]['name']
            }
            categories.append(data)
        return JsonResponse(categories, safe=False, status=status.HTTP_200_OK)


@api_view(['PUT', 'DELETE'])
def edit_del_category(request, pk):
    """Edit or delete the category."""

    category_data = JSONParser().parse(request)
    if request.method == 'PUT':
        if validate_category_tree(category_data):
            edit_category(pk, category_data)
            return JsonResponse(f"The category {pk} was edited successfully", 
                                safe=False, status=status.HTTP_201_CREATED)
    
    elif request.method == 'DELETE':
        if del_category(pk):
            return JsonResponse(f"The category {pk} was deleted successfully", 
                                safe=False, status=status.HTTP_201_CREATED)
        tree_error = {"error": "The category could not be deleted."}
        return JsonResponse(tree_error, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def del_inactive_category(request, pk):
    """inactive category."""
    if inactive_category(pk):
        htttpresponse = {"Success": f"The category {pk} was inactivated successfully"}
        return JsonResponse(htttpresponse, 
                            safe=False, status=status.HTTP_201_CREATED)
    tree_error = {"error": "The category could not be inactivated."}
    return JsonResponse(tree_error, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def put_activate_category(request, pk):
    """activate category."""
    if activate_category(pk):
        htttpresponse = {"Success": f"The category {pk} was activated successfully"}
        return JsonResponse(htttpresponse, 
                            safe=False, status=status.HTTP_201_CREATED)
    tree_error = {"error": "The category could not be activated."}
    return JsonResponse(tree_error, status=status.HTTP_400_BAD_REQUEST)
    


