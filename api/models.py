from django.db import models
from django.utils.translation import gettext_lazy as _

class Hudud(models.Model):
    hudud = models.CharField(max_length=100)

    def __str__(self):
        return str(self.hudud)


class Tashkilot(models.Model):
    tashkilot = models.CharField(max_length=100)

    def __str__(self):
        return str(self.tashkilot)


class Lavozim(models.Model):
    lavozim = models.CharField(max_length=120)

    def __str__(self):
        return str(self.lavozim)


class SportTuri(models.Model):
    sportturi = models.CharField(max_length=212)

    def __str__(self):
        return str(self.sportturi)


class Razryad(models.Model):
    razryad_nomi = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.razryad_nomi)


class Profile(models.Model):
    class HolatCheck(models.TextChoices):
        Qabul = 'Qabul qilindi', _('Qabul qilindi')
        Ignor = 'Rad etildi', _('Rad etildi')
        NotYet = 'Ko\'rib chiqilmoqda', _('Ko\'rib chiqilmoqda')

    class DocCheck(models.TextChoices):
        Toliq = 'To\'liq', _('To\'liq')
        Chala = 'Chala', _('Chala')

    class IfChecked(models.TextChoices):
        tekshirilgan = 'Tekshirilgan', _('Tekshirilgan')
        tekshirilmagan = 'Tekshirilmagan', _('Tekshirilmagan')

    class MalumotChesk(models.TextChoices):
        oliy = 'Oliy', _('Oliy')
        urta = 'O\'rta maxsus/Professional', _('O\'rta maxsus/Professional')

    class ShaklChesk(models.TextChoices):
        kunduzgi = 'Kunduzgi', _('Kunduzgi')
        masofaviy = 'Masofaviy', _('Masofaviy')

    class TurChesk(models.TextChoices):
        shartnoma = 'Shartnoma asosida', _('Shartnoma asosida')
        reja = 'Reja asosida', _('Reja asosida')

    class TilChesk(models.TextChoices):
        uzbek = 'O\'zbek tili', _('O\'zbek tili')
        rus = 'Rus tili', _('Rus tili')

    telegram_id = models.IntegerField(null=True)
    full_name = models.CharField(max_length=156, null=True, blank=True)
    phone = models.CharField(max_length=25, null=True)
    Passport = models.CharField(max_length=45, null=True)
    Hudud = models.ForeignKey(Hudud, on_delete=models.CASCADE, null=True)
    Shahar = models.CharField(max_length=120, null=True)
    tashkilot = models.ForeignKey(Tashkilot, on_delete=models.CASCADE, null=True)
    malumot = models.CharField(max_length=30,
                               choices=MalumotChesk.choices,
                               null=True)
    mutaxasislik = models.CharField(max_length=255, null=True)
    lavozim = models.ForeignKey(Lavozim, on_delete=models.CASCADE, null=True)
    unvoni = models.ForeignKey(Razryad, on_delete=models.CASCADE, null=True)
    oqishshakli = models.CharField(max_length=30,
                                   choices=ShaklChesk.choices,
                                   null=True)
    oqishturi = models.CharField(max_length=30,
                                 choices=TurChesk.choices,
                                 null=True)
    sportturi = models.ForeignKey(SportTuri, on_delete=models.CASCADE, null=True)
    talimtili = models.CharField(max_length=15,
                                 choices=TilChesk.choices,
                                 null=True)
    passportcopy = models.FileField(null=True)
    image = models.ImageField(null=True)
    diplomcopy = models.FileField(null=True)
    inn = models.FileField(null=True)
    buyruq = models.FileField(null=True)
    razryad = models.FileField(null=True)

    tuliqligi = models.CharField(max_length=20,
                                 choices=DocCheck.choices,
                                 default=DocCheck.Chala, )
    holat = models.CharField(max_length=20,
                             choices=HolatCheck.choices,
                             default=HolatCheck.NotYet, )
    sabab = models.TextField(default='Xujjatlar to\'liq emas')

    tekshirilganli = models.CharField(max_length=30,
                                      choices=IfChecked.choices,
                                      default=IfChecked.tekshirilmagan)

    def __str__(self):
        return str(self.full_name)

    @property
    def passportURL(self):
        try:
            return self.passportcopy.url
        except:
            return self.passportcopy

    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return self.image

    @property
    def diplomURL(self):
        try:
            return self.diplomcopy.url
        except:
            return self.diplomcopy

    @property
    def innURL(self):
        try:
            return self.inn.url
        except:
            return self.inn

    @property
    def buyruqURL(self):
        try:
            return self.buyruq.url
        except:
            return self.buyruq

    @property
    def razryadURL(self):
        try:
            return self.razryad.url
        except:
            return self.razryad
