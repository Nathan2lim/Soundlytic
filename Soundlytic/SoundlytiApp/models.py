from django.db import models

class copyright(models.Model): 
    id_copyright = models.IntegerField(primary_key=True, unique=True)
    text = models.TextField()
    type = models.TextField()

  
class external_ids(models.Model): 
    id_external_ids = models.IntegerField(primary_key=True, unique=True)
    isrc = models.TextField()
    ean = models.TextField()
    upc = models.TextField()

  
class id_external_urls(models.Model): 
    id_url = models.IntegerField(primary_key=True, unique=True)
    url = models.TextField()
    type = models.TextField()
    avanced = models.TextField()

  
class Artiste(models.Model): 
    id_artiste = models.(primary_key=True, unique=True)
    external_urls = models.ForeignKey('id_external_urls', to_field='id_url')
    followers = models.IntegerField()
    total_follower = models.IntegerField()
    genres = models.TextField()
    href = models.TextField()
    image_small = models.ForeignKey('id_external_urls', to_field='id_url')
    image_medium = models.ForeignKey('id_external_urls', to_field='id_url')
    image_large = models.ForeignKey('id_external_urls', to_field='id_url')
    name_artiste = models.TextField()
    popularity = models.FloatField()
    type = models.TextField()
    uri = models.TextField()

  
class id_platforme(models.Model): 
    id_platforme = models.IntegerField(primary_key=True, unique=True)
    id_sound = models.TextField()

  
class ALBUM(models.Model): 
    id_album = models.IntegerField(primary_key=True, unique=True)
    type_album = models.TextField()
    total_tracks = models.IntegerField()
    available_market = models.TextField()
    id_external_urls = models.ForeignKey('id_external_urls', to_field='id_url')
    href = models.TextField()
    id_platforme = models.ForeignKey('id_platforme', to_field='id_platforme')
    image = models.ForeignKey('id_external_urls', to_field='id_url')
    name = models.TextField()
    release_date = models.DateField()
    release_date_precision = models.DateField()
    type = models.TextField()
    id_artiste = models.ForeignKey('Artiste', to_field='id_artiste')
    copyright = models.ForeignKey('copyright', to_field='id_copyright')
    eternal_ids = models.ForeignKey('external_ids', to_field='id_external_ids')
    genres = models.TextField()
    label = models.TextField()
    popularity = models.FloatField()
    is_playable = models.BooleanField()

  
class SOUND(models.Model): 
    id_sound = models.IntegerField(primary_key=True, unique=True)
    id_album = models.TextField()
    available_markets = models.TextField()
    disc_number = models.IntegerField()
    duration_ms = models.IntegerField()
    explicit = models.BooleanField()
    id_external_urls = models.ForeignKey('id_external_urls', to_field='id_url')
    id_external_ids = models.ForeignKey('external_ids', to_field='id_external_ids')
    href = models.TextField()
    linked_from = models.TextField()
    name = models.TextField()
    popularity = models.FloatField()
    preview_url = models.TextField()
    track_number = models.IntegerField()
    type = models.TextField()
    uri = models.TextField()
    is_local = models.BooleanField()
    image_small = models.ForeignKey('id_external_urls', to_field='id_url')
    image_medium = models.ForeignKey('id_external_urls', to_field='id_url')
    image_large = models.ForeignKey('id_external_urls', to_field='id_url')
    id_platforme = models.ForeignKey('id_platforme', to_field='id_platforme')

  
class R_musiqueart(models.Model): 
    id_musiqueArtiste = models.IntegerField(primary_key=True, unique=True)
    id_album = models.ForeignKey('ALBUM', to_field='id_album')
    id_artiste = models.ForeignKey('Artiste', to_field='id_artiste')
    id_sound = models.ForeignKey('SOUND', to_field='id_sound')

  
class Utilisateur(models.Model): 
    id_user = models.IntegerField(primary_key=True, unique=True)
    username = models.TextField()
    firstname = models.TextField()
    lastnatme = models.TextField()
    password = models.AutoField()

  
class stream_user(models.Model): 
    id_musiqueArtiste = models.ForeignKey('R_musiqueart', to_field='id_musiqueArtiste')
    id_user = models.ForeignKey('Utilisateur', to_field='id_user')
    date = models.DateField()
    duration_played = models.AutoField()

