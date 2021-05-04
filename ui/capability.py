def capability_android(
        app_path: str,
        app_package: str,
        app_activity: str,
        platform_version: str = '8.1',
        auto_grand_permission: bool = True,
        orientation: str = 'PORTRAIT'
) -> dict:
    return {
        'platformName': 'Android',
        'platformVersion': platform_version,
        'automationName': 'Appium',
        'appPackage': app_package,
        'appActivity': app_activity,
        'autoGrantPermissions': auto_grand_permission,
        'app': app_path,
        "orientation": orientation
    }
