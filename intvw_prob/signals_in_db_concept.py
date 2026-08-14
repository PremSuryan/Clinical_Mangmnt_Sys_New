#Signals

#When to use?

"""

signal is a mechanism that lets one part of the application notify another part when certain events occur, such as saving or deleting a model.
 It helps perform automatic actions without explicitly calling those functions every time.

When do you use Signals?

Use signals for secondary or side-effect actions, such as:

Automatically creating a user profile after a user is created.
Sending confirmation emails.
Writing audit logs.
Sending notifications.
Clearing or updating caches.

Avoid using signals for core business logic that needs to be explicit and easy to follow, because signals can make the application's flow harder to 
understand and debug
"""

#When not to use Signal:
"""
Don't use signals if:

The logic is only used in one place.
The action is part of the main business flow.
The code becomes difficult to understand.
"""

#Generator QR Code after log in using Signal ---> in Django :

#Django provides a built-in signal:

from django.contrib.auth.signals import user_logged_in

#Create a signal:

# signals.py

from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in


def generate_qr(user):
    pass


@receiver(user_logged_in)   # receiver---> A decorator for connecting receivers to signals. Used by passing in the signal (or list of signals) and keyword arguments to connect::
def create_qr(sender, request, user, **kwargs):
    print("User logged in")

    # Generate QR
    generate_qr(user)

#Register the signal.

#In apps.py:

from django.apps import AppConfig

class UsersConfig(AppConfig):
    name = "users"

    def ready(self):
        import users.signals