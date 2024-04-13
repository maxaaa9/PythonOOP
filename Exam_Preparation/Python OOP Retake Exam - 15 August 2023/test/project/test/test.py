from project.trip import Trip
from unittest import TestCase, main


class TestTrip(TestCase):

    def setUp(self) -> None:
        self.test_trip = Trip(1000, 5, True)

    def test_init(self):
        self.assertEqual(1000, self.test_trip.budget)
        self.assertEqual(5, self.test_trip.travelers)
        self.assertTrue(self.test_trip.is_family)

    def test_travelers_raise_VE(self):
        with self.assertRaises(ValueError) as ve:
            self.test_trip.travelers = 0

        self.assertEqual('At least one traveler is required!', str(ve.exception))

    def test_is_family_as_False(self):
        self.test_trip.travelers = 1
        self.test_trip.is_family = True

        self.assertFalse(self.test_trip.is_family)

    def test_book_a_trip_with_invalid_destination(self):
        result = self.test_trip.book_a_trip("Unknown")

        self.assertEqual('This destination is not in our offers, please choose a new one!', result)

    def test_book_with_valid_destination_with_not_enough_budget(self):
        result = self.test_trip.book_a_trip('New Zealand')

        self.assertEqual(0, len(self.test_trip.booked_destinations_paid_amounts))
        self.assertEqual('Your budget is not enough!', result)

    def test_book_with_valid_destination_successful(self):
        self.test_trip.budget = 100_000
        calculation = self.test_trip.budget - (self.test_trip.travelers * 7500) * 0.9
        result = self.test_trip.book_a_trip('New Zealand')

        self.assertEqual(1, len(self.test_trip.booked_destinations_paid_amounts))
        self.assertEqual(calculation, self.test_trip.budget)
        self.assertEqual(f'Successfully booked destination New Zealand! Your budget left is {calculation:.2f}', result)

    def test_booking_status_without_books(self):
        self.assertEqual(f"No bookings yet. Budget: {self.test_trip.budget:.2f}", self.test_trip.booking_status())

    def test_booking_correct_return_output(self):
        self.test_trip.budget = 10_000
        self.test_trip.book_a_trip("Bulgaria")
        paid_amount = (500 * self.test_trip.travelers) * 0.9

        expect = f"Booked Destination: Bulgaria\nPaid Amount: {paid_amount:.2f}"
        expect += f"\nNumber of Travelers: 5\nBudget Left: {self.test_trip.budget:.2f}"

        self.assertEqual(expect, self.test_trip.booking_status())

