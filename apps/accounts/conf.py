from django.utils.translation import gettext_lazy as _

# Directories
AVATAR_DIRECTORY = 'avatars'
USER_EXPORT_DIRECTORY = 'data'

# Messages

# Login Messages
LOGIN_FAILED_REQUIRED_FIELDS_MESSAGE = _('The username or email is required')
LOGIN_FAILED_BY_USERNAME_MESSAGE = _('The username or password is incorrect')
LOGIN_FAILED_BY_EMAIL_MESSAGE = _('The email or password is incorrect')

# Signup Messages
PASSWORDS_MISSMATCH_MESSAGE = _('Passwords do not match')
USER_CREATION_SUCCESSFUL_MESSAGE = _('Your signup was successful')

# Follow & Unfollow Messages
USER_NOT_FOUND_ERROR = _('User not found')
FOLLOW_MESSAGE = _('Follow was successful')
UNFOLLOW_MESSAGE = _('Unfollow was successful')
