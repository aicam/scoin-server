from django.shortcuts import render
from django.http import HttpResponse
from .models import advertisement
from .models import Comments
from .models import Users
from .models import AD_pics
from .models import codes
from .models import ADCategory
from .models import users_payments
from .models import notifications
from .models import Categories
from .models import medals
from .models import game_bombs_data
from .models import game_bombs
from django.utils import timezone
from datetime import datetime, timedelta
from .models import IpAddresses
from .Games_awars import game_awards
from django.views.decorators.csrf import csrf_exempt
import random
import json
from .Questions import questions


##
## extra Methods
##
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


##
## /extra Methods
##

def index(request):
    return HttpResponse('<h>hello</h>')


def category(request):
    user_id = request.GET['userID']


def HomePage(request):
    user_id = request.GET['userID']
    json_data = {}
    most_popular = []
    freesuggestions = []
    bombs = []
    product = []
    restuarant = []
    services = []
    just_scoin = []
    copen = []
    dailysuggestions = []
    counter = 0

    # notification view
    json_data.update({'notif_check': 1, 'notif_title': 'سلام', 'notif_text': 'خوش آمدید'})

    for row_data in advertisement.objects.raw(
            "select * from requests_advertisement as rad ,requests_dailysuggestions as rda where rad.advertisement_id = rda.ad_id"):
        remaining = row_data.time
        this_section_data = {'id': row_data.advertisement_id, 'title': row_data.title, 'pic': row_data.pic_link,
                             'timers': row_data.time, 'active': row_data.active}
        dailysuggestions.append(this_section_data)
        counter += 1
    json_data['dailysuggestions'] = dailysuggestions
    counter = 0
    for row_data in advertisement.objects.raw("select * from requests_advertisement order by rate DESC LIMIT 15"):
        remaining = row_data.time - timezone.now()
        time_data = ""
        typeoftime = 0
        if (remaining.days < 0):
            time_data = 'end'
            typeoftime = 0
        elif (remaining.days > 0):
            time_data = remaining.days
            typeoftime = 1
        else:
            time_data = remaining.seconds
            typeoftime = 2
        this_section_data = {'id': row_data.advertisement_id, 'title': row_data.title, 'pic': row_data.pic_link,
                             'timers': time_data, 'typeoftime': typeoftime, 'old_cost': row_data.old_cost,
                             'cost': row_data.cost, 'off': row_data.off, 'min_level': row_data.minlevel,
                             'Scoin_available': row_data.Scoin_available, 'Scoin_cost': row_data.Scoin_cost,
                             'bought': row_data.bought}
        most_popular.append(this_section_data)
        counter += 1
    json_data['most_popular'] = most_popular
    counter = 0
    for row_data in advertisement.objects.raw(
            "select * from requests_advertisement as ad inner join requests_adcategory as rad where rad.category_id = 49 and ad.advertisement_id = rad.ad_id LIMIT 8"):
        remaining = row_data.time - timezone.now()
        time_data = ""
        typeoftime = 0
        if (remaining.days < 0):
            time_data = 'end'
            typeoftime = 0
        elif (remaining.days > 0):
            time_data = remaining.days
            typeoftime = 1
        else:
            time_data = remaining.seconds
            typeoftime = 2
        this_section_data = {'id': row_data.advertisement_id, 'title': row_data.title, 'pic': row_data.pic_link,
                             'timers': time_data, 'typeoftime': typeoftime, 'old_cost': row_data.old_cost,
                             'cost': row_data.cost, 'off': row_data.off, 'min_level': row_data.minlevel,
                             'Scoin_available': row_data.Scoin_available, 'Scoin_cost': row_data.Scoin_cost,
                             'bought': row_data.bought}
        services.append(this_section_data)
        counter += 1
    json_data['services'] = services
    counter = 0
    for row_data in advertisement.objects.raw(
            "select * from requests_advertisement as ad inner join requests_adcategory as rad where rad.category_id = 50 and ad.advertisement_id = rad.ad_id LIMIT 8"):
        remaining = row_data.time - timezone.now()
        time_data = ""
        typeoftime = 0
        if (remaining.days < 0):
            time_data = 'end'
            typeoftime = 0
        elif (remaining.days > 0):
            time_data = remaining.days
            typeoftime = 1
        else:
            time_data = remaining.seconds
            typeoftime = 2
        this_section_data = {'id': row_data.advertisement_id, 'title': row_data.title, 'pic': row_data.pic_link,
                             'timers': time_data, 'typeoftime': typeoftime, 'old_cost': row_data.old_cost,
                             'cost': row_data.cost, 'off': row_data.off, 'min_level': row_data.minlevel,
                             'Scoin_available': row_data.Scoin_available, 'Scoin_cost': row_data.Scoin_cost,
                             'bought': row_data.bought}
        bombs.append(this_section_data)
        counter += 1
    json_data['bomb'] = bombs
    counter = 0
    for row_data in advertisement.objects.raw(
            "select * from requests_advertisement as ad inner join requests_adcategory as rad where rad.category_id = 51 and ad.advertisement_id = rad.ad_id LIMIT 8"):
        remaining = row_data.time - timezone.now()
        time_data = ""
        typeoftime = 0
        if (remaining.days < 0):
            time_data = 'end'
            typeoftime = 0
        elif (remaining.days > 0):
            time_data = remaining.days
            typeoftime = 1
        else:
            time_data = remaining.seconds
            typeoftime = 2
        this_section_data = {'id': row_data.advertisement_id, 'title': row_data.title, 'pic': row_data.pic_link,
                             'timers': time_data, 'typeoftime': typeoftime, 'old_cost': row_data.old_cost,
                             'cost': row_data.cost, 'off': row_data.off, 'min_level': row_data.minlevel,
                             'Scoin_available': row_data.Scoin_available, 'Scoin_cost': row_data.Scoin_cost,
                             'bought': row_data.bought}
        restuarant.append(this_section_data)
        counter += 1
    json_data['restuarant'] = restuarant
    counter = 0
    for row_data in advertisement.objects.raw(
            "select * from requests_advertisement as ad inner join requests_adcategory as rad where rad.category_id = 52 and ad.advertisement_id = rad.ad_id LIMIT 8"):
        remaining = row_data.time - timezone.now()
        time_data = ""
        typeoftime = 0
        if (remaining.days < 0):
            time_data = 'end'
            typeoftime = 0
        elif (remaining.days > 0):
            time_data = remaining.days
            typeoftime = 1
        else:
            time_data = remaining.seconds
            typeoftime = 2
        this_section_data = {'id': row_data.advertisement_id, 'title': row_data.title, 'pic': row_data.pic_link,
                             'timers': time_data, 'typeoftime': typeoftime, 'old_cost': row_data.old_cost,
                             'cost': row_data.cost, 'off': row_data.off, 'min_level': row_data.minlevel,
                             'Scoin_available': row_data.Scoin_available, 'Scoin_cost': row_data.Scoin_cost,
                             'bought': row_data.bought}
        just_scoin.append(this_section_data)
        counter += 1
    json_data['just_scoin'] = just_scoin
    counter = 0
    for row_data in advertisement.objects.raw(
            "select * from requests_advertisement as ad inner join requests_adcategory as rad where rad.category_id = 53 and ad.advertisement_id = rad.ad_id LIMIT 8"):
        remaining = row_data.time - timezone.now()
        time_data = ""
        typeoftime = 0
        if (remaining.days < 0):
            time_data = 'end'
            typeoftime = 0
        elif (remaining.days > 0):
            time_data = remaining.days
            typeoftime = 1
        else:
            time_data = remaining.seconds
            typeoftime = 2
        this_section_data = {'id': row_data.advertisement_id, 'title': row_data.title, 'pic': row_data.pic_link,
                             'timers': time_data, 'typeoftime': typeoftime, 'old_cost': row_data.old_cost,
                             'cost': row_data.cost, 'off': row_data.off, 'min_level': row_data.minlevel,
                             'Scoin_available': row_data.Scoin_available, 'Scoin_cost': row_data.Scoin_cost,
                             'bought': row_data.bought}
        copen.append(this_section_data)
        counter += 1
    json_data['copen'] = copen
    counter = 0
    for row_data in advertisement.objects.raw(
            "select * from requests_advertisement as ad inner join requests_adcategory as rad where rad.category_id = 54 and ad.advertisement_id = rad.ad_id LIMIT 8"):
        remaining = row_data.time - timezone.now()
        time_data = ""
        typeoftime = 0
        if (remaining.days < 0):
            time_data = 'end'
            typeoftime = 0
        elif (remaining.days > 0):
            time_data = remaining.days
            typeoftime = 1
        else:
            time_data = remaining.seconds
            typeoftime = 2
        this_section_data = {'id': row_data.advertisement_id, 'title': row_data.title, 'pic': row_data.pic_link,
                             'timers': time_data, 'typeoftime': typeoftime, 'old_cost': row_data.old_cost,
                             'cost': row_data.cost, 'off': row_data.off, 'min_level': row_data.minlevel,
                             'Scoin_available': row_data.Scoin_available, 'Scoin_cost': row_data.Scoin_cost,
                             'bought': row_data.bought}
        freesuggestions.append(this_section_data)
        counter += 1
    json_data['freesuggestions'] = freesuggestions
    counter = 0
    for row_data in advertisement.objects.raw(
            "select * from requests_advertisement as ad inner join requests_adcategory as rad where rad.category_id = 55 and ad.advertisement_id = rad.ad_id LIMIT 8"):
        remaining = row_data.time - timezone.now()
        time_data = ""
        typeoftime = 0
        if (remaining.days < 0):
            time_data = 'end'
            typeoftime = 0
        elif (remaining.days > 0):
            time_data = remaining.days
            typeoftime = 1
        else:
            time_data = remaining.seconds
            typeoftime = 2
        this_section_data = {'id': row_data.advertisement_id, 'title': row_data.title, 'pic': row_data.pic_link,
                             'timers': time_data, 'typeoftime': typeoftime, 'old_cost': row_data.old_cost,
                             'cost': row_data.cost, 'off': row_data.off, 'min_level': row_data.minlevel,
                             'Scoin_available': row_data.Scoin_available, 'Scoin_cost': row_data.Scoin_cost,
                             'bought': row_data.bought}
        product.append(this_section_data)
        counter += 1
    json_data['product'] = product
    return HttpResponse(json.dumps(json_data, ensure_ascii=False))


def location(request):
    counter = 0
    most_popular = []
    for row_data in advertisement.objects.raw("select * from requests_advertisement order by rate DESC LIMIT 15"):
        this_section_data = {'id': row_data.advertisement_id, 'title': row_data.title, 'pic': row_data.pic_link,
                             'timers': row_data.time}
        most_popular.append(this_section_data)
        counter += 1
    json_data = {'nearest': most_popular}
    return HttpResponse(json.dumps(json_data, ensure_ascii=False))


def ADinfo(request):
    json_data = {}
    user_id = request.GET['ad_id']
    for row_data in advertisement.objects.raw("select * from requests_advertisement where advertisement_id=" + user_id):
        remaining = row_data.time - timezone.now()
        time_data = ""
        typeoftime = 0
        if (remaining.days < 0):
            time_data = 'end'
            typeoftime = 0
        elif (remaining.days > 0):
            time_data = remaining.days
            typeoftime = 1
        else:
            time_data = remaining.seconds
            typeoftime = 2
        json_data = {'id': row_data.advertisement_id, 'title': row_data.title, 'pic': row_data.pic_link,
                     'timers': time_data, 'typeoftime': typeoftime, 'old_cost': row_data.old_cost,
                     'cost': row_data.cost, 'off': row_data.off, 'min_level': row_data.minlevel,
                     'Scoin_available': row_data.Scoin_available, 'Scoin_cost': row_data.Scoin_cost,
                     'bought': row_data.bought, 'rate': round(row_data.rate, 1), 'description': row_data.description,
                     'ad_link': row_data.link}
    categories = []
    categories_id = 1
    related = []
    for row_data in ADCategory.objects.raw(
            'select * from requests_adcategory as rad, requests_categories as rca where rad.ad_id=' + user_id + ' and rad.category_id=rca.id'):
        categories.append({'name': row_data.name})
        categories_id = row_data.category_id
    json_data.update({'category': categories})
    for row_data in advertisement.objects.raw(
            'select * from requests_adcategory as rad, requests_advertisement as rca where rad.category_id=' + str(categories_id) + ' and rca.advertisement_id = rad.ad_id LIMIT 7'):
        remaining = row_data.time - timezone.now()
        time_data = ""
        typeoftime = 0
        if (remaining.days < 0):
            time_data = 'end'
            typeoftime = 0
        elif (remaining.days > 0):
            time_data = remaining.days
            typeoftime = 1
        else:
            time_data = remaining.seconds
            typeoftime = 2
        this_section_data = {'id': row_data.advertisement_id, 'title': row_data.title, 'pic': row_data.pic_link,
                             'timers': time_data, 'typeoftime': typeoftime, 'old_cost': row_data.old_cost,
                             'cost': row_data.cost, 'off': row_data.off, 'min_level': row_data.minlevel,
                             'Scoin_available': row_data.Scoin_available, 'Scoin_cost': row_data.Scoin_cost,
                             'bought': row_data.bought}
        related.append(this_section_data)
    json_data['related'] = related
    pic_links = []
    for row_data in AD_pics.objects.raw('select * from requests_AD_pics where ad_id=' + user_id):
        pic_links.append({'url': row_data.pic_link})
    json_data['pic_links'] = pic_links
    return HttpResponse(json.dumps(json_data, ensure_ascii=False))


def more(request):
    json_data = {}
    category = request.GET['option']
    category = int(category)
    offset = int(request.GET['offset'])
    items = []
    this_section_data = {}
    if category != 5:
        for row_data in advertisement.objects.raw(
                "select * from requests_advertisement as rad,requests_adcategory as radc where radc.category_id= " + str(
                    category) + " and rad.advertisement_id = radc.ad_id LIMIT 10 OFFSET " + str(
                    offset * 10)):
            remaining = row_data.time - timezone.now()
            time_data = ""
            typeoftime = 0
            if (remaining.days < 0):
                time_data = 'end'
                typeoftime = 0
            elif (remaining.days > 0):
                time_data = remaining.days
                typeoftime = 1
            else:
                time_data = remaining.seconds
                typeoftime = 2
            this_data = {'id': row_data.advertisement_id, 'title': row_data.title, 'pic': row_data.pic_link,
                         'timers': time_data, 'short_desc': row_data.short_description,
                         'typeoftime': typeoftime, 'off': row_data.off, 'cost': row_data.cost,
                         'old_cost': row_data.old_cost, 'bought': row_data.bought, 'rate': round(row_data.rate, 1)}
            items.append(this_data)
    if category == 5:
        for row_data in advertisement.objects.raw(
                "select * from requests_advertisement order by rate asc LIMIT 10 OFFSET " + str(offset * 10)):
            remaining = row_data.time - timezone.now()
            time_data = ""
            typeoftime = 0
            if (remaining.days < 0):
                time_data = 'end'
                typeoftime = 0
            elif (remaining.days > 0):
                time_data = remaining.days
                typeoftime = 1
            else:
                time_data = remaining.seconds
                typeoftime = 2
            this_data = {'id': row_data.advertisement_id, 'title': row_data.title, 'pic': row_data.pic_link,
                         'timers': time_data, 'short_desc': row_data.short_description,
                         'typeoftime': typeoftime, 'off': row_data.off, 'cost': row_data.cost,
                         'old_cost': row_data.old_cost, 'bought': row_data.bought, 'rate': round(row_data.rate, 1)}
            items.append(this_data)
    json_data['items'] = items
    return HttpResponse(json.dumps(json_data, ensure_ascii=False))


def submit_rate(request):
    ad_id = request.GET['ad_id']
    rate = request.GET['rate']
    adv = advertisement.objects.get(advertisement_id=ad_id)
    new_rate = ((adv.rate) * int(adv.rate_count) + int(rate)) / (adv.rate_count + 1)
    adv.rate = new_rate
    adv.rate_count = adv.rate_count + 1
    adv.save()
    json_data = {'success': True}
    return HttpResponse(new_rate)


def comment(request):
    comment_get = request.GET['cm']
    adID = request.GET['ad_id']
    username = Users.objects.get(username=request.GET['username']).userID
    cm = Comments(comment=comment_get, ad_id=adID, user_id=username)
    cm.save()
    return HttpResponse('submit')


def show_comment(request):
    ad_id = request.GET['ad_id']
    offset = int(request.GET['offset'])
    json_data = {}
    items = []
    for row_data in Comments.objects.raw(
            "select * from requests_comments AS rc,requests_users AS ru where rc.ad_id=" + ad_id + " and rc.user_id = ru.userID" + " LIMIT 5 OFFSET " + str(
                offset * 5)):
        this_section_data = {'comment': row_data.comment, 'username': row_data.username}
        items.append(this_section_data)
    json_data['comments'] = items
    return HttpResponse(json.dumps(json_data, ensure_ascii=False))


def Search_data(request):
    json_data = {}
    indexstr = request.GET['indexstr']
    offset = int(request.GET['offset'])
    items = []
    this_section_data = {}
    for row_data in advertisement.objects.filter(short_description__icontains=indexstr)[offset:offset + 10]:
        remaining = row_data.time - timezone.now()
        time_data = ""
        typeoftime = 0
        if (remaining.days < 0):
            time_data = 'end'
            typeoftime = 0
        elif (remaining.days > 0):
            time_data = remaining.days
            typeoftime = 1
        else:
            time_data = remaining.seconds
            typeoftime = 2
        this_data = {'id': row_data.advertisement_id, 'title': row_data.title, 'pic': row_data.pic_link,
                     'timers': time_data, 'short_desc': row_data.short_description,
                     'typeoftime': typeoftime, 'off': row_data.off, 'cost': row_data.cost,
                     'old_cost': row_data.old_cost, 'bought': row_data.bought, 'rate': round(row_data.rate, 1)}
        items.append(this_data)
    json_data['items'] = items
    return HttpResponse(json.dumps(json_data, ensure_ascii=False))


# Accounts methods
def save_session(request):
    request.session['time_loged'] = str(timezone.now())


def register_user(request):
    user_ip = get_client_ip(request)
    reagent = request.GET['reagent']
    # time_loged = request.session.get('time_loged')
    # time_loged = datetime.strptime(time_loged, '%Y-%m-%d %H:%M:%S.%f')
    a = Users.objects.filter(username=request.GET['username']).exists()
    # if time_loged == None or time_loged + timedelta(seconds=5) < timezone.now():
    new_scoin = 500
    if reagent != 'null' and Users.objects.filter(username=request.GET['reagent']).exists():
        new_scoin = 600
        a = 4
        reagent_user = Users.objects.get(username=reagent)
        reagent_user.Scoin += 100
        reagent_user.save()
    usersql = Users(username=request.GET['username'], Scoin=new_scoin, name=request.GET['name'], notifications=0,
                    sex=request.GET['sex'], phonenumber=request.GET['phonenumber'], level_grow=200, level=0)
    usersql.save()
    # save_session(request)
    return HttpResponse(a)


# games
from django.template import loader
from .models import Game_rates
from .models import Games
from .models import game_bombs_data

def games(request):
    username = request.GET['username']
    page_data = {}
    medal_ids = []
    for row_data in medals.objects.filter(username=username):
        medal_ids.append(row_data.pic_link)
    page_data.update({'medals' : medal_ids})
    one_week_later = timezone.now() + timedelta(days=-7)
    print(one_week_later)
    weekly_rates_array = []
    one_week_later = timezone.now() + timedelta(days=-7)
    cnt = 1
    for item in Game_rates.objects.raw('SELECT game_id,id,username,SUM(rate) as total_rate FROM requests_game_rates WHERE time > "' + one_week_later.strftime("%Y-%m-%d %H:%M:%S.%f") + '" GROUP BY username ORDER BY total_rate DESC limit 5'):
        weekly_rates_array.append({'username': item.username, 'rate': item.total_rate, 'counter': cnt})
        cnt += 1
    page_data.update({'weekly_rates' : weekly_rates_array})
    one_month_later = timezone.now() + timedelta(days=-30)
    month_rates_array = []
    cnt = 1
    for row_data in Game_rates.objects.raw(
            'SELECT game_id,id,username,SUM(rate) as total_rate FROM requests_game_rates WHERE time > "' + one_month_later.strftime("%Y-%m-%d %H:%M:%S.%f") + '" GROUP BY username ORDER BY total_rate DESC limit 5'):
        month_rates_array.append({'username': row_data.username, 'rate': row_data.total_rate, 'counter':cnt})
        cnt += 1
    page_data.update({'month_rates': month_rates_array})
    events = []
    for row_data in game_bombs_data.objects.all():
        events.append({'start_time': str(row_data.time_start), 'end_time': str(row_data.time_end),
                       'max': row_data.capacity, 'award': row_data.award, 'link': row_data.link,'cost':row_data.cost})
    page_data.update({'events': events})
    page_data.update({'scoin' : Users.objects.get(username=username).Scoin})
    page_data.update({'username':username})
    template = loader.get_template('Games/index.html')
    return HttpResponse(json.dumps(page_data))

def game_page(request):
    username = request.GET['username']
    game_id = request.GET['game_id']
    page_data = {}
    medal_ids = []
    page_data.update({'awards':game_awards[int(game_id)]})
    for row_data in medals.objects.filter(username=username):
        medal_ids.append({'id':row_data.medal_id + '.gif'})
    page_data.update({'medals' : medal_ids})
    one_week_later = timezone.now() + timedelta(days=-7)
    weekly_rates_array = []
    cnt = 1
    for row_data in Game_rates.objects.raw('SELECT game_id,id,username,SUM(rate) as total_rate FROM requests_game_rates WHERE time > "' + one_week_later.strftime("%Y-%m-%d %H:%M:%S.%f") + '" and game_id= ' + game_id + ' GROUP BY username ORDER BY total_rate DESC limit 5'):
        weekly_rates_array.append({'username' : row_data.username,'rate':row_data.total_rate,'cnt':cnt})
        cnt += 1
    page_data.update({'weekly_rates' : weekly_rates_array})
    one_month_later = timezone.now() + timedelta(days=-30)
    month_rates_array = []
    cnt = 1
    for row_data in Game_rates.objects.raw(
            'SELECT game_id,id,username,SUM(rate) as total_rate FROM requests_game_rates WHERE time > "' + one_month_later.strftime("%Y-%m-%d %H:%M:%S.%f") + '" and game_id= ' + game_id + ' GROUP BY username ORDER BY total_rate DESC limit 5'):
        month_rates_array.append({'username': row_data.username, 'rate': row_data.total_rate,'cnt':cnt})
        cnt += 1
    page_data.update({'month_rates': month_rates_array})
    player_rank = 0
    for row_data in Game_rates.objects.raw('select * from requests_game_rates having game_id='+ game_id +' order by rate DESC '):
        player_rank += 1
        if row_data.username == username:
            break
    page_data.update({'player_rank': player_rank})
    page_data.update({'scoin' : Users.objects.get(username=username).Scoin})
    page_data.update({'username':username})
    page_data.update({'game_id':game_id})
    template = loader.get_template('Game_page/index.html')
    return HttpResponse(template.render(page_data,request))

@csrf_exempt
def getHighScore(request):
    userID = request.GET['userID']
    score = request.GET['add']
    game_id = request.GET['game_id']
    if Game_rates.objects.filter(username=userID,game_id=game_id).count() > 0:
        user_game = Game_rates.objects.get(username=userID,game_id=game_id)
        if user_game.rate < int(score):
            timee = timezone.now()
            user_game.rate = int(score)
            user_game.save()
    else:
        timee = timezone.now()
        games = Game_rates(rate=score, game_id=game_id, username=userID, time=timee)
        games.save()
    response = {'status': 'success'}
    return HttpResponse(json.dumps(response))


def test(request):
    one_week_later = timezone.now() + timedelta(days=-7)
    remaining = timezone.now()
    for row_data in advertisement.objects.filter(advertisement_id=1):
        remaining = row_data.time
    remaining = remaining - timezone.now()
    remaining = remaining.days
    return HttpResponse(one_week_later.strftime("%Y-%m-%d %H:%M:%S.%f"))


def userData(request):
    user = request.GET['userID']
    json_data = {}
    item = []
    for row_data in Users.objects.filter(username=user):
        json_data = {'phonenumber': row_data.phonenumber, 'name': row_data.name, 'Bcoin': row_data.Scoin,
                     'level': row_data.level, 'notification': row_data.notifications}
    return HttpResponse(json.dumps(json_data))


##pages
def turnover_Dj(request):
    user_id = request.GET['username']
    template = loader.get_template('Turnover/Index.html')
    page_data = {}
    items = []
    for row_data in users_payments.objects.filter(username=user_id):
        items.append({'title': row_data.title, 'scoin': row_data.Scoin, 'mode': row_data.mode})
    page_data = {'items': items}
    return HttpResponse(template.render(page_data, request))


def notifs(request):
    username = request.GET['username']
    items = []
    page_data = {}
    for row_data in notifications.objects.filter(username=username, seen='n'):
        items.append({'title': row_data.title, 'message': row_data.message})
        row_data.seen = 's'
        row_data.save()
    page_data = {'items': items}
    template = loader.get_template('notification_page/index.html')
    return HttpResponse(template.render(page_data, request))


def Buy(request):
    template = loader.get_template('Buy/index.html')
    ad_id = request.GET['ad_id']
    user_id = request.GET['userID']
    page_data = {}
    page_data_parse = {}
    for row_data in advertisement.objects.raw('select * from requests_advertisement where advertisement_id=' + ad_id):
        remaining = row_data.time - timezone.now()
        time_data = ""
        typeoftime = 0
        page_data_parse['available'] = False
        if int(remaining.days) > 0:
            page_data_parse['day'] = remaining.days
        else:
            page_data_parse['day'] = 0
        hour = remaining.seconds // 3600
        if hour > 0:
            page_data_parse['hour'] = hour
        else:
            page_data_parse['hour'] = 0
        minute = (remaining.seconds // 60) % 60
        if minute > 0:
            page_data_parse['minute'] = minute
        else:
            page_data_parse['minute'] = 0
        seconds = remaining.seconds - (minute * 60) - (hour * 3600)
        if seconds > 0:
            page_data_parse['seconds'] = seconds
        else:
            page_data_parse['seconds'] = 0
        page_data_parse.update({'desc': row_data.description, 'title': row_data.title})
        page_data.update(
            {'Scoin_cost': row_data.Scoin_cost, 'ad_id': row_data.advertisement_id, 'minlevel': row_data.minlevel})
    for row_data in Users.objects.filter(username=user_id):
        page_data.update({'user_id': row_data.userID, 'user_level': row_data.level, 'user_scoin': row_data.Scoin})
    if int(page_data['Scoin_cost']) > int(page_data['user_scoin']):
        page_data_parse['inner_alert'] = 'شما Sکوین کافی ندارید'
    elif int(page_data['minlevel']) > int(page_data['user_level']):
        page_data_parse['inner_alert'] = 'سطح شما ابتدا باید به ' + str(page_data['minlevel']) + ' برسد'
    else:
        page_data_parse['inner_alert'] = 'خرید با موفقیت انجام شد'
        page_data_parse['available'] = True
    page_data_parse['service_id'] = ad_id
    page_data_parse['username'] = user_id
    return HttpResponse(template.render(page_data_parse, request))


def submit_buy(request):

    service_code = request.GET['service_code']
    username = request.GET['username']
    page_data_parse = {}
    page_data = {}
    user_data = Users.objects.get(username=username)
    for row_data in advertisement.objects.raw(
            'select * from requests_advertisement where advertisement_id=' + service_code):
        remaining = row_data.time - timezone.now()
        time_data = ""
        typeoftime = 0
        page_data_parse['available'] = False
        if int(remaining.days) > 0:
            page_data_parse['day'] = remaining.days
        else:
            page_data_parse['day'] = 0
        hour = remaining.seconds // 3600
        if hour > 0:
            page_data_parse['hour'] = hour
        else:
            page_data_parse['hour'] = 0
        minute = (remaining.seconds // 60) % 60
        if minute > 0:
            page_data_parse['minute'] = minute
        else:
            page_data_parse['minute'] = 0
        seconds = remaining.seconds - (minute * 60) - (hour * 3600)
        if seconds > 0:
            page_data_parse['seconds'] = seconds
        else:
            page_data_parse['seconds'] = 0
        page_data_parse.update({'desc': row_data.description, 'title': row_data.title})
        page_data.update(
            {'Scoin_cost': row_data.Scoin_cost, 'ad_id': row_data.advertisement_id, 'minlevel': row_data.minlevel})
    page_data.update({'user_id': user_data.userID, 'user_level': user_data.level, 'user_scoin': user_data.Scoin})
    if int(page_data['Scoin_cost']) > int(page_data['user_scoin']):
        page_data_parse['inner_alert'] = 'شما Sکوین کافی ندارید'
    elif int(page_data['minlevel']) > int(page_data['user_level']):
        page_data_parse['inner_alert'] = 'سطح شما ابتدا باید به ' + str(page_data['minlevel']) + ' برسد'
    else:
        page_data_parse['inner_alert'] = "خرید با موفقیت انجام شد"
        code = ""
        user_data.Scoin -= int(page_data['Scoin_cost'])
        user_data.save()
        for row_data in codes.objects.filter(id=int(service_code)).values():
            page_data_parse['inner_alert'] += "<br>" + row_data['code'] + "  : کدمحصول موردنظر"
        page_data_parse['available'] = True
    return HttpResponse(page_data_parse['inner_alert'])


def get_notif(request):
    data = {'startnotif': True, 'title': 'kir', 'message': 'kire khar'}
    return HttpResponse(json.dumps(data))


def check_user_exists(request):
    phonenumber = request.GET['phonenumber']
    json_data = {}
    for row_data in Users.objects.filter(phonenumber=phonenumber):
        json_data.update(
            {'Bcoin': row_data.Scoin, 'username': row_data.username, 'name': row_data.name, 'registered': True})
    if (json_data.get('Bcoin') == None):
        json_data['registered'] = False
    return HttpResponse(json.dumps(json_data, ensure_ascii=False))


def check_username_exists(request):
    username = request.GET['username']
    json_data = {}
    for row_data in Users.objects.filter(username=username):
        json_data.update({'exists': True})
    if (json_data.get('exists') == None):
        json_data['exists'] = False
    return HttpResponse(json.dumps(json_data))


def return_name(request):
    username = request.GET['username']
    json_data = {}
    for row_data in Users.objects.filter(username=username).values():
        name = row_data['name'].split('.')
        json_data['name'] = name[0] + " " + name[1]
        json_data['level'] = row_data['level']
        json_data['scoin'] = row_data['Scoin']
    return HttpResponse(json.dumps(json_data, ensure_ascii=False))


def get_video(request):
    json_data = {
        'video_link': 'https://hw2.cdn.asset.aparat.com/aparat-video/42e5ed3715e23fa63f43a5d97dc4815c13296973-480p__72958.mp4',
        'scoin': 100}
    return HttpResponse(json.dumps(json_data, ensure_ascii=False))


def video_award(request):
    secretkey = request.GET['secretkey']
    secretnumber = secretkey[0:4]
    secretnumber = int(secretnumber)
    secretstr = secretkey[4:6]
    authenticated = False
    if (secretnumber % 5 == 1 and secretstr == 'ac'):
        authenticated = True
    elif (secretnumber % 3 == 2 and secretstr == 'dr'):
        authenticated = True
    elif (secretnumber % 7 == 4 and secretstr == 'lf'):
        authenticated = True
    elif (secretstr == 'kr'):
        authenticated = True
    if authenticated:
        reagent_user = Users.objects.get(username=request.GET['username'])
        reagent_user.Scoin += int(request.GET['scoin'])
        reagent_user.save()
    return HttpResponse('ok')


# requests handler



@csrf_exempt
def submit_new_ad(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    pic_links = body['pic_link'].split(',')
    ad = advertisement(title=body['title'], description=body['description'],
                       short_description=body['short_description'], time=body['time'],
                       minlevel=1, old_cost=body['old_cost'], off=body['off'],
                       link=body['link'],
                       pic_link=pic_links[0], rate=body['rate'], rate_count=body['rate_count'],
                       bought=body['bought'], longitude=body['long'],
                       latitude=body['lat'], Scoin_available=0, Scoin_cost=0, priority=10,
                       cost=body['cost'])
    ad.save()
    for items in pic_links:
        if items != None:
            adc = AD_pics(ad=ad, pic_link=items)
            adc.save()
    categories_items = body['categories'].split(',')
    for items in categories_items:
        if items != '':
            category = Categories.objects.get(id=int(items))
            adca = ADCategory(ad=ad, category=category)
            adca.save()

    return HttpResponse(ad.advertisement_id)
