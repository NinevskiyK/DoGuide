from django.db import models
import json
import requests
from django.contrib.auth.models import User
from lk.models import Profile


class Excursion(models.Model):
    Place = models.CharField(max_length=200, help_text="Введи место твоей экскурсии!")
    S_coor = models.FloatField(default=0)
    N_coor = models.FloatField(default=0)
    Img = models.ImageField(upload_to='excursion_title')
    Description = models.TextField(help_text="Опиши себя и свою экскурсию!")
    Max_number = models.SmallIntegerField(help_text="Введи, какое максимальное количество человек может быть на твоей экскурсии")
    Cost = models.SmallIntegerField(help_text="Введи, сколько стоит твоя экскурсия")
    Time = models.SmallIntegerField(help_text="Введи, сколько экскурсия будет длиться")
    City = models.CharField(max_length=40, help_text="Введи город проведения экскурсии")
    Country = models.CharField(max_length=40, help_text="Введи страну проведения экскурсии", default='Россия')
    Short_description = models.CharField(max_length=60, help_text="Введи короткое описание твоей экскурсии", default='')
    Number_of_user = models.SmallIntegerField(help_text="Сколько человек записалось на твою экскурсию", default=0)
    Made_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    def get_coor(self):
        address = self.City + ' ' + self.Place
        request = requests.get(
            "https://geocode-maps.yandex.ru/1.x?geocode={}&apikey=0be7f9af-cccd-4838-af31-9e9a8d19df0f&format=json".format(
                address))
        request.encoding = 'utf-8'
        j = json.loads(request.text)
        request.encoding = 'utf-8'
        N, S = (j['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['boundedBy']['Envelope'][
            'lowerCorner']).split(' ')
        N = float(N)
        S = float(S)
        N1, S1 = (j['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['boundedBy']['Envelope'][
            'upperCorner']).split(' ')
        N1 = float(N1)
        S1 = float(S1)
        N += N1
        S += S1
        N /= 2
        S /= 2
        self.S_coor = S
        self.N_coor = N
        self.save()

    @staticmethod
    def create_json(e):
        with open('search/static/search/data.json', 'r') as file:
            file_text = file.read()
            j = json.loads(file_text)
            j['features'] = []
            Excursion.get_coor(e)
            j['features'].append({"type": "Feature", "id": e.pk, "geometry": {"type": "Point", "coordinates": [
                float(e.S_coor), float(e.N_coor)]},
                                  "properties": {"hintContent": e.Short_description}})
        with open('search/static/search/data.json', 'w') as file:
            json.dump(j, file)


class Book(models.Model):
    vk = models.CharField(max_length=50, help_text="Введи ссылку на твой ВК")
    data = models.DateField(help_text="Выбери удобное для тебя время")
    excursion = models.ForeignKey(Excursion, on_delete=models.SET_NULL, null=True, blank=True)