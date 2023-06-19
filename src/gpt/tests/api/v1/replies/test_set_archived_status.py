import pytest

from rest_framework import status

from gpt.models import Reply

pytestmark = [
    pytest.mark.django_db,
]

BASE_URL: str = "/api/v1/replies/status/archived/"


@pytest.fixture
def url() -> str:
    return BASE_URL


@pytest.mark.parametrize("quantity", [2, 5, 10])
def test_archived_successful(as_user, user, factory, url: str, quantity):
    factory.cycle(quantity).reply(author=user, status=Reply.Status.ARCHIVED)

    as_user.post(url, expected_status=status.HTTP_200_OK)

    assert Reply.objects.filter(author=user, status=Reply.Status.ARCHIVED).count() == quantity
