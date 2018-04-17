import datetime

from django.utils import timezone
from django.test import TestCase
from django.urls import reverse

from .models import Create


def create_create(create_text, days):
    """
    Create a create with the given `create_text` and published the
    given number of `days` offset to now (negative for creates published
    in the past, positive for creates that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Create.objects.create(create_text=create_text, time=time)


class CreateIndexViewTests(TestCase):
    def test_no_creates(self):
        """
        If no creates exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('currencies:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No currencies are available.")
        self.assertQuerysetEqual(response.context['latest_create_list'], [])

    def test_past_create(self):
        """
        Creates with a time in the past are displayed on the
        index page.
        """
        create_create(create_text="Past create.", days=-30)
        response = self.client.get(reverse('currencies:index'))
        self.assertQuerysetEqual(
            response.context['latest_create_list'],
            ['<Create: Past create.>']
        )

    def test_future_create(self):
        """
        Creates with a time in the future aren't displayed on
        the index page.
        """
        create_create(create_text="Future create.", days=30)
        response = self.client.get(reverse('currencies:index'))
        self.assertContains(response, "No currencies are available.")
        self.assertQuerysetEqual(response.context['latest_create_list'], [])

    def test_future_create_and_past_create(self):
        """
        Even if both past and future creates exist, only past creates
        are displayed.
        """
        create_create(create_text="Past create.", days=-30)
        create_create(create_text="Future create.", days=30)
        response = self.client.get(reverse('currencies:index'))
        self.assertQuerysetEqual(
            response.context['latest_create_list'],
            ['<Create: Past create.>']
        )

    def test_two_past_creates(self):
        """
        The creates index page may display multiple creates.
        """
        create_create(create_text="Past create 1.", days=-30)
        create_create(create_text="Past create 2.", days=-5)
        response = self.client.get(reverse('currencies:index'))
        self.assertQuerysetEqual(
            response.context['latest_create_list'],
            ['<Create: Past create 2.>', '<Create: Past create 1.>']
        )


class CreateModelTests(TestCase):

    def test_created_with_future_create(self):
        """
        created() returns False for creates whose time
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_create = Create(time=time)
        self.assertIs(future_create.created(), False)

    def test_created_with_old_create(self):
        """
        created() returns False for creates whose time
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_create = Create(time=time)
        self.assertIs(old_create.created(), False)

    def test_created_with_recent_create(self):
        """
        created() returns True for creates whose time
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_create = Create(time=time)
        self.assertIs(recent_create.created(), True)


class CreateDetailViewTests(TestCase):
    def test_future_create(self):
        """
        The detail view of a create with a time in the future
        returns a 404 not found.
        """
        future_create = create_create(create_text='Future create.', days=5)
        url = reverse('currencies:detail', args=(future_create.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_create(self):
        """
        The detail view of a create with a time in the past
        displays the create's text.
        """
        past_create = create_create(create_text='Past Create.', days=-5)
        url = reverse('currencies:detail', args=(past_create.id,))
        response = self.client.get(url)
        self.assertContains(response, past_create.create_text)
