from datetime import date

AUTHOR = "Leo Gagliardi"
SITENAME = "datajitsu"
SITESUBTITLE = "Leo Gagliardi — Data Science"
SITEURL = ""
CURRENT_YEAR = date.today().year


PATH = "content"
ARTICLE_PATHS = ["articles"]
TIMEZONE = "Europe/Paris"
DEFAULT_LANG = "fr"

THEME = "theme"

# URLs
ARTICLE_URL = "articles/{slug}/"
ARTICLE_SAVE_AS = "articles/{slug}/index.html"
ARCHIVES_SAVE_AS = ""

# Feeds off for local dev; enable + set real SITEURL before publishing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

STATIC_PATHS = ["images"]

DEFAULT_DATE_FORMAT = "%B %Y"

RELATIVE_URLS = True
