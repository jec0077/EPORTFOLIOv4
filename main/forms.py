from django.forms import ModelForm, EmailInput, TextInput
from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["message_sender_email", "message_subject", "message_content"]
        widgets = {
            "message_sender_email":
            EmailInput(
                attrs={
                    'class':
                    "w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out",
                    'type': 'email',
                    'id': 'email',
                    'name': 'email'
                }),
            "message_subject":
            TextInput(
                attrs={
                    'class':
                    "w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out",
                    'type': 'text',
                    'id': 'name',
                    'name': 'name'
                }),
            "message_content":
            TextInput(
                attrs={
                    'class':
                    "w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 h-32 text-base outline-none text-gray-700 py-1 px-3 resize-none leading-6 transition-colors duration-200 ease-in-out",
                    'id': 'message',
                    'name': 'message'
                })
        }
