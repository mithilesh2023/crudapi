from rest_framework.generics import GenericAPIView
from .serializers import VcardSerializer
from .models import Vcard
from rest_framework.views import APIView
from rest_framework.response import Response

class VcardList(APIView):
    vcard=Vcard.objects.all()
    serializer=VcardSerializer(vcard,many=True)

    def get(self,req):
        return Response(self.serializer.data,status=200)
    
    def post(self,req):

        data={
            "name":req.POST.get("name"),
            "contact":req.POST.get("contact")
        }
        serializer=VcardSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
        
class VcardDetails(GenericAPIView):
    serializer_class=VcardSerializer
    def get(self,req,id=None):
        singleVCard=Vcard.objects.get(id=id)
        serializer=VcardSerializer(singleVCard)
        return Response(serializer.data,status=200)

    def delete(slef,req,id=None):
        singleVCard=Vcard.objects.get(id=id)
        singleVCard.delete()
        return Response(status=200)

    def patch(slef,req,id=id):
        singleVCard=Vcard.objects.get(id=id)
        serializer=VcardSerializer(singleVCard,data=req.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
        else:
            return Response({"msg":"record not updated","error":serializer.errors})

