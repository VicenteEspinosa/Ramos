from backend_app.db_paginators.question_paginator import QuestionPaginator
from backend_app.db_models.block import Block
from backend_app.db_models.question import Question
from backend_app.db_serializers.question_serializer import QuestionSerializer, QuestionPutSerializer
from backend_app.db_validators.question_validators import validate_options, validate_question_category_exits, validate_question_unique, validate_question_put_type
from backend_app.db_helpers.json_helpers import get_indexed_json
from backend_app.db_validators.block_validators import check_block_dependencies
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser


@api_view(['GET', 'POST'])
def question_list(request):
    """Return all the questions and add a new question."""

    if request.method == 'GET':
        questions = Question.objects.all().order_by('-id')
        questions_serializer = QuestionSerializer(questions, many=True)
        return JsonResponse(questions_serializer.data, safe=False, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        question_data = JSONParser().parse(request)
        try:
            options = question_data['options']
            category = question_data['category_id']
        except:
            question_error = {"error": "Missing fields."}
            return JsonResponse(question_error, status=status.HTTP_400_BAD_REQUEST)
        question_serializer = QuestionSerializer(data=question_data)
        if question_serializer.is_valid():
            if validate_options(options):
                if validate_question_category_exits(category):
                    if validate_question_unique(category, question_data["value"]):
                        q = question_serializer.save()
                        q.save()
                        return JsonResponse(question_serializer.data, status=status.HTTP_201_CREATED)
                    return JsonResponse({"error": "question is repeated"}, status=status.HTTP_400_BAD_REQUEST)
                question_error = {"error": "Inalid category."}
                return JsonResponse(question_error, status=status.HTTP_400_BAD_REQUEST)
            question_error = {"error": "options structure is invalid."}
            return JsonResponse(question_error, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse(question_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def question_list_indexed(request):
    """Return all the questions with the index."""

    questions = Question.objects.all().order_by('-id')
    questions_serializer = QuestionSerializer(questions, many=True)
    return JsonResponse(get_indexed_json(questions_serializer.data), safe=False, status=status.HTTP_200_OK)


@api_view(['GET'])
def question_list_active_paginated(request):
    """Return all the questions with pagination."""

    questions = Question.objects.filter(status=True).order_by('-id')
    page_size = request.query_params.get('page_size', False)
    if page_size:
        question_paginator = QuestionPaginator(page_size)
        response = question_paginator.generate_response(questions, QuestionSerializer, request)
        return response
    return JsonResponse({'error': 'The page_size must be in the path values.'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def question_list_active(request):
    """Return all the questions active."""

    if request.method == 'GET':
        questions = Question.objects.filter(status=True)
        questions_serializer = QuestionSerializer(questions, many=True)
        return JsonResponse(questions_serializer.data, safe=False, status=status.HTTP_200_OK)


@api_view(['GET'])
def question_list_category(request, category):
    """Return all the questions active."""

    if request.method == 'GET':
        questions = Question.objects.filter(category_id=category, status=True)
        questions_serializer = QuestionSerializer(questions, many=True)
        return JsonResponse(get_indexed_json(questions_serializer.data), safe=False, status=status.HTTP_200_OK)


@api_view(['GET'])
def question_list_active_indexed(request):
    """Return all the questions active with index."""

    if request.method == 'GET':
        questions = Question.objects.filter(status=True)
        questions_serializer = QuestionSerializer(questions, many=True)
        return JsonResponse(get_indexed_json(questions_serializer.data), safe=False, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
def question_detail(request, pk):
    """The GET, PUT and DELETE method for an answer."""

    try:
        question = Question.objects.get(pk=pk)

        if request.method == 'GET':
            question_serializer = QuestionSerializer(question)
            return JsonResponse(question_serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            question_data = JSONParser().parse(request)
            options = question_data['options']
            question_serializer = QuestionPutSerializer(question, data=question_data)
            if question_serializer.is_valid():
                if validate_question_put_type(question, question_data):
                    if validate_options(options):
                        q = question_serializer.save()
                        q.save()
                        return JsonResponse(question_serializer.data, status=status.HTTP_201_CREATED)
                    question_error = {"error": "options structure is invalid."}
                    return JsonResponse(question_error, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return JsonResponse({'error': 'Can only change between types 0 and 1.'}, status=status.HTTP_400_BAD_REQUEST)

            return JsonResponse(question_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE': 
            (block_dependency_list, allowed_to_delete) = check_block_dependencies(question)
            if allowed_to_delete:
                question.status = False
                question.save()
                return JsonResponse({"deleted": True}, status=status.HTTP_200_OK)
            else:
                # Question cannot be deleted
                response = {"deleted": False, "blocks": block_dependency_list}
                return JsonResponse(response, status=status.HTTP_200_OK)

    except Question.DoesNotExist:
        return JsonResponse({'error': 'The question does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def question_delete(request, pk):
    """Removes question from every block it belongs to."""

    try:
        question = Question.objects.get(pk=pk)
        question.status = False
        question.save()
        blocks = Block.objects.all()
        for block in blocks:
            if question.id in block.questions["question_ids"]:
                # Remove question from block questions list
                block.questions["question_ids"].remove(question.id)
                block.save()
        return JsonResponse({'message': 'deleted question successfully'}, status=status.HTTP_200_OK)
    except Question.DoesNotExist:
        return JsonResponse({'error': 'The question does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def question_associated_blocks(request, pk):
    """Return the dependencie for the questions in blocks."""

    try:
        question = Question.objects.get(pk=pk)
        (block_dependency_list, allowed_to_delete) = check_block_dependencies(question)
        response = {"blocks": block_dependency_list}
        return JsonResponse(response, status=status.HTTP_200_OK)
    except Question.DoesNotExist:
        return JsonResponse({'error': 'The question does not exist'}, status=status.HTTP_404_NOT_FOUND)
