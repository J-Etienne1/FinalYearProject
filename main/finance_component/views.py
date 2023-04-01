from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from calendar_component.models import Booking
from matplotlib.ticker import FuncFormatter
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Sum
import matplotlib.pyplot as plt
from datetime import datetime
import base64
import io



# Use for for matplotlib to Agg that can be used to create images
import matplotlib
matplotlib.use('Agg')


class Finance(View,LoginRequiredMixin):
    login_url = '/login'

    def get(self, request):
        # gets all the bookings for a user for the year
        events = Booking.objects.filter(start_time__year=datetime.now().year, user=self.request.user)

        # uses start_time__month to group income and expenses
        group_income_expenses = events.values('start_time__month').annotate(
            income=Sum('quote'),
            expense=Sum('materials_cost'),
        )

        # makes a lists of months
        months = [datetime(2000, x['start_time__month'], 1).strftime('%B') for x in group_income_expenses] # for each month convert datetime to the month
        # list through income per month
        income_per_month = [x['income'] for x in group_income_expenses]
        # list through expense per month
        expense_per_month = [x['expense'] for x in group_income_expenses]

        # create a figure and axes to hold plots on the graph
        fig, ax = plt.subplots()
        fig.set_size_inches(8, 6)
        fig.subplots_adjust(bottom=0.2)

        # set up barcharts for the income and expenses per month
        ax.bar([x - 0.2 for x in range(len(group_income_expenses))], income_per_month, width=0.4, label='Income')
        ax.bar([x + 0.2 for x in range(len(group_income_expenses))], expense_per_month, width=0.4, label='Expense')
        ax.set_xticks(range(len(group_income_expenses))) # get as many x-axes ticks as there are months to display
        ax.set_xticklabels(months, rotation=45) # rotate months so text doesnt overlap

        # get up a legend for the graph
        ax.legend()
        ax.set_xlabel("Months")
        ax.set_ylabel("Euros")

        # make a memory buffer
        buf = io.BytesIO()
        # saves the graph as a png image to the buffer so that a image file does not need to be saved to the database
        plt.savefig(buf, format='png') 
        # need to set the buffer to 0 to read what is it
        buf.seek(0)
        # converts the buffer to a base64 so that the graph can be used on the finacne page
        income_expense_graph = base64.b64encode(buf.getvalue()).decode()

        # returns the finacne page with the finace graph and the current year
        return render(request, 'finance.html', {'finance_bar_graph': income_expense_graph, 'current_year': datetime.now()})





