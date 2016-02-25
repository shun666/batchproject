# coding: utf-8
import sys


from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth import login,authenticate

from celery.result import AsyncResult

from .models import BatchWork, Item
from .serializers import BatchWorkSerializer



@api_view(['POST'])
def do_login(request):
    status = 0
    if request.user.is_authenticated():
        status = 1
    else:
        if request.method == 'POST':
            json_data = request.data
            username = json_data["username"]
            password = json_data["password"]
            user = authenticate(username=username,password=password)
            if user is not None:
                status = 1
                login(request,user)
                print(request.session.session_key)
            else:
                return Response({"status":status})
    return Response({"status":status})


class DoTaskView(APIView):
    """
    非同期実行用REST APIサンプル


    get:パラメータで与えられたjob_idのceleryジョブの実行結果を取得し､返却する

    post:celeryにジョブ実行リクエストを送る

    """
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        print(request.GET['job_id'])
        result = AsyncResult(request.GET['job_id'])

        response = Response(result.status, status=status.HTTP_200_OK)
        return response


    def post(self, request, *args, **kwargs):
        # Any URL parameters get passed in **kwargs
        try:
            json_data = request.data
            # コマンドライン引数から実行モジュールを指定する
            mod = __import__(json_data["package_name"],fromlist=[json_data["cls_name"]])
            class_def = getattr(mod,json_data["cls_name"])


            # コマンドライン引数からCeleryに引数を渡す
            result = class_def().delay(*json_data["param"])

            response = Response(result.id, status=status.HTTP_202_ACCEPTED)
            return response
        except Exception as exc:
            print(exc)
            response = Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return response


class DoSyncTaskView(APIView):
    """
    同期実行用REST API
    """
    #authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        result = BatchWork.objects.all()[:100]
        serializer = BatchWorkSerializer(result, many=True)
        return Response(serializer.data)


    def post(self, request, *args, **kwargs):
        print(request.user)
        # Any URL parameters get passed in **kwargs
        items = Item.objects.all()[:100]
        batch_cnt = items.count()
        for item in items:
            BatchWork(name=item.name, date=item.date).save()

        response = Response(status=status.HTTP_200_OK)
        return response