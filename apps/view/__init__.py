from flask_mail import Mail
from flask_cache import Cache
cache = Cache(config={'CACHE_TYPE': 'simple'})
mail = Mail()