from presentation.visualization.results import scored_news
from presentation.vars.arguments import set_language
from presentation.visualization import results
from bussiness_logic.data_processing import filters
from data_access.database import save_register, retreive_data
import py_cui


def show_news():
    for _ in filters.filtered_list:
        print(_)


class App:

    def __init__(self, master):
        # Variable that will store user inputs from form
        self.form_results = None

        # The root py_cui window
        self.master = master

        # We want to show what user entered into form on exit
        self.master.run_on_exit(self.show_form_results)

        # Simple button that opens form popup
        self.master.add_button('Open Form', 1, 1, command=self.open_form)

    def save_form_results(self, form_output):
        """Callback function for form popup, simply saves results to instance variable
        """

        self.form_results = form_output

    def open_form(self):
        """Callback for button press, opens form popup
        """

        # The name of the form is Demo From
        # The second argument represents individual fields. These must be unique
        # We specify password fields to be ones where characters are replaced with '*'
        # Required fields will need to be populated before submission
        # The callback function is called with a single parameter - a dict of fields -> user inputs
        self.master.show_form_popup('Newspaper parameters',
                                    ['url', 'quantity', 'language', 'type'],
                                    required=['url', 'language'],

                                    callback=self.save_form_results)

    def show_form_results(self):
        """Helper function called on exit. Prints form results
        """
        news_number = int(self.form_results['quantity'])
        url = self.form_results['url']
        language = self.form_results['language']
        type = self.form_results['type']
        set_language(language)
        results.execute_search(url, news_number)
        filters.filterNews(scored_news, type)
        show_news()

        save_register(news_number, url, type)
        print("Algunas búsquedas recientes:")
        retreive_data()
        #print(str(self.form_results))


# Create the UI
root = py_cui.PyCUI(3, 3)

# Use unicode box characters for borders
root.toggle_unicode_borders()

# Initialize wrapper class
app = App(root)

# Start the UI
root.start()
