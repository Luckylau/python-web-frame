import wsmeext.pecan as wsme_pecan


def expose(*args, **kwargs):
    if 'rest_content_types' not in kwargs:
        kwargs['rest_content_types'] = ('json',)
    return wsme_pecan.wsexpose(*args, **kwargs)
