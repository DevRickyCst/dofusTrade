window.addEventListener("load", function() {
    if (document.getElementById('charactere-btn')) {
        adjustCharacterButtonPosition();
    }
});

window.addEventListener('scroll', function() {
    if (document.getElementById('charactere-btn')) {
        adjustCharacterButtonPosition();
    }
});

window.addEventListener('resize', function() {
    if (document.getElementById('charactere-btn')) {
        adjustCharacterButtonPosition();
    }
});

function adjustCharacterButtonPosition() {
    var scrollPosition = this.window.scrollY;
    var child = document.getElementById('charactere-btn');
    var bottomRelativeToPage = document.body.scrollHeight - scrollPosition - window.innerHeight + 20;
    child.style.bottom = bottomRelativeToPage + 'px';
}