from unittest import TestCase
from .printer import Printer,PrinterError

class TestPrinter(TestCase):
    @classmethod
    def setUp(self): ## Method to run before every test
        self.printer = Printer(pages_per_s=2.0,capacity=300)

    def test_print_within_capacity(self):
        message = self.printer.print(25)
        self.assertEqual(f"Printed 25 pages in 12.50 seconds.", message)

    def test_print_outside_capacity(self):
        with self.assertRaises(PrinterError):
            self.printer.print(301)

    def test_print_exact_capacity(self):
        self.printer.print(self.printer._capacity)

    def test_printer_speed(self):
        pages = 10
        expected = "Printed 10 pages in 5.00 seconds."

        result = self.printer.print(pages)
        self.assertEqual(result,expected)