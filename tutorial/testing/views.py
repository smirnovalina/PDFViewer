from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import permissions, status
from testing.models import Test, Result
from django.contrib.auth.models import User
from testing.serializers import TestSerializer, ResultSerializer, UserSerializer
from testing.permissions import IsOwner


class TestList(APIView):
    """
    List all tests, or create a new test.
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'testing/index.html'

    def get(self, request):
        tests = Test.objects.all()
        serializer = TestSerializer(tests, many=True)
        return Response({'tests': serializer.data})
        # return Response(serializer.data)

    def post(self, request):
        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TestDetail(APIView):
    """
    Retrieve, update or delete a test instance.
    """

    def get(self, request, pk):
        test = get_object_or_404(Test, pk=pk)
        serializer = TestSerializer(test)
        return Response(serializer.data)

    def put(self, request, pk):
        test = get_object_or_404(Test, pk=pk)
        self.check_object_permissions(request, test)
        serializer = TestSerializer(test, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        word = get_object_or_404(Test, pk=pk)
        self.check_object_permissions(request, word)
        word.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ResultList(APIView):
    """
    List all results, or create a new result.
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request):
        results = Result.objects.all()
        self.check_object_permissions(request, results)
        serializer = ResultSerializer(results, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ResultSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResultDetail(APIView):
    """
    Retrieve, update or delete a word instance.
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwner)

    def get(self, request, pk):
        result = get_object_or_404(Result, pk=pk)
        self.check_object_permissions(request, result)
        serializer = ResultSerializer(result)
        return Response(serializer.data)

    def put(self, request, pk):
        result = get_object_or_404(Result, pk=pk)
        self.check_object_permissions(request, result)
        serializer = ResultSerializer(result, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        result = get_object_or_404(Result, pk=pk)
        self.check_object_permissions(request, result)
        result.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserList(APIView):
    """
    List all users.
    """
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class UserDetail(APIView):
    """
    Retrieve a user instance.
    """
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
