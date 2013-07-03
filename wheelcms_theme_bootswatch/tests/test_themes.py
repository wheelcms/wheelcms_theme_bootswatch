from wheelcms_axle.configuration import ConfigurationForm
from ..models import themes

class TestThemes(object):
    def test_themes_form_choices(self):
        f = ConfigurationForm()
        for theme in themes:
            def t():
                assert theme in f.fields['theme'].choices
            yield t
