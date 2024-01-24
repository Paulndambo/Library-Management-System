from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.models import Member


class MemberDebtAPIView(APIView):
    def get(self, request, *args, **kwars):
        member_id = self.request.query_params.get("member_id")

        member = Member.objects.get(id=member_id)

        return Response({
            "member_id": member_id, 
            "id": member.id, 
            "name": member.name,
            "debt": member.outstanding_debt
            }, 
            status=status.HTTP_200_OK)
