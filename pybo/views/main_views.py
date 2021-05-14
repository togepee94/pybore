from flask import Blueprint,render_template,url_for
from pybo.models import Question, Answer, User
from datetime import datetime
from pybo import db
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/test')
def test():
    for i in range(100):
        q = Question(subject='테스트 데이터 [%03d]'%i, content='내용무',create_date=datetime.now())
        db.session.add(q)
    db.session.commit()
    return redirect(url_for('main.index'))


@bp.route('/hello')
def hello_pybo():
    #result = Question.query.filter(Question.id<6).all()
    #result = Question.query.get(1) #id(primary key)가 1번 데이터를 가져옴
    #result = Question.query.filter(Question.subject.like('%무엇%')).all()
    #result = Question.query.filter(Question.username.like('김%')).all()
    #result = Question.query.get(1)
    #result.subject = '파이보 정말 재밌어요' #데이터 변경
    #db.session.delete(result)
    #db.session.commit()

    #q = Question.query.get(2)
    #a = Answer(question = q, content='답변 3번',create_date=datetime.now())
    #db.session.add(a)
    #db.session.commit()

    #2번 질문에 대한 답변 데이터를 가져오세요.
    #q = Question.query.get(5)
    #a = Answer(question=q, content='답변 1번', create_date=datetime.now())
    #a1 = Answer(question=q, content='답변 2번', create_date=datetime.now())
    #a2 = Answer(question=q, content='답변 3번', create_date=datetime.now())
    #a3 = Answer(question=q, content='답변 4번', create_date=datetime.now())
    #a4 = Answer(question=q, content='답변 5번', create_date=datetime.now())
    #result = q.answer_set
    #print(result)
    #db.session.delete(q)
    #db.session.commit()




    #print(result)


    q = Question(subject='pybo가 무엇인가요?', content='pybo에 대해서 알고싶습니다.', create_date=datetime.now())
    q1 = Question(subject='pybo가 힘들 땐 어떻게 해야하나요?', content='도움받을 만할 소스를 알고 싶습니다', create_date=datetime.now())
    q2 = Question(subject='테이블 확인은 어디서하나요?', content='무슨프로그램으로 확인하나요?', create_date=datetime.now())
    q3 = Question(subject='migrate는 무엇인가요?', content='flask db migrate는 어떤 명령어인가요?', create_date=datetime.now())
    q4 = Question(subject='주소를 더 추가하려면 어떻게 하나요?', content='주소를 더 많이 집어넣고 싶습니다.', create_date=datetime.now())
    q5 = Question(subject='날짜를 추가하려면 어떻게 하나요?', content='현재 날짜를 추가하고 싶어요.', create_date=datetime.now())
    q6 = Question(subject='오류가 나요', content='에러 원인을 찾는 법을 알고싶습니다.', create_date=datetime.now())
    q7 = Question(subject='파이썬 활용법은?', content='파이썬으로 무엇을 할 수 있나요?', create_date=datetime.now())
    q8 = Question(subject='수정된 시간도 추가가 가능한가요?', content='질문 수정 시간을 추가하고 싶습니다.', create_date=datetime.now())
    q9 = Question(subject='flask란 무엇인가요?', content='flask에 대해서 알고싶습니다.', create_date=datetime.now())
    db.session.add(q)
    db.session.add(q1)
    db.session.add(q2)
    db.session.add(q3)
    db.session.add(q4)
    db.session.add(q5)
    db.session.add(q6)
    db.session.add(q7)
    db.session.add(q8)
    db.session.add(q9)

    db.session.commit()



    return 'Hello, Pybo!'

#@bp.route('/')
#def index():
#    question_list= Question.query.order_by(Question.create_date.desc())
#    return render_template('question/question_list.html',question_list=question_list)



@bp.route('/')
def index():
    return redirect(url_for('question._list'))


