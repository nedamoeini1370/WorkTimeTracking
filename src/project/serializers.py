from datetime import timedelta

from rest_framework import serializers

from project.models import Project, Task


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    total_time = serializers.ReadOnlyField()
    total_suspend_time = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ('start_date', 'end_date', 'suspend_date', 'total_suspend_time', 'total_time',)

    def get_total_suspend_time(self, obj) -> str:
        """
        Provide hh:mm:ss view for total_suspend_time
        :param obj:
        :return: total_suspend_time:
        """
        time = timedelta(0, obj.total_suspend_time)
        return "%s" % str(time).split('.')[0]
