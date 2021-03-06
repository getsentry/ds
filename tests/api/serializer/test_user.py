from freight.api.serializer import serialize
from freight.testutils import TestCase


class UserSerializerTest(TestCase):
    def test_simple(self):
        user = self.create_user()

        result = serialize(user)
        assert result["id"] == str(user.id)
        assert result["name"] == user.name
