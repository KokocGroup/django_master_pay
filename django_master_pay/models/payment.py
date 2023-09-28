from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Payment(models.Model):
    STATUS_WAIT = 0
    STATUS_PAID = 1
    STATUS_PAID_PERCENT = 2
    STATUS_CANCEL = 3
    STATUS_COMPLETE = 4
    STATUS_ERROR = 5
    STATUS_UNREALIZABLE = 6

    STATUS_CHOICES = (
        (STATUS_WAIT, _("Ожидает")),
        (STATUS_PAID, _("Выплачивается")),
        (STATUS_PAID_PERCENT, _("Выплачен частично")),
        (STATUS_ERROR, _("Ошибка")),
        (STATUS_COMPLETE, _("Выплачен")),
        (STATUS_CANCEL, _("Отменен пользователем")),
        (STATUS_UNREALIZABLE, _("Неисполнимый")),
    )

    WORK_STATUSES = (STATUS_WAIT, STATUS_PAID, STATUS_PAID_PERCENT)

    created_at = models.DateTimeField(_('Создан'), default=timezone.now)
    updated_at = models.DateTimeField(_('Обновлен'), auto_now=True)
    external_id = models.CharField(_("Внешний ключ"), max_length=250)
    master_pay_id = models.CharField(_("Индефикатор MasterPay"), max_length=250)
    partner_id = models.CharField(_("Индефикатор партнера в MasterPay"), max_length=250)
    status = models.PositiveSmallIntegerField(_("Статус"), choices=STATUS_CHOICES, default=STATUS_WAIT)
    error = models.TextField(_('Ошибка автоматической выплаты'), blank=True, null=True)
    record_data = JSONField(_("RAW data"))

    class Meta:
        verbose_name = _("Платеж")
        verbose_name_plural = _("Платежи")

    def __str__(self):
        return "#{} external_id={} master_pay_id={} status={}".format(
            self.id, self.external_id, self.master_pay_id, self.status
        )

    @classmethod
    def status_display(cls, status):
        status_dict = dict(cls.STATUS_CHOICES)
        return status_dict[status]
