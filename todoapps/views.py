from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,serializers

from .models import Todo
from .serializers import TodoSerializer


class TodoCreateGetView(APIView):
    # create
    def post(self,request):
        try:
            serializers = TodoSerializer(data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data, status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"Error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    # retrieve all
    def get(self,request):
        try:
            todo = Todo.objects.all()
            serializers = TodoSerializer(todo, many=True)
            if serializers.data:
                return Response(serializers.data, status=status.HTTP_200_OK)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"Error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

# get single, update, delete (id)
class TodoGetUpdateDeleteView(APIView):
    # retrieve single
    def get(self,request,id):
        try:
            todo = Todo.objects.get(id=id)
            serializer = TodoSerializer(todo)
            if not serializer.data:
                return Response({"Error":"No data found"}, status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    # update single
    def put(self,request,id):
        try:
            todo = Todo.objects.get(id=id)
            serializers = TodoSerializer(todo, data=request.data,partial=True)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data, status=status.HTTP_200_OK)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"Error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    # retrieve single
    def delete(self,request,id):
        try:
            todo = Todo.objects.get(id=id)
            todo.delete()
            return Response({"Message":f"Todo -{todo.title} deleted successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)