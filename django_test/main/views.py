from django.http import HttpResponse
from datetime import datetime

def home(request):
    now = datetime.now()
    return HttpResponse(f"""
        <html>
            <head><title>Django Test</title></head>
            <body>
                <h1>Hello, Django works!</h1>
                <p>Date actuelle : {now}</p>
            </body>
        </html>
    """)