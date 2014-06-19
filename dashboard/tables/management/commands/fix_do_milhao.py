from django.core.management.base import BaseCommand
from tables.models import CountryOperation, CountryOperationIT, \
    GrantsFinances


class Command(BaseCommand):

    def handle(self, *args, **options):
        country_operation = CountryOperation.objects.all()
        for co in country_operation:
            if co.it_disbursements_planned < 10:
                co.it_disbursements_planned *= 1000000

            if co.it_disbursements_actual < 10:
                co.it_disbursements_actual *= 1000000

            if co.it_execution_planned < 10:
                co.it_execution_planned *= 1000000

            if co.it_execution_actual < 10:
                co.it_execution_actual *= 1000000

            co.save()

        country_operation_it = CountryOperationIT.objects.all()
        for obj in country_operation_it:
            if obj.it < 10:
                obj.it *= 1000000
                obj.save()

        grants_finances = GrantsFinances.objects.all()
        for obj in grants_finances:
            if obj.value < 100:
                obj.value *= 1000000
                obj.save()
