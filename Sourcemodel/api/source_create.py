from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Sourcemodel.models import Source, SourceSerializer
from rest_framework.views import APIView


class SourceCreate(APIView):
    @csrf_exempt
    def get(self, request):
        source = Source.objects.all()

        return JsonResponse(SourceSerializer(source, many=True).data, safe=False)

    @csrf_exempt
    def post(self, request):
        source_url = request.data.get("source_url")
        name = request.data.get("name")
        phone = request.data.get("phone")

        if name is None:
            return HttpResponse("Вы не ввели достаточно информации, повторите попытку", status=400)
        else:
            source = Source(name=name, source_url=source_url, phone=phone)
        source.save()
        return JsonResponse(SourceSerializer(source).data, status=201)