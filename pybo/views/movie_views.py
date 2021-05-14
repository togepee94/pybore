from flask import Blueprint, render_template, url_for, request
from werkzeug.utils import redirect
from pybo.movieapi import Mrank, navermovie
from ..forms import MovieForm


bp = Blueprint('movie', __name__, url_prefix='/movie')


@bp.route('/rank/')
def Movierank():
    rankdata = Mrank()


    return render_template('movie/movierank.html',rankdata=rankdata)

@bp.route('/search/', methods=('GET','POST'))
def Moviesearch():
    form = MovieForm()

    if request.method == "POST" and form.validate_on_submit():
        #post로 들어오고 데이터가 오류가 아니면, 제대로 들어왔으면
        search = navermovie(form.search.data)
        return render_template('movie/navermovie.html', searchmovie=search['items'], form=form)

    return render_template('movie/navermovie.html',form=form)