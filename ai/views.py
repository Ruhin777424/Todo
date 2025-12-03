from django.http import JsonResponse
from groq import Groq
from django.conf import settings
import logging
import traceback

logger = logging.getLogger(__name__)

def ask_ai(request):
    try:
        question = request.GET.get("q", "").strip()

        if not question:
            return JsonResponse({"error": "No prompt provided"}, status=400)

        api_key = settings.GROQ_API_KEY
        if not api_key:
            logger.error("GROQ_API_KEY not configured")
            return JsonResponse({"error": "AI service not configured"}, status=500)

        client = Groq(api_key=api_key)
        
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": question}]
        )

        answer = response.choices[0].message.content
        return JsonResponse({"answer": answer})
        
    except Exception as e:
        logger.error(f"AI request error: {str(e)}\n{traceback.format_exc()}")
        return JsonResponse(
            {"error": f"AI service error: {str(e)}"}, 
            status=500
        )


