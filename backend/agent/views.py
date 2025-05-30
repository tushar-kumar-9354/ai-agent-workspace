from django.shortcuts import render

# Create your views here.
# agent/views.py
from rest_framework.views import APIView
from rest_framework.response import Response

class HealthCheck(APIView):
    def get(self, request):
        return Response({"status": "AI Agent is up and running!"})

from code_engine.gemini_client import generate_code

def post(self, request):
    user_prompt = request.data.get("prompt")
    code = generate_code(user_prompt)
    # Save or execute code here
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from code_engine.gemini_client import generate_code  # ✅ Your Gemini helper
from file_engine.file_saver import save_code_to_file

class CodeGenerationView(APIView):
    def post(self, request):
        user_prompt = request.data.get("prompt")
        if not user_prompt:
            return Response({"error": "Prompt is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            code = generate_code(user_prompt)
            file_path = save_code_to_file(code)

            return Response({
                "generated_code": code,
                "file_path": file_path
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
