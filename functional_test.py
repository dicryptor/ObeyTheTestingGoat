from selenium import webdriver
import unittest

class NewvisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_list_and_retrieve_later(self):
        ## checking out new cool website to manage to-do lists
        self.browser.get('http://localhost:8000')

        ## notices page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test')


## invited to enter to-do item straight away

## types "Buy peacock feathers" into a text box

## hit enter, page updates to show newly added item, 1: Buy peacock feathers

## waiting text box inviting to add another item. Enter "Use peacock feathers to make a fly" (very methodical)

## Page updates again to show both items

## persistence: site will generate a unique url with some explanatory text

## visit that url to show persistent to-do list

## satisfied, go back to the real world


if __name__ == "__main__":
    unittest.main(warnings='ignore')