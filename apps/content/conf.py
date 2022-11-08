from django.utils.translation import gettext_lazy as _


SCORE_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5')
)


# Directories
POST_EXPORT_DIRECTORY = 'data'
CATEGORY_EXPORT_DIRECTORY = POST_EXPORT_DIRECTORY
SCORE_EXPORT_DIRECTORY = POST_EXPORT_DIRECTORY

# Messages
POST_SEND_SUCCESSFULLY_MESSAGE = _('Post was send successfully')
SCORE_CREATION_SUCCESSFULLY_MESSAGE = _('Score was recorded successfully')
