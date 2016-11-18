# coding=utf-8
from .fetch import fetch


class Country(object):
    """
    Docs: https://vk.com/dev/database.getCountriesById
    """
    __slots__ = ('id', 'title')

    @classmethod
    def from_json(cls, json_obj):
        country = cls()
        country.id = json_obj.get('id')
        country.title = json_obj.get('title')
        return country

    @classmethod
    def get_country_by_id(cls, country_id):
        country_json = fetch('database.getCountriesById', country_ids=country_id)[0]
        return cls.from_json(country_json)

    def __repr__(self):
        return u"<Country: {0}>".format(self.id)


class City(object):
    """
    Docs: https://vk.com/dev/database.getCitiesById
    """
    __slots__ = ('id', 'title')

    @classmethod
    def from_json(cls, json_obj):
        city = cls()
        city.id = json_obj.get('id')
        city.title = json_obj.get('title')
        return city

    @classmethod
    def get_city_by_id(cls, city_id):
        city_json = fetch('database.getCitiesById', city_ids=city_id)[0]
        return cls.from_json(city_json)

    def __repr__(self):
        return u"<City: {0}>".format(self.id)
