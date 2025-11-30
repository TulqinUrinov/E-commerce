from rest_framework_simplejwt.tokens import RefreshToken


def create_tokens(user):
    """
        create accesa and refresh tokens
    """
    refresh = RefreshToken.for_user(user)

    refresh['user_id'] = str(user.id)
    refresh['role'] = user.role

    return {
        'access': str(refresh.access_token),
        'refresh': str(refresh),
    }
