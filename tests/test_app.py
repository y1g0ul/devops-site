import unittest

from app import create_app


class PortfolioRoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.client = create_app({"TESTING": True}).test_client()

    def test_index(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn("НИКИТА", response.get_data(as_text=True))

    def test_health(self):
        response = self.client.get("/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"status": "ok"})

    def test_resume_download(self):
        response = self.client.get("/resume/nikita-kirilenko-resume.pdf")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, "application/pdf")
        self.assertIn("attachment", response.headers["Content-Disposition"])
        response.close()

    def test_unknown_resume_is_not_exposed(self):
        response = self.client.get("/resume/unknown.pdf")

        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
