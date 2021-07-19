from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.postgres.fields import JSONField


class Payment(models.Model):
    STATUS_NEW = 'NEW'
    STATUS_IN_WORK = 'IN_WORK'
    STATUS_DONE = 'DONE'
    STATUS_ERROR = 'ERROR'

    STATUS_CHOICES = (
        (STATUS_NEW, _("Новый")),
        (STATUS_IN_WORK, _("В работе")),
        (STATUS_DONE, _("Проведен")),
        (STATUS_ERROR, _("Ошибка"))
    )

    created_at = models.DateTimeField(_('Создан'), default=timezone.now)
    updated_at = models.DateTimeField(_('Обновлен'), auto_now=True)
    external_id = models.CharField(_("Внешний ключ"), max_length=250)
    master_pay_id = models.CharField(_("Индефикатор MasterPay"), max_length=250)
    status = models.CharField(_("Статус"), max_length=100, choices=STATUS_CHOICES, default=STATUS_NEW)
    record_data = JSONField(_("RAW data"))

    class Meta:
        verbose_name = _("Платеж")
        verbose_name_plural = _("Платежи")
