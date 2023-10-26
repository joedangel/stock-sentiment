from django.shortcuts import render
from django.http import JsonResponse
import random
from datetime import datetime, timedelta
import json
import time

# Create your views here.

with open('sentiment/SentimentScores.json', 'r') as f:
    json_data = json.load(f)

def sentiment_scores(request):
    days = request.GET.get('days', None)
    if days is not None:
        try:
            days = int(days)
        except ValueError:
            return JsonResponse({'error': 'Invalid days parameter'}, status=400)

        if days == 7 or days == 30:
            start = time.time()
            now = datetime.now() - timedelta(hours=7)

            current_date = now.strftime("%m/%d")
            last_seven_days = [now - timedelta(days=i) for i in range(days)]
            last_seven_days_str = set([date.strftime("%m/%d") for date in last_seven_days])

            # Reading the JSON data from the file
            # with open('sentiment/SentimentScores.json', 'r') as f:
            #     json_data = json.load(f)

            filtered_data = {}
            for key in json_data.keys():
                filtered_data[key] = [value for value in json_data[key] if value["Date"] in last_seven_days_str]

            print(time.time() -start)
            return JsonResponse(filtered_data)
        else:
            return JsonResponse({'error': 'Days value must be 7 or 30'}, status=400)
    else:
        return JsonResponse({'error': 'Days parameter is required'}, status=400)

