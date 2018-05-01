# drf-form-bootstrap-4

Bootstrap 4 templates for [Django Rest Framework `render_form` tag](http://www.django-rest-framework.org/topics/html-and-forms/).

## Requirements

Tested with Django 2.0 and Python 3.6. Probably works in earlier versions.

## Installation

From PyPI:

```
todo
```

Add `drfformbootstrap4` to your `INSTALLED_APPS` setting.

```
INSTALLED_APPS = (
    ...
    'drfformbootstrap4',
)
```

## Usage

Like the template packs in Django Rest Framework, this supports three layouts:

##### Vertical

    <form method="POST" novalidate>
      {% csrf_token %}
      {% render_form serializer template_pack='drfformbootstrap4/vertical' %}
      <div class="row">
        <div class="col text-right">
          <input class="btn btn-primary" type="submit" value="Submit">
        </div>
      </div>
    </form>


##### Horizontal


    <form method="POST" novalidate>
      {% csrf_token %}
      {% render_form serializer template_pack='drfformbootstrap4/horizontal' %}
      <div class="row">
        <div class="col text-right">
          <input class="btn btn-primary" type="submit" value="Submit">
        </div>
      </div>
    </form>



##### Inline

Note that `inline` is less well-tested than the others, and at the moment the error states don't  render properly. If this is a problem for you, submit an issue (or even better, a pull request).

    <form method="POST" novalidate class="form-inline">
      {% csrf_token %}
      {% render_form serializer template_pack='drfformbootstrap4/inline' %}
      <div class="row">
        <div class="col text-right">
          <input class="btn btn-primary" type="submit" value="Submit">
        </div>
      </div>
    </form>

### Additional Options

To display a field as text instead of as a field:

```
style={'class': 'form-control-plaintext'}
```

For inline checkboxes and radio buttons:

```
style={'inline': True}
```

Prepend/append text for inputs:

```
style={
    'prepend': 'prepend',
    'append': 'append',
}
```

## Development

Pretty standard: fork this repo, make changes, make a GitHub pull request.

There are demo pages showing a variety of form fields and layouts. To use it, first install its dependencies:

```
pip install django-debug-toolbar
```

Then run the server:

```
make runserver
```

When using this `runserver`, you don't need to install `drfformbootstrap4` into your virtualenv before seeing changes. However if you want to see your changes reflected in a different application using the same virtualenv, install it with:

```
pip install .
```

## License

MIT

&copy; 2018 Matthew Fox
