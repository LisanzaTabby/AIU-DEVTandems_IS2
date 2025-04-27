from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from .models import Message, User

@receiver(post_save, sender=Message)
def notify_users_on_new_message(sender, instance, created, **kwargs):
    if created:
        room = instance.room
        sender_user = instance.user

        # Gather host and participants
        recipients = list(room.participants.all())

        # Include the host if not the one who sent the message
        if room.host and room.host != sender_user:
            recipients.append(room.host)

        # Remove duplicates and exclude sender
        recipients = list(set(recipients))
        recipients = [user for user in recipients if user != sender_user]

        recipient_emails = [user.email for user in recipients if user.email]

        if recipient_emails:
            subject = f"🔔🔔New message in AIUDEVTandems room: {room.name}🔔🔔"

            # Prepare context for the HTML email template
            email_context = {
                'host_username': room.host.username if room.host else 'User',
                'sender_username': sender_user.username,
                'room_name': room.name,
                'message_body': instance.body,
            }

            # Render HTML content
            html_content = render_to_string('AIUApp/email_notification.html', email_context)

            # Create EmailMultiAlternatives object
            email = EmailMultiAlternatives(
                subject=subject,
                body=f"Hi, {sender_user.username} posted a new message in '{room.name}'.",  # plain text fallback
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=recipient_emails,
            )
            email.attach_alternative(html_content, "text/html")  # attach HTML content

            email.send(fail_silently=False) 
             # show errors during development
@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:  # Only when a new user is created
        subject = '🎉 Welcome to AIUDEVTandem!'
        
        # Prepare context for welcome email
        email_context = {
            'username': instance.username,
        }

        html_content = render_to_string('AIUApp/welcome_email.html', email_context)

        email = EmailMultiAlternatives(
            subject=subject,
            body=f"Hi {instance.username}, welcome to AIUDEVTandem! 🚀",
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[instance.email],
        )
        email.attach_alternative(html_content, "text/html")
        email.send(fail_silently=False)