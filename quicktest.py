from twotest.quicktest import QuickDjangoTest

if __name__ == '__main__':
    QuickDjangoTest(
        apps=("wheelcms_theme_bootswatch",),
        installed_apps=(
            ## these are mostly wheelcms_axle's dependencies
            'wheelcms_axle',
            'wheelcms_theme_bootswatch',
        ),
        ROOT_URLCONF="wheelcms_axle.quicktest_urls",
        ANONYMOUS_USER_ID=-1,
        HAYSTACK_CONNECTIONS={'default':{'engine':'haystack.backends.simple_backend.SimpleEngine'}},
        AUTH_PROFILE_MODULE="wheelcms_axle.WheelProfile",
        CLEANUP_MEDIA=True,
        TEST_MEDIA_ROOT="/tmp/wheelcms_axle_test",
        USE_TZ=True,
        STATIC_URL='/',
        CONTENT_LANGUAGES=(('en', 'English'), ('nl', 'Nederlands')),
        FALLBACK='en',
    )
