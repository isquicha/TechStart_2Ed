config = {
    "DEFAULT": {
        "TITLE": "",
        "DEBUG": False,
        "FLASK_ADMIN_NAME": "Admin",
        "FLASK_ADMIN_TEMPLATE_MODE": "bootstrap3",
        "FLASK_ADMIN_SWATCH": "cosmo",
        "SQLALCHEMY_DATABASE_URI": "sqlite:///development.db",
        "SQLALCHEMY_TRACK_MODIFICATIONS": "false",
        "SECRET_KEY": "ÇDSHALIDUA34S43b5i6bDSBAldbasldbLIASBDLIUadbliubibgb3",
        "PASSWORD_SCHEMES": ["pbkdf2_sha512", "md5_crypt"],
        "BABEL_DEFAULT_LOCALE": "pt_br",
        "BABEL_DEFAULT_TIMEZONE": "Brazil/East",
        "EXTENSIONS_PATH": "src.extensions",
        "BLUEPRINTS_PATH": "src.blueprints",
    },
    "DEVELOPMENT": {
        "TEMPLATES_AUTO_RELOAD": True,
        "DEBUG": True,
        "DEBUG_TOOLBAR_ENABLED": True,
        "DEBUG_TB_INTERCEPT_REDIRECTS": False,
        "DEBUG_TB_PROFILER_ENABLED": True,
        "DEBUG_TB_TEMPLATE_EDITOR_ENABLED": True,
        "DEBUG_TB_PANELS": [
            "flask_debugtoolbar.panels.versions.VersionDebugPanel",
            "flask_debugtoolbar.panels.sqlalchemy.SQLAlchemyDebugPanel",
            "flask_debugtoolbar.panels.timer.TimerDebugPanel",
            "flask_debugtoolbar.panels.headers.HeaderDebugPanel",
            "flask_debugtoolbar.panels.request_vars.RequestVarsDebugPanel",
            "flask_debugtoolbar.panels.template.TemplateDebugPanel",
            "flask_debugtoolbar.panels.route_list.RouteListDebugPanel",
            "flask_debugtoolbar.panels.logger.LoggingPanel",
            "flask_debugtoolbar.panels.profiler.ProfilerDebugPanel",
            "flask_debugtoolbar.panels.config_vars.ConfigVarsDebugPanel",
        ],
    },
    "TESTING": {
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
    },
    "PRODUCTION": {
        "DEBUG": False,
        "TESTING": False,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///production.db",
    },
}

extensions = {
    "DEFAULT": [
        "database",
        "authentication",
        # "commands",
        # "admin",
        # "language",
    ],
    "DEVELOPMENT": [
        "flask_debugtoolbar:DebugToolbarExtension",
    ],
    "TESTING": [],
    "PRODUCTION": [],
}

blueprints = {
    "DEFAULT": [
        "api",
    ],
    "DEVELOPMENT": [
        "client",
    ],
    "TESTING": [],
    "PRODUCTION": [
        "client",
    ],
}
