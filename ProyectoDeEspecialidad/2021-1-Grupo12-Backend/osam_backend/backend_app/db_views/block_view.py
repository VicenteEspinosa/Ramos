from backend_app.db_models.report import Report
from backend_app.db_helpers.form_helpers import check_form_dependencies
from backend_app.db_helpers.report_helpers import check_report_dependencies
from backend_app.db_serializers.block_serializer import BlockSerializer, BlockPutSerializer
from backend_app.db_validators.question_validators import validate_questions, check_questions_category
from backend_app.db_validators.block_validators import validate_block_category_exits, validate_anwers_unique
from backend_app.db_helpers.json_helpers import get_indexed_json
from backend_app.db_models.block import Block
from backend_app.db_models.form import Form
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status


@api_view(['GET', 'POST'])
def block_list(request):
    """Returns all the answers or save a block."""

    if request.method == 'GET':
        blocks = Block.objects.all().order_by('-id')
        blocks_serializer = BlockSerializer(blocks, many=True)
        return JsonResponse(blocks_serializer.data, safe=False, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        block_data = JSONParser().parse(request)
        try:
            questions_obj = block_data['questions']
            category = block_data['category']
        except KeyError:
            block_error = {"error": "Missing fields"}
            return JsonResponse(block_error, status=status.HTTP_400_BAD_REQUEST)
        block_serializer = BlockSerializer(data=block_data)
        if block_serializer.is_valid():
            if validate_questions(questions_obj):
                if validate_block_category_exits(category):
                    if check_questions_category(questions_obj["question_ids"], category):  
                        if validate_anwers_unique(questions_obj["question_ids"]):
                            b = block_serializer.save()
                            b.save()
                            return JsonResponse(block_serializer.data, status=status.HTTP_201_CREATED)
                        block_error = {"error": "Some questions are repeated"}
                        return JsonResponse(block_error, status=status.HTTP_400_BAD_REQUEST)
                    block_error = {"error": "Some questions are from another category"}
                    return JsonResponse(block_error, status=status.HTTP_400_BAD_REQUEST)
                block_error = {"error": "Invalid category."}
                return JsonResponse(block_error, status=status.HTTP_400_BAD_REQUEST)
            block_error = {"error": "The questions id are not valid"}
            return JsonResponse(block_error, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse(block_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def block_list_indexed(request):
    """Returns all the blocks with index."""

    if request.method == 'GET':
        blocks = Block.objects.all().order_by('-id')
        blocks_serializer = BlockSerializer(blocks, many=True)
        return JsonResponse(get_indexed_json(blocks_serializer.data), safe=False, status=status.HTTP_200_OK)

@api_view(['GET'])
def block_list_category_for_form(request, category, for_form):
    """Returns all the blocks with index."""

    try:
        int(category)
    except ValueError:
        if category != "null":
            block_error = {"error": "category must be a integer"}
            return JsonResponse(block_error, status=status.HTTP_400_BAD_REQUEST)
    if for_form != "True" and for_form != "False" and for_form != "null":
        block_error = {"error": "for_form must be a boolean"}
        return JsonResponse(block_error, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        if for_form != "null":
            if category != "null":
                blocks = Block.objects.filter(category=category, for_form=for_form).order_by('-id')
            else:
                blocks = Block.objects.filter(for_form=for_form).order_by('-id')
        else:
            if category != "null":
                blocks = Block.objects.filter(category=category).order_by('-id')
            else:
                block_error = {"error": "No filter received"}
                return JsonResponse(block_error, status=status.HTTP_400_BAD_REQUEST)
        blocks_serializer = BlockSerializer(blocks, many=True)
        return JsonResponse(get_indexed_json(blocks_serializer.data), safe=False, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
def block_detail(request, pk):
    """The GET, PUT and DELETE method for a block."""

    try:
        block = Block.objects.get(pk=pk)

        if request.method == 'GET':
            block_serialized = BlockSerializer(block)
            return JsonResponse(block_serialized.data, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            block_data = JSONParser().parse(request)
            category = block.category
            try:
                questions_obj = block_data['questions']
            except KeyError:
                block_error = {"error": "Missing fields"}
                return JsonResponse(block_error, status=status.HTTP_400_BAD_REQUEST)
            block_serializer = BlockPutSerializer(block, data=block_data)
            if block_serializer.is_valid():

                if validate_questions(questions_obj):
                    if check_questions_category(questions_obj["question_ids"], category):
                        if validate_anwers_unique(questions_obj["question_ids"]): 
                            b = block_serializer.save()
                            b.save()
                            return JsonResponse(block_serializer.data, status=status.HTTP_201_CREATED)
                        block_error = {"error": "Some questions are repeated"}
                        return JsonResponse(block_error, status=status.HTTP_400_BAD_REQUEST)
                    block_error = {"error": "Some questions are from another category"}
                    return JsonResponse(block_error, status=status.HTTP_400_BAD_REQUEST)
                block_error = {"error": "The questions id are not valid"}
                return JsonResponse(block_error, status=status.HTTP_400_BAD_REQUEST)
            return JsonResponse(block_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE': 
            (forms_dependency_list, allowed_to_delete_form) = check_form_dependencies(block)
            (reports_dependency_list, allowed_to_delete_report) = check_report_dependencies(block)
            if allowed_to_delete_form and allowed_to_delete_report:
                block.delete()
                return JsonResponse({"deleted": True}, status=status.HTTP_201_CREATED)
            elif allowed_to_delete_form:
                response = {"deleted": False, "reports": reports_dependency_list}
                return JsonResponse(response, status=status.HTTP_201_CREATED)
            elif allowed_to_delete_report:
                response = {"deleted": False, "forms": forms_dependency_list}
                return JsonResponse(response, status=status.HTTP_201_CREATED)
            else:
                response = {"deleted": False, "forms": forms_dependency_list,  "reports": reports_dependency_list}
                return JsonResponse(response, status=status.HTTP_201_CREATED)
    except Block.DoesNotExist:
        return JsonResponse({'error': 'The block does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def block_delete(request, pk):
    """Removes question from every block or reports it belongs to."""

    try:
        block = Block.objects.get(pk=pk)
        forms = Form.objects.filter(category=block.category)
        for form in forms:
            if block.id in form.blocks["block_ids"]:
                # Remove block from form blocks list
                form.blocks["block_ids"].remove(block.id)
                form.save()
        reports = Report.objects.filter(category=str(block.category))
        for report in reports:
            if block.id in report.blocks["block_ids"]:
                # Remove block from report blocks list
                report.blocks["block_ids"].remove(block.id)
                report.save()
        block.delete()
        return JsonResponse({'message': 'Block was deleted successfully!'}, status=status.HTTP_200_OK)
    except Block.DoesNotExist:
        return JsonResponse({'error': 'The block does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def block_associated_forms(request, pk):
    """Returns the block that belongs to the form."""

    try:
        block = Block.objects.get(pk=pk)
        (form_dependency_list, allowed_to_delete) = check_form_dependencies(block)
        response = {"forms": form_dependency_list}
        return JsonResponse(response, status=status.HTTP_200_OK)
    except Block.DoesNotExist:
        return JsonResponse({'error': 'The block does not exist'}, status=status.HTTP_404_NOT_FOUND)
