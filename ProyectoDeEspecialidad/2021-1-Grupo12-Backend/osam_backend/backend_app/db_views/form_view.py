from backend_app.db_models.form import Form
from backend_app.db_models.form_tree import FormTree
from backend_app.db_serializers.form_serializer import FormSerializer
from backend_app.db_validators.form_validators import (validate_blocks_form,
    validate_tree_path, validate_blocks_category, validate_for_form_blocks)
from backend_app.db_helpers.json_helpers import get_indexed_json
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from backend_app.db_helpers.form_tree_helpers import set_form_in_leaf, delete_form_from_leaf


@api_view(['GET', 'POST'])
def form_list(request):
    """Return all the forms and add a new form."""

    if request.method == 'GET':
        forms = Form.objects.all().order_by('-id')
        form_serializer = FormSerializer(forms, many=True)
        return JsonResponse(form_serializer.data, safe=False, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        form_data = JSONParser().parse(request)
        try:
            category = form_data["category"]
            blocks_obj = form_data['blocks']
        except KeyError:
            form_error = {"error": "missing fields"}
            return JsonResponse(form_error, status=status.HTTP_400_BAD_REQUEST)
        form_serializer = FormSerializer(data=form_data)
        if form_serializer.is_valid():
            if validate_blocks_form(blocks_obj):
                if form_data["for_mobile"]:
                    if validate_tree_path(form_data):
                        if validate_blocks_category(blocks_obj["block_ids"] ,category):
                            if validate_for_form_blocks(blocks_obj["block_ids"]):
                                f = form_serializer.save()
                                f.save()
                                set_form_in_leaf(f)
                            else:
                                form_error = {"error": "some blocks are not for forms"}
                                return JsonResponse(form_error, status=status.HTTP_400_BAD_REQUEST)
                        else:
                            form_error = {"error": "some blocks are not for this category"}
                            return JsonResponse(form_error, status=status.HTTP_400_BAD_REQUEST)
                    else:
                        form_error = {"error": "category, audit_type or service_type are invalid for the form_tree"}
                        return JsonResponse(form_error, status=status.HTTP_400_BAD_REQUEST)
                else:
                    if validate_blocks_category(blocks_obj["block_ids"] ,category):
                        if validate_for_form_blocks(blocks_obj["block_ids"]):
                            f = form_serializer.save()
                            f.save()
                        else:
                            form_error = {"error": "some blocks are not for forms"}
                            return JsonResponse(form_error, status=status.HTTP_400_BAD_REQUEST)
                    else:
                        form_error = {"error": "some blocks are not for this category"}
                        return JsonResponse(form_error, status=status.HTTP_400_BAD_REQUEST)
                return JsonResponse(form_serializer.data, status=status.HTTP_201_CREATED)
            form_error = {"error": "The blocks id are not valid"}
            return JsonResponse(form_error, status=status.HTTP_404_NOT_FOUND)

        return JsonResponse(form_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def form_list_indexed(request):
    """Return all the forms with index."""

    if request.method == 'GET':
        forms = Form.objects.all().order_by('-id')
        form_serializer = FormSerializer(forms, many=True)
        return JsonResponse(get_indexed_json(form_serializer.data), safe=False, status=status.HTTP_200_OK)
    

@api_view(['GET', 'PUT', 'DELETE'])
def form_detail(request, pk):
    """The GET, PUT and DELETE method for a form."""

    try:
        form = Form.objects.get(pk=pk)  
        if request.method == 'GET':
            form_serializer = FormSerializer(form)
            return JsonResponse(form_serializer.data)
        elif request.method == 'PUT':
            form_data = JSONParser().parse(request)
            try:
                category = form_data["category"]
                blocks_obj = form_data['blocks']
            except KeyError:
                form_error = {"error": "missing fields"}
                return JsonResponse(form_error, status=status.HTTP_400_BAD_REQUEST)
            form_serializer = FormSerializer(form, data=form_data)
            if form_serializer.is_valid():
                if validate_blocks_form(blocks_obj):
                    if form_data["for_mobile"]:
                        if validate_tree_path(form_data):
                            if validate_blocks_category(blocks_obj["block_ids"] ,category):
                                if validate_for_form_blocks(blocks_obj["block_ids"]):
                                    f = form_serializer.save()
                                    f.save()
                                    set_form_in_leaf(f)
                                else:
                                    form_error = {"error": "some blocks are not for forms"}
                                    return JsonResponse(form_error, status=status.HTTP_400_BAD_REQUEST)
                            else:
                                form_error = {"error": "some blocks are not for this category"}
                                return JsonResponse(form_error, status=status.HTTP_400_BAD_REQUEST)
                        else:
                            form_error = {"error": "category, audit_type or service_type are invalid for the form_tree"}
                            return JsonResponse(form_error, status=status.HTTP_400_BAD_REQUEST)
                    else:
                        f = form_serializer.save()
                        f.save()
                    return JsonResponse(form_serializer.data, status=status.HTTP_201_CREATED)
                form_error = {"error": "The blocks id are not valid"}
                return JsonResponse(form_error, status=status.HTTP_404_NOT_FOUND)
            return JsonResponse(form_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE': 
            if form.for_mobile:
                delete_form_from_leaf(form)
            form.delete()
            return JsonResponse({'message': 'Form was deleted successfully!'}, status=status.HTTP_201_CREATED)

    except Form.DoesNotExist:
        return JsonResponse({'error': 'The form does not exist'})
