import unittest
from unittest import TestLoader, TestSuite, TextTestRunner
from tests.FeedbackFormElementsTets import FeedbackFormElementsTests
from tests.FeedbackPermissionToReadTests import FeedbackPermissionToRead
from tests.FeedbackTests import FeedbackTests
from tests.LogInTests import LoginTests
from tests.RequestsTests import RequestTests
from tests.OnboardingTests import OnboardingTests
from tests.SignUpTests import SignUpTests



if __name__ == '__main__':

    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(SignUpTests),
        loader.loadTestsFromTestCase(LoginTests),
        loader.loadTestsFromTestCase(OnboardingTests),
        loader.loadTestsFromTestCase(FeedbackFormElementsTests),
        loader.loadTestsFromTestCase(FeedbackPermissionToRead),
        loader.loadTestsFromTestCase(FeedbackTests),
        loader.loadTestsFromTestCase(RequestTests)
    ))

    runner = TextTestRunner()
    runner.run(suite)
