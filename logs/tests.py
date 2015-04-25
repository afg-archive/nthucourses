from django.test import TestCase

import traceback

from logs.models import Log, Logger


class LoggerTestCase(TestCase):
    def test_logger_returns_log_instance(self):
        with Logger('test_logger_returns_log_instance') as log:
            self.assertIsInstance(log, Log)

    def test_logs_are_saved(self):
        with Logger('test_logs_are_saved') as log:
            the_log = log
        self.assertEqual(Log.objects.count(), 1)
        self.assertEqual(Log.objects.get(), the_log)

    def test_logs_are_created_at_the_beginning(self):
        with Logger('test_logs_are_created_at_the_beginning'):
            self.assertEqual(Log.objects.count(), 1)

    def test_log_status_is_running_while_running(self):
        with Logger('test_log_status_is_running_whie_running') as log:
            self.assertIs(log.success, None)
            self.assertEqual(log.status, 'running')

    def test_log_status_is_failure_if_failed(self):
        try:
            with Logger('test_log_status_is_failure_if_failed'):
                raise Exception('This is an exception')
        except Exception:
            log = Log.objects.get()
            self.assertEqual(log.success, False)
            self.assertEqual(log.status, 'failure')
        else:
            self.fail('Exception not raised')

    def test_log_status_is_success_if_success(self):
        with Logger('test_log_status_is_success_if_success'):
            pass
        log = Log.objects.get()
        self.assertEqual(log.success, True)
        self.assertEqual(log.status, 'success')

    def test_log_message_saved(self):
        message = 'test_log_message_saved'
        with Logger(message) as log:
            self.assertEqual(log.message, message)
        log = Log.objects.get()
        self.assertEqual(log.message, message)

    def test_exc_information_empty_if_success(self):
        with Logger('test_exc_information_empty_if_success'):
            pass
        log = Log.objects.get()
        self.assertEqual(log.traceback, '')
        self.assertEqual(log.exc_name, '')

    def test_logger_saves_exception_name(self):
        wrong_key = 'ThisKeyDoesNotExistHahahaha'
        with self.assertRaises(KeyError):
            with Logger('test_logger_saves_exception_name'):
                {}[wrong_key]
        log = Log.objects.get()
        self.assertEqual(log.exc_name, 'KeyError')

    def test_logger_saves_exception_traceback(self):
        try:
            with Logger('test_logger_saves_exception_traceback'):
                {}['this_key_does_not_exist']
        except KeyError:
            log = Log.objects.get()
            self.assertMultiLineEqual(log.traceback, traceback.format_exc())
        else:
            self.fail('KeyError not raised')

    def test_time_is_recorded(self):
        with Logger('test_time_is_recorded') as log:
            self.assertIsNot(log.started, None)
            self.assertIs(log.ended, None)
        self.assertIsNot(log.started, None)
        self.assertIsNot(log.ended, None)
