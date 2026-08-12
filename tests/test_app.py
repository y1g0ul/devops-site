import unittest

from app import create_app


class PortfolioRoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.client = create_app({"TESTING": True}).test_client()

    def test_index(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn("НИКИТА", response.get_data(as_text=True))

    def test_terminal_input_cannot_submit_a_get_form(self):
        response = self.client.get("/")
        html = response.get_data(as_text=True)

        self.assertNotIn('<form id="terminal-form"', html)
        self.assertIn('id="terminal-input-group"', html)
        self.assertIn("js/main.js?v=2", html)

    def test_terminal_enter_is_handled_in_javascript(self):
        response = self.client.get("/static/js/main.js")
        javascript = response.get_data(as_text=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn('addEventListener("keydown"', javascript)
        self.assertIn('event.key !== "Enter"', javascript)
        self.assertIn("event.preventDefault()", javascript)
        response.close()

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
