from .models import UserProfile, Message

def new_messages_processor(request):
    try:
        user = UserProfile.objects.get(user=request.user)
        new_messages = user.received.filter(read=False)
        return {'new_messages': new_messages}
    except:
        return {}


def get_user_profile(request):
    try:
        user = UserProfile.objects.get(user=request.user)
        return {'userprofile': user}
    except:
        return {}
