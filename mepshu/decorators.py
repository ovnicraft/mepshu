
from functools import wraps

def check_type(f):
    """
    check type session allowed
    """
    @wraps(f)
    def check(*fargs):
        obj = fargs[0]
        if not obj.MAPPING_ENTITIES[obj.entity_path] == obj.session.type:
            raise TypeError('Not valid key to action requested.')
        return f(*fargs)
    return check
