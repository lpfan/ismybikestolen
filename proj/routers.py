from proj import app
from views import index

app.add_url_rule('/index', view_func=index.index_view, methods=['GET',])



