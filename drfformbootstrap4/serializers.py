"""
These resources are for the demo page used in development.
"""
from rest_framework import serializers
from django.utils import timezone

DEMO_CHOICES = [('Lorem', 'Lorem'), ('Ipsum', 'Ipsum')]


def always_invalid(value):
    """Always raise ValidationError, for showing error states in the demo."""
    raise serializers.ValidationError('This is the error message.')


class DemoSerializer(serializers.Serializer):
    char_required_field = serializers.CharField(
        required=True, allow_blank=False, max_length=100,
        help_text='Character, required',
        validators=[always_invalid]
    )
    char_not_required_field = serializers.CharField(
        required=False, allow_blank=True, max_length=100,
        help_text='Character, not required',
        validators=[always_invalid]
    )
    char_input_group = serializers.CharField(
        required=False, allow_blank=True, max_length=100,
        help_text='Input group with prepend and append',
        style={
            'prepend': 'prepend',
            'append': 'append',
        },
        validators=[always_invalid]
    )
    char_readonly_field = serializers.CharField(
        initial='the read-only value',
        help_text='Character, read-only field',
        read_only=True,
        validators=[always_invalid]
    )
    readonly_plain_text_field = serializers.CharField(
        initial='the read-only value',
        help_text='Character, read-only, rendered as text',
        read_only=True,
        style={'class': 'form-control-plaintext'},
        validators=[always_invalid]
    )
    textarea_field = serializers.CharField(
        style={
            'base_template': 'textarea.html',
            'rows': 3,
        },
        help_text='Character text area',
        validators=[always_invalid]
    )
    boolean_field = serializers.BooleanField(
        required=False, help_text='Boolean field',
        validators=[always_invalid]
    )
    choice_field = serializers.ChoiceField(
        choices=DEMO_CHOICES, default='Lorem',
        allow_blank=True,
        help_text='Choice field, blank allowed, select widget',
        validators=[always_invalid]
    )
    choice_radio_field = serializers.ChoiceField(
        choices=DEMO_CHOICES, default='Lorem',
        allow_blank=True,
        help_text='Choice field, blank allowed, radio widget',
        style={'base_template': 'radio.html'},
        validators=[always_invalid]
    )
    choice_radio_field_inline = serializers.ChoiceField(
        choices=DEMO_CHOICES, default='Lorem',
        allow_blank=True,
        help_text='Choice field, blank allowed, radio widget, inline',
        style={'base_template': 'radio.html', 'inline': True},
        validators=[always_invalid]
    )
    multiple_choice_field = serializers.MultipleChoiceField(
        choices=DEMO_CHOICES,
        help_text='Multiple choice field. Ctrl-click to select more than one.',
        validators=[always_invalid]
    )
    multiple_choice_checkbox_field = serializers.MultipleChoiceField(
        choices=DEMO_CHOICES,
        help_text='Multiple choice as checkbox fields',
        style={'base_template': 'checkbox_multiple.html'},
        validators=[always_invalid]
    )
    multiple_choice_checkbox_field_inline = serializers.MultipleChoiceField(
        choices=DEMO_CHOICES,
        help_text='Multiple choice as checkbox fields, inline',
        style={'base_template': 'checkbox_multiple.html', 'inline': True},
        validators=[always_invalid]
    )
    email_field = serializers.EmailField(
        max_length=None, min_length=None,
        allow_blank=False, help_text='Email field, required',
        validators=[always_invalid]
    )
    integer_field = serializers.IntegerField(
        max_value=None, min_value=None,
        help_text='Integer field',
        validators=[always_invalid]
    )
    file_field = serializers.FileField(
        required=False,
        max_length=None, allow_empty_file=True,
        help_text='File upload field',
        validators=[always_invalid]
    )
    hidden_field = serializers.HiddenField(
        default=timezone.now, help_text='You should not see this rendered!',
        validators=[always_invalid]
    )

    def validate(self, data):
        """This is only run if no fields have errors."""
        raise serializers.ValidationError('This is a non-field error.')
