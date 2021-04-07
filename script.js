var addAnchorLinkTests = document.getElementById('link');
addAnchorLinkTests.addEventListener('click', () => {
    addElement("Link", " ", " ");
    addElement(" ", "Click/Tap the link", "Links to the ${url}.");
})

var addTextInputTests = document.getElementById('text');
addTextInputTests.addEventListener('click', () => {
    addElement("${label} Input Required", " ", " ");
    addElement(" ", "Submit the form without any data", "The form is not submitted.");
    addElement(" ", "Submit the form without any data", "The error message is displayed. ${error}");    
    addElement("${label} Input Boundary", " ", " ");
    addElement(" ", "Enter the text into the input field: ${boundary}+1", "Only ${boundary} is able to be entered.");
    addElement("${label} Input Accepted Characters", " ", " ");
    addElement(" ", "Enter the text into the input field: ${characters}", "Only ${characters} are able to be entered.");
})



function addElement(t, a, r){
    var itemTable = document.getElementById("itemList");

    var tr = itemTable.insertRow(itemTable.rows.length);
    var title = tr.insertCell(0);
    var action = tr.insertCell(1);
    var result = tr.insertCell(2);

    title.innerHTML = t;
    action.innerHTML = a;
    result.innerHTML = r;
}