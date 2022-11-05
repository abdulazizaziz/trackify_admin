from rest_framework import serializers
from .models import *


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'id',
            'user',
            'name',
            'time',
            'idol',
            'clicks',
            'presses',
        ]


class ScreenShotSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        project_id = self.context["project_id"]
        return ScreenShot.objects.create(project_id=project_id, **validated_data)
    class Meta:
        model = ScreenShot
        fields = [
            'id',
            'screenshot'
        ]

class TimeSheetSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        project_id = self.context["project_id"]
        return TimeSheet.objects.create(project_id=project_id, **validated_data)
    class Meta:
        model = TimeSheet
        fields = [
            'id',
            'status',
        ]


class SimpleProjectSerializer(serializers.ModelSerializer):
    screenshots = ScreenShotSerializer(many=True, read_only=True)
    timesheets = TimeSheetSerializer(many=True, read_only=True)
    class Meta:
        model = Project
        fields = [
            'id',
            'user',
            'name',
            'time',
            'idol',
            'clicks',
            'presses',
            'screenshots',
            'timesheets',
        ]