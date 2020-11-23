from presentation.visualization.results import scored_news
from bussiness_logic.data_processing import TemplateFilters, filters
from data_access.database import save_register, retreive_data
from presentation.vars import arguments
from presentation.vars.arguments import set_origin_language, set_target_language, set_news_type
from presentation.visualization import results

import py_cui


class SosNoticiaUI:

    def __init__(self, master):
        # Variable that will store user inputs from form
        self.form_results = None

        self.master = master

        

        # The scrolled list cells that will contain our tasks in each of the three categories
        self.history_scroll_cell = self.master.add_scroll_menu(
            'HISTORY', 0, 0, row_span=6, column_span=2)
        self.news_items_scroll_cell = self.master.add_scroll_menu(
            'News items', 0, 2, row_span=7, column_span=4)

        # Button for entering new items

        # Form button
        self.new_query_button = self.master.add_button(
            'New query', 6, 0, column_span=2, command=self.open_form)

        # Redo comment if history element is selected and enter is pressed
        self.history_scroll_cell.add_key_command(
            py_cui.keys.KEY_ENTER, self.redo_query)
        
        self.news_items_scroll_cell.add_key_command(
            py_cui.keys.KEY_ENTER, self.get_new)

        self.show_history()


    def redo_query(self):
        """ Make a query """

        history_item = self.history_scroll_cell.get()
        if history_item is None:
            self.master.show_error_popup(
                'No Item', 'There is no item in the list to redo the query')
            return

    def get_new(self):

        news_item = self.news_items_scroll_cell.get()
        if news_item is None:
            self.master.show_error_popup(
                'No Item', 'There is no item in the list')
            return
        score = news_item.get_score()
        type_score = results.process_score(score)
        text = f'{score} {type_score} - Subjectivity {news_item.get_subjectivity()}'
        self.master.show_message_popup(news_item.get_title(), text)

    def show_history(self):

        records = retreive_data()
        self.history_scroll_cell.clear()
        for row in records:
            self.history_scroll_cell.add_item(f'{row}')


    def show_news_items(self):

        
        self.get_news_items()
        self.news_items_scroll_cell.clear()

        if arguments.NEWS_TYPE == '':
            self.show_nonfiltered_news()
        else:
            self.show_filtered_news()


    def open_form(self):
        """Callback for button press, opens form popup
        """

        self.master.show_form_popup('Newspaper parameters',
                                    ['url', 'quantity', 'origin language',
                                        'target language', 'type'],
                                    required=[
                                        'url', 'origin language', 'target language'], callback=self.save_form_results)


    def save_form_results(self, form_output):
        """Callback function for form popup, simply saves results to instance variable
        """
        self.form_results = form_output
        self.show_news_items()
        self.show_history()
        


    def get_news_items(self):
        quantity = self.form_results['quantity']
        news_number = int(quantity) if quantity else None
        url = self.form_results['url']
        origin_language = self.form_results['origin language']
        target_language = self.form_results['target language']
        sentimental_type = self.form_results['type']

        set_origin_language(origin_language)
        set_target_language(target_language)
        set_news_type(sentimental_type)

        results.execute_search(url, news_number)
        
        save_register(news_number, url, sentimental_type)


    def show_filtered_news(self):
        filters.filterNews(arguments.NEWS_TYPE)
        for _ in TemplateFilters.filtered_list:
            text = f'{_.get_title()}'
            #text = f'{_[0]}\n{_[1]} - subjectivity {_[2]}'
            # print(text)
            self.news_items_scroll_cell.add_item(_)


    def show_nonfiltered_news(self):
        'https://www.nytimes.com/'
        for _ in scored_news:
            text = f'{_.get_title()}'
            # print(text)
            self.news_items_scroll_cell.add_item(_)


    def remove_item(self):
        """ Remove a todo item """

        self.history_scroll_cell.remove_selected_item()


# Create the CUI with 7 rows 6 columns, pass it to the wrapper object, and start it
root = py_cui.PyCUI(7, 6)
root.set_title('SOS NOTICIA')
root.toggle_unicode_borders()
s = SosNoticiaUI(root)
root.enable_logging()


root.start()
