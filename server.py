from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    send_from_directory,
)
from article import Article
import os
from database import Database


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


@app.route("/")
@app.route("/index")
def index():
    return render_template("ruwiki.html")


database = {
    'sonic': {
        'title_article':'Ёж Соник',
        'text_article': '''Ёж Со́ник (яп. ソニック・ザ・ヘッジホッグ Соникку дза Хэдзихоггу, англ. Sonic the Hedgehog) — главный персонаж
    серии видеоигр Sonic the Hedgehog от компании Sega, а также созданных на её основе комиксов, мультсериалов и полнометражных фильмов.
    Соник — синий антропоморфный ёж, созданный художником Наото Осимой, программистом Юдзи Накой и дизайнером Хирокадзу Ясухарой. Во время 
    разработки было предложено множество образов главного героя будущей игры, но разработчики остановились на ёжике синего цвета. Своё имя Соник 
    получил за способность бегать на сверхзвуковых скоростях (англ. sonic — «звуковой; со скоростью звука»). Геймплей за Соника в большинстве игр серии 
    Sonic the Hedgehog заключается в быстром прохождении уровней и битвах с врагами, для атаки которых Соник сворачивается в шар во время прыжка. Немаловажную
    роль для Соника играют золотые кольца, служащие ему в качестве защиты. Главным антагонистом героя является доктор Эггман, который хочет захватить мир и построить 
    свою империю «Эггманленд».После выхода одноимённой игры с его участием Соник быстро стал популярным во всём мире и положил начало крупной медиафраншизе. Персонаж 
    стал талисманом компании Sega, которым остаётся и сейчас, сменив Алекса Кидда, бывшего неофициальным маскотом компании до 1990 года. На ноябрь 2014 года было продано
    свыше 150 миллионов экземпляров игр серии о Сонике[4]. Помимо компьютерных игр, ёж Соник является главным героем комиксов, книг, ряда мультсериалов и полнометражных аниме и фильмов.''' ,
        'article_image_title':'Соник',
        'article_image_path':'images/Sonic.png'
    },

    'Ехидна_Наклз':{
        'title_article':'Ехидна Наклз',
        'text_article': '''Ехидна Наклз[2] (яп. ナックルズ・ザ・エキドゥナ Наккурудзу дза Экидуна, англ. Knuckles the Echidna) 
    — персонаж видеоигр, телешоу и комиксов серии Sonic the Hedgehog. Его прозвища — «Knuckie», «Rad Red», «Red Storm», 
    «Knux», и «Knucklehead». Создан Такаси Юдой. Первое появление — игра Sonic the Hedgehog 3. Наклз — красная 
    антропоморфная ехидна, чьи иглы похожи на причёску из многочисленных коротких дредов. Можно заметить некоторое 
    различие между игровым и неигровым спрайтами Наклза. В играх играбельный Наклз предстаёт в ярко-красном цвете с 
    зелёными носками, а неиграбельный — как красно-розовый с жёлтыми носками. По официальным данным Наклзу 16 лет.''' ,
        'article_image_title':'Ехидна Наклз',
        'article_image_path':'images/Nackles.png'
    },

    'Чёрный_американский_стриж':{
        'title_article':'Чёрный американский стриж',
        'text_article': '''Чёрный американский стриж[1] (лат. Cypseloides niger) — вид птиц семейства стрижиных. Самый крупный стриж к северу от Мексики и самый северный из американских стрижей. Обитает вдоль тихоокеанского побережья Северной Америки от Аляски до Мексики, встречается также на атлантическом побережье Мексики. В Центральной Америке птицы обитают на территории от Коста-Рики до Гватемалы и Гондураса, на многих островах Вест-Индии. Точные места зимовок чёрного американского стрижа неизвестны, миграция может составлять до 7 тысяч километров. У птиц крепкое тело и длинные широкие крылья, хвост с неглубоким, но хорошо заметным разрезом. Оперение чёрное, голова заметно светлее, в нижней части кончики перьев часто окрашены в белый цвет. Чёрные американские стрижи охотятся на летающих насекомых, при этом собираются в большие стаи и могут улетать за несколько километров от гнездовых колоний. Птицы летают настолько высоко, что их часто не видно с земли. Традиционно устраивают гнёзда в одних и тех же влажных и недоступных местах, часто на скалах высоко в горах, около водопадов. Основным материалом при строительстве гнезда является мох, а также небольшое количество веточек, сосновых иголок, папоротников или водорослей. Гнездо скрепляется грязью. В кладке обычно одно яйцо, инкубационный период составляет 22—32 дня. Птенцы появляются на свет голыми и беспомощными, через 45—52 дня вылетают из гнезда и больше в этом сезоне к нему не возвращаются.''' ,
        'article_image_title':'Чёрный американский стриж',
        'article_image_path':'images/falls.jpg'
    },    

}

@app.route("/article/<name>")
def article(name):
    article = Database.find_article_by_title(name)
    if article is None:
        return f"<h1>Статьи '{name}' не существует!</h1>"

    return render_template('article.html', article=article)


@app.route("/uploads/<filename>")
def uploaded_photo(filename):
    return send_from_directory(
        app.config["UPLOAD_FOLDER"],
        filename
    )

 
@app.route('/add_article', methods=['GET', 'POST'])
def add_article():
    if request.method == 'GET':
        return render_template('add_article.html')
    
    # POST-запрос далее
    title = request.form.get("title")
    if title is None:
        flash("Для статьи необходимо название")
        redirect(request.url)
        return

    content = request.form.get("content")
    if content is None:
        flash("Для статьи необходим текст")
        redirect(request.url)
        return

    photo = request.files.get("photo")
    if photo is None or photo.filename is None:
        flash("Для статьи нужна фотография")
        redirect(request.url)
        return

    photo.save(app.config["UPLOAD_FOLDER"] + photo.filename)
    article = Article(title, content, photo.filename)
    Database.save(article)

    return redirect(url_for('show_articles'))


@app.route("/articles")
def show_articles():
    articles = Database.get_all_articles()

    groups = []
    k = 3
    for i in range(0, len(articles), k):
        groups.append(articles[i:i+k])

    #range(0, 10, 3) => 0, 3, 6, 9

    #0:3
    #3:6
    #6:9
    #9:12

    return render_template('articles.html', groups=groups)


if __name__ == '__main__':
    app.run(debug=True)