from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.permissions import IsSuperUser, IsManager, IsCurrentUser
from users.serializers import UserSerializer, UserSerializerForAll


class UserViewSet(ModelViewSet):
	serializer_class = UserSerializerForAll
	queryset = User.objects.all()

	def retrieve(self, request, *args, **kwargs):
		instance = self.get_object()
		if self.kwargs['pk'] == str(request.user.pk):
			serializer = UserSerializer(instance)
			return Response(serializer.data)
		else:
			serializer = UserSerializerForAll(instance)
			return Response(serializer.data)

	def get_permissions(self):
		if self.request.method in ['PUT', 'PATCH']:
			permission_classes = [IsCurrentUser | IsSuperUser | IsManager]
		elif self.request.method in ['DELETE']:
			permission_classes = [IsSuperUser]
		else:
			permission_classes = []
		return [permission() for permission in permission_classes]
