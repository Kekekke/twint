import twint
from datetime import datetime, timedelta

c = twint.Config()
c.Search = 'зима OR мороз OR холод'
c.Near = 'Yakutsk'
c.Since = (datetime.now() - timedelta(3)).strftime('%Y-%m-%d')
c.Database = "twe.db"

twint.run.Search(c)

