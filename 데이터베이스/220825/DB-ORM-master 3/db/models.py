from django.db import models

# 1번
class Director(models.Model):
    name = models.TextField()
    debut = models.DateTimeField()
    country = models.TextField()

class Genre(models.Model):
    title = models.TextField()


class Movie(models.Model):
    director = models.ForeignKey(Director,on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre,on_delete=models.CASCADE)
    title = models.TextField()
    opening_date = models.DateField()
    running_time = models.IntegerField()
    screening = models.BooleanField()


# 4번
director = Director.objects.get(name='봉준호')
print(f'id : {director.id}')
print(f'name : {director.name}')
print(f'debut : {director.debut}')
print(f'debut : {director.country}')


# 5번-첫번째 방법
drama = Genre.objects.get(title="드라마")
print(f'id : {drama.id}\ntitle : {drama.title}')

#5번-두번째 방법
genre = Genre.objects.get(title = '드라마')
print(f'id : {genre.id}')
print(f'title : {genre.title}')


# 6번
movie = Movie()

director_ = Director.objects.get(name='봉준호')
genre_ = Genre.objects.get(title='드라마')

movie.director = director_
movie.genre = genre_
movie.title = '기생충'
movie.opening_date = '2019-05-30'
movie.running_time = '132'
movie.screening = 'False'

movie.save()
# 6번 - QuerySet 이용하기
Movie.objects.create(director = director_, genre = genre_, title = '기생충', opening_date = '2019-05-30', running_time = 132, screening = False)

# 7번
movies = [("봉준호", "드라마", "괴물", "2006-07-27", 119, False),
("봉준호", "SF", "설국열차", "2013-10-30", 125, False),
("김한민", "사극", "한산", "2022-07-27", 129, True),
("최동훈", "SF", "외계+인", "2022-07-20", 142, False),
("이정재", "첩보", "헌트", "2022-08-10", 125, True),
("이경규", "액션", "복수혈전", "1992-10-10", 88, False),
("한재림", "재난", "비상선언", "2022-08-03", 140, True),
("Joseph Kosinski", "액션", "탑건 : 매버릭", "2022-06-22", 130, True)]

for mo in movies:
    movie = Movie()
    director_ = Director.objects.get(name=mo[0])
    genre_ = Genre.objects.get(title=mo[1])
    title_ = mo[2]
    opening_date_ = mo[3]
    running_time_ = mo[4]
    screening_ = mo[5]

    movie.director = director_
    movie.genre = genre_
    movie.title = title_
    movie.opening_date = opening_date_
    movie.running_time = running_time_
    movie.screening = screening_
    movie.save()





# 8번
movie = Movie.objects.all() # 리스트

for i in movie:
    print(i.director, i.genre, i.title, i.opening_date, i.screening)

# 9번


# 10번--1
see = Movie.objects.all()

for i in see:
    print(i.director.name, i.genre.title, i.title,
    i.opening_date, i.running_time,
    i.screening)

# 10번--2

for i in movie:
    print(i.director.name, i.genre.title, i.title, i.opening_date, i.screening)