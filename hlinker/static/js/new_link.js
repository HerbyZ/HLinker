const
    submitBtn = document.getElementById('submitNewLink'),
    nameInput = document.getElementById('name'),
    parentLinkInput = document.getElementById('parent_link');

let
    correctName,
    correctParent;

function checkCorrect() {
    if (correctName && correctParent) {
        submitBtn.disabled = false;
    } else {
        submitBtn.disabled = true;
    }
}

nameInput.oninput = function() {
    if (nameInput.value.length >= 4) {
        correctName = true;
    } else {
        correctName = false;
    }

    checkCorrect();
}

parentLinkInput.oninput = function() {
    if (parentLinkInput.value.length >= 9) {
        correctParent = true;
    } else {
        correctParent = false;
    }

    checkCorrect();
}

parentLinkInput.onchange = function() {
    if (!parentLinkInput.value.startsWith('https://')) {
        const oldValue = parentLinkInput.value;
        parentLinkInput.value = 'https://' + oldValue;

        if (parentLinkInput.value.length >= 9) {
            correctParent = true;
        } else {
            correctParent = false;
        }
    }
}
