
from django.http import HttpRequest, HttpResponse, JsonResponse
from zerver.models import HighScore


def end_game(request):
    #if a there is a post and score is present, save the score
    #if request.method is 'POST':
    if 'score' in request.POST:
        game=request.POST['gameID']
        score=request.POST['score']


        try:
            highscore = HighScore.objects.create(
                name = request.user.name,
                game = game,
                score =score,
            )
            highscore.save()
            #it worked
            response = {
                'status': 1,
                'message': 'Game saved'
            }
        except Exception as e:
            #something didnt work
             response = {
                 'status': 0,
                 'message': 'Something went wrong - ' +str(e)
             }
    return JsonResponse(response)
