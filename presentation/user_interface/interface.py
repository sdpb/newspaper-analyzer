from presentation.visualization.results import scored_news
from bussiness_logic.data_processing import filters
from data_access.database import save_register, retreive_data
from presentation.vars.arguments import set_origin_language, set_target_language
from presentation.visualization import results


import py_cui


def show_news():
    for _ in filters.filtered_list:
        print(_)


def show_nonfiltered_news():
    for _ in scored_news:
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
        self.master.add_button('Buscar', 1, 1, command=self.open_form)

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
                                    ['url', 'quantity', 'origin language', 'target language', 'type'],
                                    required=['url', 'origin language', 'target language'],

                                    callback=self.save_form_results)

    def show_form_results(self):
        quantity = self.form_results['quantity']
        news_number = int(quantity) if quantity else None
        url = self.form_results['url']
        origin_language = self.form_results['origin language']
        target_language = self.form_results['target language']
        sentimental_type = self.form_results['type']
        set_origin_language(origin_language)
        set_target_language(target_language)
        results.execute_search(url, news_number)
        filters.filterNews(scored_news, sentimental_type)

        if sentimental_type == '':
            show_nonfiltered_news()
        else:
            show_news()

        save_register(news_number, url, sentimental_type)
        print("Algunas búsquedas recientes:")
        retreive_data()
        # print(str(self.form_results))


# Create the UI
root = py_cui.PyCUI(3, 3)

# Use unicode box characters for borders
root.toggle_unicode_borders()

# Initialize wrapper class
app = App(root)

# Start the UI
root.start()
