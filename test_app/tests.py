from django.utils import unittest
from django.test.client import RequestFactory
from django.contrib.auth.models import User, AnonymousUser
from django.conf import settings
import logging


class DjangoHandlerTestCase(unittest.TestCase):
    """
    Tests for Django integration - logging configuration etc.

    This test case uses the Django settings configuration information to
    set up a logger.
    """

    def setUp(self):
        self.logger = logging.getLogger('test')
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.request = self.factory.get('/')

    def test_django_settings(self):
        "Test that standard django settings pick up logging config."
        logger = logging.getLogger("test")
        self.assertIsNotNone(logger)
        self.assertEqual(len(logger.handlers), 1)
        self.assertEqual(logger.handlers[0].name, "django_errordite")
        self.assertEqual(logger.handlers[0].token, settings.ERRORDITE_TOKEN)

    def test_with_request(self):
        "Test logging an error containing basic request info."
        func = self.test_with_request
        try:
            throw_exception(func.__name__)
        except:
            self.request.META['HTTP_USER_AGENT'] = "Django test runner"
            self.request.META['HTTP_X_FORWARDED_FOR'] = "Django test runner"
            self.logger.error(func.__doc__,
                extra={"request": self.request}
            )
            print ("Please check Errordite for an error containing HTTP "
                "request info, with message: '%s'" % func.__doc__)

    def test_with_request_header_forwarded(self):
        "Test logging an error with X-Forward-For request header."
        func = self.test_with_request_header_forwarded
        try:
            throw_exception(func.__name__)
        except:
            self.request.META['HTTP_USER_AGENT'] = "Django test runner"
            self.request.META['HTTP_X_FORWARDED_FOR'] = "ip goes here"
            self.logger.error(func.__doc__,
                extra={"request": self.request}
            )
            print ("Please check Errordite for an error containing HTTP "
                "request info, with message: '%s'" % func.__doc__)

    def test_with_request_header_remote_addr(self):
        "Test logging an error with REMOTE_ADDR request header."
        func = self.test_with_request_header_remote_addr
        try:
            throw_exception(func.__name__)
        except:
            self.request.META['HTTP_USER_AGENT'] = "Django test runner"
            self.request.META['REMOTE_ADDR'] = "remote address goes here"
            self.logger.error(func.__doc__,
                extra={"request": self.request}
            )
            print ("Please check Errordite for an error containing HTTP "
                "request info, with message: '%s'" % func.__doc__)

    def test_with_request_and_anonymous_user(self):
        "Test logging an error caused by AnonymousUser."
        func = self.test_with_request_and_anonymous_user
        try:
            self.request.user = AnonymousUser()
            throw_exception(func.__name__)
        except:
            self.logger.error(func.__doc__, extra={"request": self.request})
            print ("Please check Errordite for an error containing HTTP "
                "request info, with message: '%s'" % func.__doc__)

    def test_with_request_and_known_user(self):
        "Test logging an error caused by a known user."
        func = self.test_with_request_and_known_user
        try:
            self.request.user = User.objects.create_user(
                "fred", "fred@example.com", "fred's password"
            )
            throw_exception(func.__name__)
        except:
            self.logger.error(func.__doc__, extra={"request": self.request})
            print ("Please check Errordite for an error containing HTTP "
                "request info, with message: '%s'" % func.__doc__)


class CustomException(Exception):
    def __init__(self, message):
        super(CustomException, self).__init__(message)


def throw_exception(message):
    raise CustomException(message)
