from base.base_class import Base


class Finish_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    # Getters

    # Actions

    # Methods

    def finish(self):
        self.get_current_url()
        self.assert_url('https://kazan.rus-buket.ru/opayment')
        self.get_screenshot()
