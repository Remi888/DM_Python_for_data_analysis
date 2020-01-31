from django.http                    import HttpResponse
from django.http                    import JsonResponse
from django.views.decorators.csrf   import csrf_exempt
from rest_framework.renderers       import JSONRenderer
from rest_framework.parsers         import JSONParser
from prediction.models              import incident
from prediction.serializers         import IncidentSerializer

def predict_time_completions(unscaled_data):
    from sklearn.externals import joblib
    colonnes        = ['active', 'reassignment_count', 'reopen_count', 'sys_mod_count',
       'made_sla', 'caller_id', 'opened_by', 'sys_created_by',
       'sys_updated_by', 'location', 'category', 'subcategory', 'u_symptom',
       'impact', 'urgency', 'priority', 'assignment_group', 'assigned_to',
       'knowledge', 'u_priority_confirmation', 'resolved_by',
       'sys_created_at_day', 'sys_created_at_month', 'sys_created_at_year',
       'sys_created_at_hour', 'sys_created_at_minute',
       'sys_created_at_week_day', 'sys_updated_at_day', 'sys_updated_at_month',
       'sys_updated_at_year', 'sys_updated_at_hour', 'sys_updated_at_minute',
       'sys_updated_at_week_day', 'opened_at_day', 'opened_at_month',
       'opened_at_year', 'opened_at_hour', 'opened_at_minute',
       'opened_at_week_day', 'Active_State', 'Awaiting_Evidence',
       'Awaiting_Problem', 'Awaiting_User_Info', 'Awaiting_Vendor', 'Closed',
       'New', 'Other_incident_state', 'Resolved', 'Direct_opening', 'Email',
       'IVR', 'Phone', 'Self_service', 'Other_code', 'code_1', 'code_10',
       'code_11', 'code_12', 'code_13', 'code_14', 'code_15', 'code_16',
       'code_17', 'code_2', 'code_3', 'code_4', 'code_5', 'code_6', 'code_7',
       'code_8', 'code_9', 'Other_vendor', 'Vendor_1', 'Vendor_2', 'Vendor_3',
       'code_8s', 'Do_Not_Notify', 'Send_Email']
    path_to_model   = "../../model_extraTrees.pkl"
    unscaled_data   = [unscaled_data[colonne] for colonne in colonnes]
    model           = joblib.load(path_to_model)
    scaler          = joblib.load(path_for_scaler)
    donnees_scalees = scaler.transform(unscaled_data)
    time_completions            = model.predict(donnees_scalees)
    return time_completions


@csrf_exempt
def predict(request):
    """
    Renvoie une incident avec la time_completions completee
    (Attend une time_completions innexistante)
    """
    if request.method == 'GET':
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'POST':
        data        = JSONParser().parse(request)
        serializer  = IncidentSerializer(data=data)
        if serializer.is_valid():
            data["time_completions"]        = predict_time_completions(data)
            serializer          = IncidentSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data  , status=201)
        return     JsonResponse(serializer.errors, status=400)

@csrf_exempt
def incident_list(request):
    """
    List all incidents, or create a new incident.
    """
    if request.method == 'GET':
        incident      = Incident.objects.all()
        serializer  = IncidentSerializer(incidents        , many=True)
        reponse     = JsonResponse(serializer.data  , safe=False)
        return reponse

    elif request.method == 'POST':
        data        = JSONParser().parse(request)
        serializer  = IncidentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data  , status=201)
        return     JsonResponse(serializer.errors, status=400)

@csrf_exempt
def incident_detail(request, pk):
    """
    Retrieve, update or delete a incident.
    """
    try:
        incident = Incident.objects.get(pk=pk)
    except Incident.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = IncidentSerializer(incident)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = IncidentSerializer(incident, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        incident.delete()
        return HttpResponse(status=204)