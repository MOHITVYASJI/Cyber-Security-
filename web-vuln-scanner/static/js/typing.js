function typeEffect(element, speed) {
    let text = element.innerHTML;
    element.innerHTML = "";
    let i = 0;
    function typing() {
        if (i < text.length) {
            element.innerHTML += text.charAt(i);
            i++;
            setTimeout(typing, speed);
        }
    }
    typing();
}

window.onload = function() {
    document.querySelectorAll(".type-effect").forEach(function(el) {
        typeEffect(el, 20); // 20ms per character
    });
};
