from wheelcms_axle.themes import Theme, theme_registry

for id, name in (
        ('default', 'Bootstrap'),
        ('amelia', 'Amelia'),
        ('cerulean', 'Cerulean'),
        ('cosmo', 'Cosmo'),
        ('cyborg', 'Cyborg'),
        ('journal', 'Journal'),
        ('readable', 'Readable'),
        ('simplex', 'Simplex'),
        ('slate', 'Slate'),
        ('spruce', 'Spruce'),
        ('superhero', 'Superhero'),
        ('united', 'United')):
    theme_registry.register(Theme(id, name, "%s-bootstrap.min.css"))

