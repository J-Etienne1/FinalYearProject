# Import necessary modules and models
from django.db.models import Sum
import io
from datetime import datetime
from django.http import HttpResponse
from django.views import View
from calendar_component.models import Booking
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from django.shortcuts import render
import base64


# Use Agg backend to support rendering to a file without a display
import matplotlib
matplotlib.use('Agg')

# Create a class-based view for finance
class Finance(View):
    def get(self, request):
        # Retrieve all events in the current year
        events = Booking.objects.filter(start_time__year=datetime.now().year)

        # Calculate income and expenses for each month in the current year
        data = events.values('start_time__month').annotate(
            income=Sum('quote'),
            expense=Sum('materials_cost'),
        )

        # Create lists of months, income, and expenses for plotting
        months = [datetime(1900, x['start_time__month'], 1).strftime('%B') for x in data]
        in_values = [x['income'] for x in data]
        ex_values = [x['expense'] for x in data]

        # Use Matplotlib to plot the income and expenses side by side
        fig, ax = plt.subplots()
        fig.set_size_inches(8, 6)
        fig.subplots_adjust(bottom=0.2)


        ax.bar([x - 0.2 for x in range(len(data))], in_values, width=0.4, label='Income')
        ax.bar([x + 0.2 for x in range(len(data))], ex_values, width=0.4, label='Expense')
        ax.set_xticks(range(len(data)))
        ax.set_xticklabels(months, rotation=45)

        ax.legend()
        ax.set_xlabel("Months")
        ax.set_ylabel("Euros")

        # Convert the plot to a base64-encoded string for display in the HTML template
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        image_data = base64.b64encode(buf.getvalue()).decode()

        # Render the finance.html template with the plot and the current datetime
        return render(request, 'finance.html', {'image': image_data, 'now': datetime.now()})







"""
The code defines a class-based view for finance that retrieves data from the Event model, calculates income and expenses for each month in the current year, and creates a bar chart of the results using Matplotlib. The resulting plot is then converted to a base64-encoded string and passed to a template called finance.html along with the current datetime.
io.BytesIO() creates a new in-memory bytes buffer, which is used to store binary data in memory. In this specific code, it creates a new empty byte buffer that can be used to write image data to. The buf variable is used to hold the data of the generated graph image as a bytes buffer, which is then encoded using Base64 and passed to the finance.html template for display.
plt.savefig(buf, format='png') saves the current figure to the given buffer buf in PNG format.
buf.seek(0) sets the current file position in the buffer buf to the beginning of the buffer, which allows the buffer to be read from the beginning. This is necessary because after plt.savefig() is called, the file position will be at the end of the buffer.
The plot generated using matplotlib is saved in the buffer as an image in PNG format. However, to display the plot in an HTML template, we need to convert it into a format that can be displayed in the browser. One way to achieve this is by encoding the PNG image into a base64-encoded string, which can be displayed as an img tag in the HTML template.
So, the line image_data = base64.b64encode(image_data).decode() encodes the PNG image in the buffer to a base64-encoded string that can be passed to the HTML template as a context variable.
Here, we first calculate both income and expenses for each month in the current year in a single query using annotate. Then we create lists of months, income, and expenses as before. In the plotting step, we create a single ax object and call ax.bar twice to plot the income and expenses side by side. We adjust the positions of the bars for each month by subtracting or adding 0.2 to the x-coordinates. Finally, we set the x-tick labels and other axes properties as before.
"""