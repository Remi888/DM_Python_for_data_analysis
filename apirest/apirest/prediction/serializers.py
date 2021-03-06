from rest_framework import serializers
from prediction.models import Incident

class IncidentSerializer(serializers.Serializer):
	active = serializers.FloatField()
	reassignment_count = serializers.FloatField()
	reopen_count = serializers.FloatField()
	sys_mod_count = serializers.FloatField()
	made_sla = serializers.FloatField()
	caller_id = serializers.FloatField()
	opened_by = serializers.FloatField()
	sys_created_by = serializers.FloatField()
	sys_updated_by = serializers.FloatField()
	location = serializers.FloatField()
	category = serializers.FloatField()
	subcategory = serializers.FloatField()
	u_symptom = serializers.FloatField()
	impact = serializers.FloatField()
	urgency = serializers.FloatField()
	priority = serializers.FloatField()
	assignment_group = serializers.FloatField()
	assigned_to = serializers.FloatField()
	knowledge = serializers.FloatField()
	u_priority_confirmation = serializers.FloatField()
	resolved_by = serializers.FloatField()
	sys_created_at_day = serializers.FloatField()
	sys_created_at_month = serializers.FloatField()
	sys_created_at_year = serializers.FloatField()
	sys_created_at_hour = serializers.FloatField()
	sys_created_at_minute = serializers.FloatField()
	sys_created_at_week_day = serializers.FloatField()
	sys_updated_at_day = serializers.FloatField()
	sys_updated_at_month = serializers.FloatField()
	sys_updated_at_year = serializers.FloatField()
	sys_updated_at_hour = serializers.FloatField()
	sys_updated_at_minute = serializers.FloatField()
	sys_updated_at_week_day = serializers.FloatField()
	opened_at_day = serializers.FloatField()
	opened_at_month = serializers.FloatField()
	opened_at_year = serializers.FloatField()
	opened_at_hour = serializers.FloatField()
	opened_at_minute = serializers.FloatField()
	opened_at_week_day = serializers.FloatField()
	Active_State = serializers.FloatField()
	Awaiting_Evidence = serializers.FloatField()
	Awaiting_Problem = serializers.FloatField()
	Awaiting_User_Info = serializers.FloatField()
	Awaiting_Vendor = serializers.FloatField()
	Closed = serializers.FloatField()
	New = serializers.FloatField()
	Other_incident_state = serializers.FloatField()
	Resolved = serializers.FloatField()
	Direct_opening = serializers.FloatField()
	Email = serializers.FloatField()
	IVR = serializers.FloatField()
	Phone = serializers.FloatField()
	Self_service = serializers.FloatField()
	Other_code = serializers.FloatField()
	code_1 = serializers.FloatField()
	code_10 = serializers.FloatField()
	code_11 = serializers.FloatField()
	code_12 = serializers.FloatField()
	code_13 = serializers.FloatField()
	code_14 = serializers.FloatField()
	code_15 = serializers.FloatField()
	code_16 = serializers.FloatField()
	code_17 = serializers.FloatField()
	code_2 = serializers.FloatField()
	code_3 = serializers.FloatField()
	code_4 = serializers.FloatField()
	code_5 = serializers.FloatField()
	code_6 = serializers.FloatField()
	code_7 = serializers.FloatField()
	code_8 = serializers.FloatField()
	code_9 = serializers.FloatField()
	Other_vendor = serializers.FloatField()
	Vendor_1 = serializers.FloatField()
	Vendor_2 = serializers.FloatField()
	Vendor_3 = serializers.FloatField()
	code_8s = serializers.FloatField()
	Do_Not_Notify = serializers.FloatField()
	Send_Email = serializers.FloatField()
	time_completions = serializers.FloatField(allow_null=True)

	def create(self, validated_data):
        """
        Create and return a new `House` instance, given the validated data.
        """
        return House.objects.create(**validated_data)

	def update(self, instance, validated_data):
        """
        Update and return an existing `House` instance, given the validated data.
        """
		instance.active = validated_data.get('active', instance.active)
        instance.reassignment_count = validated_data.get('reassignment_count', instance.reassignment_count)
        instance.reopen_count = validated_data.get('reopen_count', instance.reopen_count)
        instance.sys_mod_count = validated_data.get('sys_mod_count', instance.sys_mod_count)
        instance.made_sla = validated_data.get('made_sla', instance.made_sla)
        instance.caller_id = validated_data.get('caller_id', instance.caller_id)
        instance.opened_by = validated_data.get('opened_by', instance.opened_by)
        instance.sys_created_by = validated_data.get('sys_created_by', instance.sys_created_by)
        instance.sys_updated_by = validated_data.get('sys_updated_by', instance.sys_updated_by)
        instance.location = validated_data.get('location', instance.location)
        instance.category = validated_data.get('category', instance.category)
        instance.subcategory = validated_data.get('subcategory', instance.subcategory)
        instance.u_symptom = validated_data.get('u_symptom', instance.u_symptom)
        instance.impact = validated_data.get('impact', instance.impact)
        instance.urgency = validated_data.get('urgency', instance.urgency)
        instance.priority = validated_data.get('priority', instance.priority)
        instance.assignment_group = validated_data.get('assignment_group', instance.assignment_group)
        instance.assigned_to = validated_data.get('assigned_to', instance.assigned_to)
        instance.knowledge = validated_data.get('knowledge', instance.knowledge)
        instance.u_priority_confirmation = validated_data.get('u_priority_confirmation', instance.u_priority_confirmation)
        instance.resolved_by = validated_data.get('resolved_by', instance.resolved_by)
        instance.sys_created_at_day = validated_data.get('sys_created_at_day', instance.sys_created_at_day)
        instance.sys_created_at_month = validated_data.get('sys_created_at_month', instance.sys_created_at_month)
        instance.sys_created_at_year = validated_data.get('sys_created_at_year', instance.sys_created_at_year)
        instance.sys_created_at_hour = validated_data.get('sys_created_at_hour', instance.sys_created_at_hour)
        instance.sys_created_at_minute = validated_data.get('sys_created_at_minute', instance.sys_created_at_minute)
        instance.sys_created_at_week_day = validated_data.get('sys_created_at_week_day', instance.sys_created_at_week_day)
        instance.sys_updated_at_day = validated_data.get('sys_updated_at_day', instance.sys_updated_at_day)
        instance.sys_updated_at_month = validated_data.get('sys_updated_at_month', instance.sys_updated_at_month)
        instance.sys_updated_at_year = validated_data.get('sys_updated_at_year', instance.sys_updated_at_year)
        instance.sys_updated_at_hour = validated_data.get('sys_updated_at_hour', instance.sys_updated_at_hour)
        instance.sys_updated_at_minute = validated_data.get('sys_updated_at_minute', instance.sys_updated_at_minute)
        instance.sys_updated_at_week_day = validated_data.get('sys_updated_at_week_day', instance.sys_updated_at_week_day)
        instance.opened_at_day = validated_data.get('opened_at_day', instance.opened_at_day)
        instance.opened_at_month = validated_data.get('opened_at_month', instance.opened_at_month)
        instance.opened_at_year = validated_data.get('opened_at_year', instance.opened_at_year)
        instance.opened_at_hour = validated_data.get('opened_at_hour', instance.opened_at_hour)
        instance.opened_at_minute = validated_data.get('opened_at_minute', instance.opened_at_minute)
        instance.opened_at_week_day = validated_data.get('opened_at_week_day', instance.opened_at_week_day)
        instance.Active_State = validated_data.get('Active_State', instance.Active_State)
        instance.Awaiting_Evidence = validated_data.get('Awaiting_Evidence', instance.Awaiting_Evidence)
        instance.Awaiting_Problem = validated_data.get('Awaiting_Problem', instance.Awaiting_Problem)
        instance.Awaiting_User_Info = validated_data.get('Awaiting_User_Info', instance.Awaiting_User_Info)
        instance.Awaiting_Vendor = validated_data.get('Awaiting_Vendor', instance.Awaiting_Vendor)
        instance.Closed = validated_data.get('Closed', instance.Closed)
        instance.New = validated_data.get('New', instance.New)
        instance.Other_incident_state = validated_data.get('Other_incident_state', instance.Other_incident_state)
        instance.Resolved = validated_data.get('Resolved', instance.Resolved)
        instance.Direct_opening = validated_data.get('Direct_opening', instance.Direct_opening)
        instance.Email = validated_data.get('Email', instance.Email)
        instance.IVR = validated_data.get('IVR', instance.IVR)
        instance.Phone = validated_data.get('Phone', instance.Phone)
        instance.Self_service = validated_data.get('Self_service', instance.Self_service)
        instance.Other_code = validated_data.get('Other_code', instance.Other_code)
        instance.code_1 = validated_data.get('code_1', instance.code_1)
        instance.code_10 = validated_data.get('code_10', instance.code_10)
        instance.code_11 = validated_data.get('code_11', instance.code_11)
        instance.code_12 = validated_data.get('code_12', instance.code_12)
        instance.code_13 = validated_data.get('code_13', instance.code_13)
        instance.code_14 = validated_data.get('code_14', instance.code_14)
        instance.code_15 = validated_data.get('code_15', instance.code_15)
        instance.code_16 = validated_data.get('code_16', instance.code_16)
        instance.code_17 = validated_data.get('code_17', instance.code_17)
        instance.code_2 = validated_data.get('code_2', instance.code_2)
        instance.code_3 = validated_data.get('code_3', instance.code_3)
        instance.code_4 = validated_data.get('code_4', instance.code_4)
        instance.code_5 = validated_data.get('code_5', instance.code_5)
        instance.code_6 = validated_data.get('code_6', instance.code_6)
        instance.code_7 = validated_data.get('code_7', instance.code_7)
        instance.code_8 = validated_data.get('code_8', instance.code_8)
        instance.code_9 = validated_data.get('code_9', instance.code_9)
        instance.Other_vendor = validated_data.get('Other_vendor', instance.Other_vendor)
        instance.Vendor_1 = validated_data.get('Vendor_1', instance.Vendor_1)
        instance.Vendor_2 = validated_data.get('Vendor_2', instance.Vendor_2)
        instance.Vendor_3 = validated_data.get('Vendor_3', instance.Vendor_3)
        instance.code_8s = validated_data.get('code_8s', instance.code_8s)
        instance.Do_Not_Notify = validated_data.get('Do_Not_Notify', instance.Do_Not_Notify)
        instance.Send_Email = validated_data.get('Send_Email', instance.Send_Email)
		instance.time_completions = validated_dat.get('time_completions', instance.time_completions)
		instance.save()
		return instance