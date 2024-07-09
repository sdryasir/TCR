function menuAnimation(x) {
    x.classList.toggle("change");
    var element = document.getElementById("slideNav");
    element.classList.toggle("navSlide");
    var textFade = document.getElementById("sideBarText");
    textFade.classList.toggle("textFadeIn");
    var iconFade = document.getElementById("socialIcons");
    iconFade.classList.toggle("iconFadeIn");
  }






    // Function to show datepicker on input click
   // Function to show datepicker on input click
   function showDatepicker(input) {
    input.type = 'date';
    input.focus();
}

// Handle focus events to manage placeholder display
document.addEventListener('DOMContentLoaded', function() {
    const dateInputs = document.querySelectorAll('.date-input');
    dateInputs.forEach(input => {
        const defaultPlaceholder = input.placeholder;
        input.addEventListener('focus', function() {
            this.placeholder = '';
            this.type = 'date'; // Ensure input type remains 'date' on focus
        });
        input.addEventListener('blur', function() {
            if (!this.value) {
                this.placeholder = defaultPlaceholder;
                this.type = 'text'; // Reset to text input type if no date selected
            }
        });
    });
});











  
// OUR CARS DROP-DOWN

// Hero Section Schedule Section

