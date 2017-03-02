app = {
    'root': 'webdemo.api.controllers.root.RootController',
    'modules': ['webdemo.api'],
    'debug': True,
}
logging = {
    'root': {'level': 'INFO', 'handlers': ['console']},
    'loggers': {
        'webdemo': {'level': 'INFO', 'handlers': ['console']}
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        }
    },
    'formatters': {
        'simple': {
            'format': ('%(asctime)s %(levelname)-5.5s [%(name)s]'
                       '[%(threadName)s] %(message)s')
        }
    }
}
