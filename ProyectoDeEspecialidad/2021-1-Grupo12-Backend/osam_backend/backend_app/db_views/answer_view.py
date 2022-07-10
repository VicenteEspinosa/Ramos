from backend_app.db_paginators.answer_paginator import AnswerPaginator
from backend_app.db_models.answer import Answers
from backend_app.db_serializers.answer_serializer import AnswerSerializer
from backend_app.db_helpers.json_helpers import get_indexed_json
from backend_app.db_helpers.user_helpers import userid_type_category_by_request
from backend_app.db_helpers.answer_helpers import (
    complete_answer_data, 
    get_timestamps, 
    string_to_datetime, 
    string_to_report_datetime, 
    complete_technician_name_redes
)
from backend_app.db_helpers.info_panel_helper import (
    create_info_data)
from backend_app.db_validators.answer_validators import (
    validate_answer_data, 
    validate_values, 
    validate_timestamps)
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser


@api_view(['GET'])
def answer_list(request):
    """Returns all the answers."""

    (user_id, user_type, user_category) = userid_type_category_by_request(request)
    if user_type == 2:
        answers = Answers.objects.filter(auditor_id=user_id).order_by('-id')
    elif user_type == 3:
        answers = Answers.objects.filter(category_id=user_category).order_by('-id')
    else:
        answers = Answers.objects.all().order_by('-id')
    answers_serializer = AnswerSerializer(answers, many=True)
    return JsonResponse(answers_serializer.data, safe=False, status=status.HTTP_200_OK)


@api_view(['GET'])
def answer_list_paginated(request):
    """Returns all the answers with pagination."""

    (user_id, user_type, user_category) = userid_type_category_by_request(request)
    if user_type == 2:
        answers = Answers.objects.filter(auditor_id=user_id).order_by('-id')
    elif user_type == 3:
        answers = Answers.objects.filter(category_id=user_category).order_by('-id')
    else:
        answers = Answers.objects.all().order_by('-id')
    page_size = request.query_params.get('page_size', False)
    if page_size:
        answer_paginator = AnswerPaginator(page_size)
        response = answer_paginator.generate_response(answers, AnswerSerializer, request)
        return response
    return JsonResponse({'error': 'The page_size must be in the path values.'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def answer_list_indexed(request):
    """Returns all the answers with the index."""

    (user_id, user_type, user_category) = userid_type_category_by_request(request)
    if user_type == 2:
        answers = Answers.objects.filter(auditor_id=user_id).order_by('-id')
    elif user_type == 3:
        answers = Answers.objects.filter(category_id=user_category).order_by('-id')
    else:
        answers = Answers.objects.all().order_by('-id')
    answers_serializer = AnswerSerializer(answers, many=True)
    return JsonResponse(get_indexed_json(answers_serializer.data), safe=False, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def answer_detail(request, pk):
    """The GET, PUT and DELETE method for an answer."""

    try:
        answer = Answers.objects.get(pk=pk)
        (user_id, user_type, user_category) = userid_type_category_by_request(request)
        if request.method == 'GET':
            if user_type == 2:
                if answer.auditor_id != user_id:
                    answers_error = {"error": "You don't have access to this answer"}
                    return JsonResponse(answers_error, status=status.HTTP_400_BAD_REQUEST)
            elif user_type == 3:
                if str(answer.category_id) != str(user_category):
                    answers_error = {"error": "You don't have access to this answer"}
                    return JsonResponse(answers_error, status=status.HTTP_400_BAD_REQUEST)
            answers_serializer = AnswerSerializer(answer)
            return JsonResponse(answers_serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            answers_data = JSONParser().parse(request)
            answers_serializer = AnswerSerializer(answer, data=answers_data)
            if answers_serializer.is_valid():
                if 'id' in answers_data:
                    del answers_data['id']
                if validate_answer_data(answers_data):
                    (final_timestamp, initial_timestamp, initial_time, initial_date) = get_timestamps(answers_data)
                    if validate_timestamps(final_timestamp, initial_timestamp, initial_time, initial_date):
                        try:
                            answer = answers_serializer.save()
                            answer.auditor_id = answers_data["auditor_id"]
                            answer.commune_id = answers_data["commune_id"]
                            answer.category_id = answers_data["category_id"]
                            answer.audit_type_id = answers_data["audit_type_id"]
                            answer.service_type_id = answers_data["service_type_id"]
                            answer.exit_timestamp = string_to_datetime(final_timestamp)
                            answer.values = answers_data["values"]
                            # Change final_timestamp format for reports
                            answers_data["metadata"]["timestamp_data"]["final_timestamp"] = string_to_report_datetime(
                                final_timestamp)

                            answers_data = complete_technician_name_redes(answers_data)
                            answer.metadata = answers_data["metadata"]
                            answer.blocks = answers_data["blocks"]
                            answer.save()
                            return JsonResponse(answers_serializer.data, safe=False, status=status.HTTP_201_CREATED)
                        except Exception as Err:
                            answers_error = {"error": str(Err)}
                            return JsonResponse(answers_error, safe=False, status=status.HTTP_400_BAD_REQUEST)
                    answers_error = {"error": "Wrong timestamps format. Datetime format: %d/%m/%Y %H:%M:%S"}
                    return JsonResponse(answers_error, status=status.HTTP_400_BAD_REQUEST)
                answers_error = {"error": "Wrong answer structure"}
                return JsonResponse(answers_error, status=status.HTTP_400_BAD_REQUEST)
            return JsonResponse(answers_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'PATCH':
            # Updates answer recieving only question "values"
            values_data = JSONParser().parse(request)
            aux_data = AnswerSerializer(answer).data
            aux_data["values"] = values_data
            answers_serializer = AnswerSerializer(answer, data=aux_data)
            if answers_serializer.is_valid():
                if validate_values(values_data):
                    a = answers_serializer.save()
                    a.values = values_data
                    a.save()
                    return JsonResponse(answers_serializer.data, status=status.HTTP_201_CREATED)
                answers_error = {"error": "Wrong values structure"}
                return JsonResponse(answers_error, safe=False, status=status.HTTP_400_BAD_REQUEST)
            return JsonResponse(answers_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE': 
            answer.delete() 
            return JsonResponse({'message': 'Answer was deleted successfully!'}, status=status.HTTP_201_CREATED)

    except Answers.DoesNotExist:
        return JsonResponse({'error': 'The answer do not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def answer_loader(request):
    """Save a new answer."""

    answers_data = JSONParser().parse(request)
    
    answers_serializer = AnswerSerializer(data=answers_data)
    if answers_serializer.is_valid():
        if validate_answer_data(answers_data):
            try:
                final_timestamp = answers_data["metadata"]["timestamp_data"]["final_timestamp"]
                completed_data = complete_answer_data(answers_data)
                answer = answers_serializer.save()
                answer.metadata = completed_data["metadata"]
                answer.exit_timestamp = completed_data["exit_timestamp"]
                answer.save()
                len_additional_photos = len(completed_data["metadata"]["additional_photos"]["photos"])
                if len_additional_photos:
                    create_info_data(final_timestamp, 
                        answer.auditor_id, 
                        0,
                        2,
                        answer.id,
                        len_additional_photos)
                return JsonResponse(answers_serializer.data, safe=False, status=status.HTTP_201_CREATED)
            except Exception as Err:
                answers_error = {"error": str(Err)}
                return JsonResponse(answers_error, safe=False, status=status.HTTP_400_BAD_REQUEST)
        answers_error = {"error": "Wrong answer structure"}
        return JsonResponse(answers_error, status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse(answers_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
