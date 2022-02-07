from main import app


class TestWebPage:
    def setup(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_page(self):
        response = self.app.get('/')
        assert response.status_code == 200
