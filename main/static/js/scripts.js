


// Inventory List Modal for Delete
document.addEventListener('DOMContentLoaded', function() {
    var deleteModalElems = document.querySelectorAll('[id^="deleteModal-"]');
    var deleteModals = [];
    deleteModalElems.forEach(function(elem) {
        deleteModals.push(new bootstrap.Modal(elem));
    });
});



// Booking Modal for Delete - this is handles in the booking.html 
/*

In both cases, a modal is used to ask for confirmation before deleting an item. 
The difference is in how the delete action is handled once the user clicks the "Confirm" button.
In the case of the inventory items, the deletion is done using JavaScript and an AJAX request. 
This is useful when you want to perform the deletion without a full page reload. 
JavaScript is used to send a request to the server to delete the item, 
and once the server confirms the deletion, the JavaScript code updates the page to remove the deleted item from the list.
For the bookings, a more traditional approach is used. 
When the user clicks the "Confirm" button, the form is submitted, and the server processes the request. 
This approach requires a page reload, as the server sends a redirect response to the updated calendar page. 
This is a simpler approach, and it does not require any JavaScript code, 
but it lacks the seamless user experience provided by the AJAX-based approach.
In summary, JavaScript was used for deleting inventory items to provide a smoother user experience without a page reload. 
For bookings, a more traditional approach was used, which does not require JavaScript but 
involves a page reload. The choice between the two methods depends on your preference, project requirements, 
and the desired user experience.


*/


