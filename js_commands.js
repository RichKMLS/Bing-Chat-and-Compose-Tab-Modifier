// the following can be ran as a snippet in the developer console manually.

// Define an IIFE function that sets the maxLength property of the search box to 25000 if the website is example1.com.
(function() {
    if (window.location.hostname === 'https://edgeservices.bing.com/edgesvc/chat') {
        let root = document.querySelector("#b_sydConvCont > cib-serp")
            .shadowRoot;
        root.querySelector("#cib-action-bar-main").shadowRoot
            .querySelector("#searchbox").maxLength = "25000";
    }
})();

// Define an IIFE function that removes elements with specified selectors from the DOM,
// changes the text content of a button to ‘Prompt’, and sets the maxLength property
// and placeholder text of a text input element if the website is example2.com.
(function() {
    if (window.location.hostname === 'https://edgeservices.bing.com/edgesvc/compose') {
        let decorations = ['.option-section', '#input_heading',
            '#preview_heading', '#insert_button', '#change_suggestions'];
        decorations.forEach((decoration) => {
            let elements = document.querySelectorAll(decoration);
            elements.forEach((element) => {
                element.parentNode.removeChild(element);
            });
        });
        let composeButton = document.querySelector('#compose_button');
        composeButton.textContent = 'Prompt';
        let promptText = document.querySelector('#prompt_text');
        promptText.maxLength = "25000";
        promptText.placeholder = '...';
    }
})();
