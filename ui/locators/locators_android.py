from appium.webdriver.common.mobileby import MobileBy


class AndroidBasePageLocators(object):
    BUTTON_KEYBOARD = (MobileBy.ID, 'ru.mail.search.electroscope:id/keyboard')
    BUTTON_BURGER_TEMPLATE = (MobileBy.ID, 'ru.mail.search.electroscope:id/assistant_menu_{}')


class MainPageLocators(AndroidBasePageLocators):
    LABEL_FACT_CARD_CONTENT = (MobileBy.ID, 'ru.mail.search.electroscope:id/item_dialog_fact_card_content_text')
    LABEL_DIALOG_ITEM = (
        MobileBy.XPATH,
        '//*[@resource-id = "ru.mail.search.electroscope:id/dialog_item" and @text = "{}"]'
    )
    LABEL_PLAYED_NAME = (MobileBy.ID, 'ru.mail.search.electroscope:id/player_track_name')
    LABEL_FACT_TITLE_TEMPLATE = (
        MobileBy.XPATH,
        '//android.widget.TextView'
        '[@resource-id = "ru.mail.search.electroscope:id/item_dialog_fact_card_title" and @text = "{}"]'
    )

    INPUT_TEXT = (MobileBy.ID, 'ru.mail.search.electroscope:id/input_text')
    BUTTON_SUBMIT = (MobileBy.ID, 'ru.mail.search.electroscope:id/text_input_action')
    BUTTON_POPULATION = (
        MobileBy.XPATH,
        '//android.widget.TextView['
        '@resource-id = "ru.mail.search.electroscope:id/item_suggest_text" and '
        '@text = "численность населения россии"]'
    )


class SettingsPageLocators(AndroidBasePageLocators):
    BUTTON_GO_MAIN = (
        MobileBy.XPATH,
        '//android.widget.LinearLayout[@resource-id = "ru.mail.search.electroscope:id/user_settings_toolbar"]/'
        'android.widget.ImageButton'
    )

    BUTTON_SOURCES_NEWS = (MobileBy.ID, 'ru.mail.search.electroscope:id/user_settings_field_news_sources')
    BUTTON_ABOUT_APP = (MobileBy.ID, 'ru.mail.search.electroscope:id/user_settings_about')


class SourcesNewsSettingsPageLocators(SettingsPageLocators):
    BUTTON_SOURCES_BACK = (
        MobileBy.XPATH,
        '//android.widget.LinearLayout[@resource-id = "ru.mail.search.electroscope:id/news_sources_toolbar"]/'
        'android.widget.ImageButton'
    )
    BUTTON_SELECT_SOURCES = (
        MobileBy.XPATH,
        '//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]'
    )

    CHECKED_ITEM_SOURCES = (
        MobileBy.XPATH,
        f'{BUTTON_SELECT_SOURCES[1]}/android.widget.ImageView'
    )


class AboutApplicationLocators(SettingsPageLocators):
    LABEL_APPLICATION_VERSION = (MobileBy.ID, 'ru.mail.search.electroscope:id/about_version')
    LABEL_COPYRIGHT = (MobileBy.ID, 'ru.mail.search.electroscope:id/about_copyright')
