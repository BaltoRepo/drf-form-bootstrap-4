from rest_framework import serializers
from django.utils import timezone

LANGUAGE_CHOICES = [('python', 'Python'), ('ruby', 'Ruby'), ('php', 'PHP'), ('c', 'C'), ('go', 'Go')]
TEST_CHOICES = [('unit', 'Unit'), ('integration', 'Integration'), ('ua', 'User acceptance')]


class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(
        required=True, allow_blank=False, max_length=100,
        help_text='Title of the snippet'
    )
    description = serializers.CharField(required=False, allow_blank=True, max_length=100, help_text='Description of snippet')
    code = serializers.CharField(style={'base_template': 'textarea.html'}, help_text='Enter the code snippet')
    linenos = serializers.BooleanField(required=False, help_text='Number of lines')
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python', allow_blank=True, help_text='Language of the snippet')
    tests = serializers.MultipleChoiceField(choices=TEST_CHOICES, help_text='Select tests to run. Ctrl-click to select more than one.')
    mail = serializers.EmailField(max_length=None, min_length=None, allow_blank=False, help_text='Your email address')
    views = serializers.IntegerField(max_value=None, min_value=None, help_text='Number of times snippet has been viewed.')
    file = serializers.FileField(max_length=None, allow_empty_file=False, help_text='Select file to upload for snippet.')
    loaded_time = serializers.HiddenField(default=timezone.now)
