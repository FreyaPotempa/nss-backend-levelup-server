"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Event


class EventView(ViewSet):
    """Level up game view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single event type

        Returns:
            Response -- JSON serialized game type
        """
        event = Event.objects.get(pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all events

        Returns:
            Response -- JSON serialized list of events
        """

        events = Event.objects.all()

        if "organizer" in request.query_params:
            organizer_id = request.query_params["organizer"]
            events = events.filter(organizer_id=organizer_id)

        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)


class EventSerializer(serializers.ModelSerializer):
    """JSON serializer for events
    """
    class Meta:
        model = Event
        fields = ('id', 'description', 'date', 'time',
                  'organizer_id')
