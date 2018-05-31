import unittest
from pathlib import Path
from quina import widgets


class MyTestCase(unittest.TestCase):
    cache_path = Path('.cache')
    mock_pdf_path = cache_path / 'mock.pdf'
    mock_png_path = cache_path / 'mock.png'
    mock_svg_path = cache_path / 'mock.svg'

    def setUp(self):
        self.cache_path.mkdir(parents=True, exist_ok=True)

    def tearDown(self):
        if self.mock_pdf_path.exists():
            self.mock_pdf_path.unlink()
        if self.mock_png_path.exists():
            self.mock_png_path.unlink()
        if self.mock_svg_path.exists():
            self.mock_svg_path.unlink()

    def test_set_central_widget(self):
        main_window = widgets.MainWindow()
        sub_widget = widgets.Widget()
        main_window.set_central_widget(sub_widget)
        self.assertIsNotNone(main_window.center_widget)
        main_window.close()

        dock_widget = widgets.DockWidget()
        sub_widget = widgets.Widget()
        dock_widget.set_central_widget(sub_widget)
        self.assertIsNotNone(dock_widget.center_widget)
        dock_widget.set_focus()
        dock_widget.close()

    def test_widget_export(self):
        w = widgets.Widget()
        w.resize(1000, 800)
        self.assertTrue(w.export_to_pdf(self.mock_pdf_path))
        self.assertTrue(self.mock_pdf_path.exists())

        w.resize(800, 1000)
        self.assertTrue(w.export_to_pdf(self.mock_pdf_path))
        self.assertTrue(self.mock_pdf_path.exists())

        self.assertTrue(w.export_to_picture(self.mock_png_path))
        self.assertTrue(self.mock_png_path.exists())

        self.assertTrue(w.export_to_svg(self.mock_svg_path))
        self.assertTrue(self.mock_svg_path.exists())


if __name__ == '__main__':
    unittest.main()
