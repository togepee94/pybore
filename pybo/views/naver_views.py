from flask import Blueprint, render_template, url_for, request
from werkzeug.utils import redirect
from pybo.naverapi import naverbook
from ..forms import NaverBookForm

bp = Blueprint('naver', __name__, url_prefix='/naver')


@bp.route('/book/', methods=('GET','POST'))
def Naverbook():
    form = NaverBookForm()

    if request.method == "POST" and form.validate_on_submit():
        #post로 들어오고 데이터가 오류가 아니면, 제대로 들어왔으면
        result = naverbook(form.search.data)
        return render_template('naver/naverbook.html', bookinfo_list=result['items'], form=form)

    return render_template('naver/naverbook.html',form=form)

